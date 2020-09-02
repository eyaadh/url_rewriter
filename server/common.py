import configparser


class Common:
    def __init__(self):
        self.app_config = "server/working_dir/config.ini"
        self.config = configparser.ConfigParser()
        self.config.read(self.app_config)

        self.db_host = self.config.get("database", "host")
        self.db_username = self.config.get("database", "username")
        self.db_password = self.config.get("database", "password")
        self.db_name = self.config.get("database", "db_name")
