import inspect
import json
import os
from datetime import datetime
from enum import Enum
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Union,
    get_args,
    get_origin,
)

from pydantic import BaseModel, field_validator, model_validator
from pyspark.sql.dataframe import DataFrame

CURRENT_FILE_DIR = os.path.dirname(os.path.abspath(__file__))


DATE_FORMATTER = {
    "year": lambda x: str(x.year),
    "month": lambda x: str(x.month).zfill(2),
    "day": lambda x: str(x.day).zfill(2),
}


class FileType(str, Enum):
    CSV = "csv"
    JSON = "json"
    PARQUET = "parquet"


class Layer(str, Enum):
    LANDING = "landing"
    RAW = "raw"
    TRUSTED = "trusted"
    ANALYTICS = "analytics"


class Env(str, Enum):
    DEV = "dev"
    PRD = "prd"


class DatePartition(str, Enum):
    PART_YEAR = "part_year"
    PART_MONTH = "part_month"
    PART_DAY = "part_day"
    YEAR = "year"
    MONTH = "month"
    DAY = "day"


class FnKind(str, Enum):
    SINGLE = "single"
    BATCH = "batch"


class BaseModelJsonDumps(BaseModel):
    def __str__(self):
        return json.dumps(self.model_dump(), indent=2, default=str)


class AWSCredentials(BaseModelJsonDumps):
    aws_access_key_id: str
    aws_secret_access_key: str


class S3BucketParams(BaseModelJsonDumps):
    env: Env
    layer: Optional[Layer] = None
    ng_prefix: str = "ng"
    bucket_name: Optional[str] = None

    @model_validator(mode="before")
    def set_bucket_name_if_not_provided(cls, data):
        layer = data.get("layer").value
        env = data.get("env").value
        ng_prefix = data.get("ng_prefix", "ng")
        bucket_name = data.get("bucket_name")

        if bucket_name is None:
            if layer is None:
                raise ValueError(
                    "'layer' must be provided if 'bucket_name' is not provided"
                )
            data["bucket_name"] = f"{ng_prefix}-datalake-{layer}-{env}"

        return data


class S3ReadJsonParams(BaseModelJsonDumps):
    bucket_params: S3BucketParams
    path: str

    @field_validator("path")
    @classmethod
    def strip_slashes(cls, v: str) -> str:
        return v.strip("/")

    @field_validator("path")
    @classmethod
    def ensure_path_to_file_has_json_extension(cls, v: str) -> str:
        if not v.endswith(".json"):
            raise ValueError(
                f"For S3 schema, 'path' must have a '.json' extension. Received path: '{v}'"
            )

        return v


class DataFrameReadWriteParams(BaseModelJsonDumps):
    bucket_params: S3BucketParams
    specific_path: Optional[str] = None
    path_to_dataframe_root: Optional[str] = None
    file_type: FileType
    processing_date: Union[
        datetime,
        Literal["{{processing_date}}"],
        Literal["{{processing_date_previous}}"],
    ] = "{{processing_date}}"
    processing_date_partitions: Optional[List[DatePartition]] = None
    processing_date_partitions_first: bool = True
    column_partitions: Optional[List[str]] = None

    @model_validator(mode="before")
    def xor_specific_path_and_path_to_dataframe_root(cls, data):
        specific_path = data.get("specific_path")
        path_to_dataframe_root = data.get("path_to_dataframe_root")

        if specific_path is not None and path_to_dataframe_root is not None:
            raise ValueError(
                "'specific_path' and 'path_to_dataframe_root' cannot be passed together"
            )

        if specific_path is None and path_to_dataframe_root is None:
            raise ValueError(
                "Either 'specific_path' or 'path_to_dataframe_root' should be passed"
            )

        return data

    @field_validator("path_to_dataframe_root", "specific_path")
    def strip_slashes(cls, v: str) -> str:
        if v is not None:
            return v.strip("/")

    @field_validator("path_to_dataframe_root")
    def ensure_dataframe_root_parent_folder(cls, v: str) -> str:
        if v is not None and "/" not in v:
            raise ValueError(
                f"'path_to_dataframe_root' should have at least one parent folder inside the bucket. Ensure there is at least one slash ('/') in the path. Received path: '{v}'"
            )

        return v


