import logging
import os
from logging import handlers
from datetime import datetime


def get_filename():
    # 主要LOG資料夾
    root_dir = "LOG"

    # 確認LOG資料夾是否存在
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)

    # 寫入LOG檔案
    log_file = "log.log"
    save_path = os.path.join(root_dir, log_file)

    return save_path


class LOGGER():
    def __init__(self):
        self.FORMAT = '%(asctime)s (%(module)s) %(levelname)s: %(message)s'
        self.DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
        self.filename = get_filename()
        self.logger = logging.getLogger(self.filename)
        self.logger_format = logging.Formatter(self.FORMAT, self.DATE_FORMAT)

        # backupCount 儲存日誌的數量，過期自動刪除
        # when 按什麼日期格式切分
        self.handle = handlers.TimedRotatingFileHandler(filename=self.filename, when='midnight', backupCount=7,
                                                        encoding='utf-8')

        self.handle.setFormatter(self.logger_format)
        self.handle.setLevel(logging.DEBUG)
        self.logger.addHandler(self.handle)

        self.logger.setLevel(logging.DEBUG)

    def setDBHandler(self, dbHandler):
        self.logdbhandle = dbHandler
        self.logger.addHandler(self.logdbhandle)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)
