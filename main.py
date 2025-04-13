import os
import argparse
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_files = {"dev": ".env.dev", "test": ".env.test", "prod": ".env.prod"}

    env_file = env_files.get(environment)
    if not os.path.exists(env_file):
        raise FileNotFoundError(
            f"The environment file '{env_file}' could not be found."
        )
    load_dotenv(dotenv_path=env_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