class InputDataFrameParams(BaseModelJsonDumps):
    pyspark_schema_struct: Optional[Dict[str, Any]] = None
    s3_schema_path_params: Optional[S3ReadJsonParams] = None
    df_params: DataFrameReadWriteParams

    @model_validator(mode="before")
    def check_schema_mode(cls, data):
        pyspark_schema_struct = data.get("pyspark_schema_struct")
        s3_schema_path_params = data.get("s3_schema_path_params")

        if pyspark_schema_struct is not None and s3_schema_path_params is not None:
            raise ValueError(
                "'pyspark_schema_struct' and 's3_schema_path_params' cannot be passed together"
            )

        return data


class OutputDataFrameParams(BaseModelJsonDumps):
    write_schema_on_s3: bool = False
    overwrite: bool = False
    df_params: DataFrameReadWriteParams


class FnIndirect(BaseModelJsonDumps):
    fn_name: str
    fn_path: str


class TransformParams(BaseModelJsonDumps):
    transform_label: str
    fn_direct: Callable
    fn_indirect: Optional[FnIndirect] = None
    fn_kwargs: Optional[dict] = None
    apply_only_on: Optional[List[str]] = None
    fn_kind: Optional[FnKind] = None

    @model_validator(mode="before")
    def validate_fn_direct_indirect_and_apply_only_on(cls, data):
        fn_indirect = data.get("fn_indirect")
        fn_direct = data.get("fn_direct")
        apply_only_on = data.get("apply_only_on")

        def get_annotation_kind(annotation):
            origin = get_origin(annotation)
            args = get_args(annotation)

            if origin is dict and args[0] is str and issubclass(args[1], DataFrame):
                return FnKind.BATCH
            elif issubclass(annotation, DataFrame):
                return FnKind.SINGLE
            return None

        if fn_indirect is not None and fn_direct is not None:
            raise ValueError("'fn_indirect' and 'fn_direct' cannot be passed together")

        if fn_indirect is None and fn_direct is None:
            raise ValueError("Either 'fn_indirect' or 'fn_direct' should be passed")

        if fn_indirect:
            raise NotImplementedError("fn_indirect is not implemented yet")

        signature = inspect.signature(fn_direct)
        parameters = signature.parameters
        first_param_annotation = (
            list(parameters.values())[0].annotation if parameters else None
        )
        return_annotation = signature.return_annotation

        first_param_kind = get_annotation_kind(first_param_annotation)
        return_kind = get_annotation_kind(return_annotation)

        if (first_param_kind is None or return_kind is None) or (first_param_kind != return_kind):
            raise ValueError(
                "Function must have a DataFrame type hint as first parameter and return type hint, or a dict of [str, DataFrame] as first parameter hint and return type hint"
            )

        if first_param_kind != FnKind.SINGLE and apply_only_on is not None:
            raise ValueError(
                "'apply_only_on' should be passed only when 'fn_direct' has a DataFrame as first parameter, not a list of DataFrames"
            )

        # If the function has a DataFrame as first parameter, then it is a single function. If it has a dict of [str, DataFrame] as first parameter, then it is a batch function
        # TODO: This should be a private attribute
        data["fn_kind"] = first_param_kind

        return data


DataFrameDict = Dict[str, DataFrame]
InputDataFrameParamsDict = Dict[str, InputDataFrameParams]
OutputDataFrameParamsDict = Dict[str, OutputDataFrameParams]
TransformParamsDict = Dict[str, TransformParams]


class StepParams(BaseModelJsonDumps):
    input_dataframes_params: InputDataFrameParamsDict
    transform_params: Optional[TransformParamsDict] = None
    output_dataframes_params: Optional[OutputDataFrameParamsDict] = None


StepParamsDict = Dict[str, StepParams]
