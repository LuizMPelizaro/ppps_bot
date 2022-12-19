from datetime import datetime


class DateTimeUtils:

    @staticmethod
    def get_current_time() -> str:
        return datetime.now().strftime('%H:%M:%S')
