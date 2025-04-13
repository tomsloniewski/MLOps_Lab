from pydantic_settings import BaseSettings
from pydantic import validator, ValidationError


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @validator("ENVIRONMENT")
    def validate_environment(cls, value):
        envs = {"dev", "test", "prod"}
        if value not in envs:
            raise ValidationError(
                f"Provided wrong environment: {value}. List of allowed environments: {envs}."
            )
        return value
