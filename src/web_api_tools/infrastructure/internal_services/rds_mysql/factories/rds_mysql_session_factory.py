from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from ..config.rds_mysql_config import get_config


def get_database_config():
    # 環境変数から設定を読み込む
    config = get_config()
    return {
        "user": config["rds_mysql_user"],
        "password": config["rds_mysql_password"],
        "host": config["rds_mysql_host"],
        "db_name": config["rds_mysql_db_name"],
    }


def create_database_url(config):
    # データベースURLの作成
    return (
        f"mysql+asyncmy://{config['user']}:{config['password']}"
        f"@{config['host']}/{config['db_name']}?charset=utf8"
    )


def create_engine():
    # SQLAlchemy エンジンの作成（非同期対応）
    config = get_database_config()
    url = create_database_url(config)
    return create_async_engine(url)


# 非同期セッションファクトリの作成
RdsMysqlSessionFactory = sessionmaker(
    bind=create_engine(),
    autocommit=False,
    autoflush=False,
    class_=AsyncSession,
)
