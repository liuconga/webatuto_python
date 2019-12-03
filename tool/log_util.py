import logging
from logging import handlers


class Logger(object):
    logger: logging.Logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger = logging.getLogger('webauto_python')
            # 设置默认的日志级别
            cls.logger.setLevel(logging.DEBUG)
            console_handler=logging.StreamHandler()
            # 设置控制台输出日志级别
            console_handler.setLevel(logging.DEBUG)

            #设置文件日志输出
            file_handler=handlers.TimedRotatingFileHandler('../log/web_auto.log',when='s',interval=5,backupCount=2,encoding='utf-8')
            file_handler.setLevel(logging.DEBUG)
            cls.logger.addHandler(console_handler)
            cls.logger.addHandler(file_handler)
        return cls.logger


if __name__ == '__main__':
    Logger.get_logger().debug("debug---------")
    Logger.get_logger().info("info---------")
    Logger.get_logger().warning("warning---------")
    Logger.get_logger().error("error---------")
    Logger.get_logger().critical("critical---------")
