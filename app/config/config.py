from dotenv import dotenv_values


class Config:
    config = dotenv_values(".env")

    @classmethod
    def get_env(cls, key: str) -> str:
        return cls.config.get(key)
