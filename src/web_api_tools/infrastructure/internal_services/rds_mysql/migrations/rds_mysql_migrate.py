import logging

from sqlalchemy import create_engine

from ..config.rds_mysql_config import get_config
from ..entities import Base
from ..entities.task_entity import (
    TaskEntity,  # TaskEntity imported dont remove
)

logging.basicConfig(level=logging.INFO)
logging.info(TaskEntity)

config = get_config()
DB_URL = (
    f"mysql+pymysql://{config['rds_mysql_user']}:"
    f"{config['rds_mysql_password']}@"
    f"{config['rds_mysql_host']}/"
    f"{config['rds_mysql_db_name']}?charset=utf8"
)
engine = create_engine(DB_URL, echo=True)


def reset_database():
    try:
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        logging.info("Database reset successful.")
    except Exception as e:
        logging.error(f"Error occurred: {e}")


if __name__ == "__main__":
    reset_database()
