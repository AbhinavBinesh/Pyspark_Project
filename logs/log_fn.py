import logging

def log_Error(message):
    logging.basicConfig(filename='logs/loginfo.log',level=logging.ERROR,format="%(asctime)s,%(levelname)s,%(message)s")
    logging.error(f'There is some error while creating table: {message}')

def log_Info(message):
    logging.basicConfig(filename='logs/loginfo.log',level=logging.INFO,format="%(asctime)s,%(levelname)s,%(message)s")
    logging.info(f'{message}')