from pydantic import BaseModel, ConfigDict


class BaseExceptionSchema(BaseModel):
    status_code: int
    detail: str


class NotFoundExceptionSchema(BaseExceptionSchema):

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "detail": "Entity not found",
        },
    })
