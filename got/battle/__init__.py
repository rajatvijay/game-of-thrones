import logging
import os


def get_logger(file_name):
    """
    Gets logger for the ingestion process
    :param file_name: str
    :return: logger
    """
    logger = logging.getLogger('ingestion')
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(os.getcwd() + ("/temp/%s_logs.txt" % file_name))
    fh.setLevel(logging.DEBUG)

    logger.addHandler(fh)

    return logger
