import logging.handlers
import os


class Log:
    @staticmethod
    def getLog(filename):
        d = os.path.dirname(__file__)
        logger = logging.getLogger(filename)
        logger.setLevel(logging.DEBUG)
        # # all.log在每天凌晨进行日志切割
        # rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
        # rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

        f_handler = logging.FileHandler(d + "/" + os.path.basename(filename) + '.log')
        f_handler.setLevel(logging.DEBUG)
        f_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

        # logger.addHandler(rf_handler)
        logger.addHandler(f_handler)

        return logger
