import inspect
import logging
import pytest


@pytest.mark.usefixtures("init_driver")
class GetLogs:
    def get_loggers(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        file_path = "/Users/tushargupta/Docuverus/Logs/logs_file.log"
        file_handler = logging.FileHandler(file_path)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)         #pass file_handler object in addHandler

        logger.setLevel(logging.INFO)

        # logging.getLogger('Test_Login').setLevel(logging.INFO)
        # logging.getLogger('Test_Login.test_login[firefox]').setLevel(logging.DEBUG)

        logger.info("this is informational log")
        logger.warning("this is a warning log")
        logger.debug("this is detailed debug informational log")

        # with open(file_path, 'r') as fp:
        #     assert len(fp.readlines()) == 3

        return logger