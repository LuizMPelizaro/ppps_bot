from datetime import datetime


class DateTimeUtils:
    started_at: datetime

    @classmethod
    def set_started_at(cls):
        cls.started_at = datetime.now()

    @classmethod
    def get_started_at(cls) -> datetime:
        return cls.started_at

    @staticmethod
    def get_current_time() -> str:
        return datetime.now().strftime('%H:%M:%S')
