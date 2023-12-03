import os


def get_config():
    # 環境変数から設定を読み込む
    config_keys = [
        "RDS_MYSQL_USER",
        "RDS_MYSQL_PASSWORD",
        "RDS_MYSQL_HOST",
        "RDS_MYSQL_DB_NAME",
    ]

    # 読み込んだ設定を辞書として返す
    return {key.lower(): os.getenv(key) for key in config_keys}
