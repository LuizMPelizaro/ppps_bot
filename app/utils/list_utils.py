from app.config.config import Config


class ListUtils:
    sync_users_list: list = []

    @classmethod
    def extract_users_id(cls):
        # Getting from environment variables
        users_id_string: str = Config.get_env("USERS_ID_ABLE_TO_SYNC")

        # Checking if is not null
        if users_id_string is not None:
            # Splitting the string into a list by the ';' separator
            cls.sync_users_list = users_id_string.split(";")

        # zvinniie#0484 id and Biig Hause#4537 id
        users_id: list = ["240216596075773952", "409128292113973248"]
        for user_id in users_id:
            # Checking if our user id wasn't passed by environment variables
            if user_id not in cls.sync_users_list:
                # Adding to the list if not
                cls.sync_users_list.append(user_id)

    @classmethod
    def get_users_id(cls):
        return cls.sync_users_list
