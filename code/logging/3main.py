import logging
logging.basicConfig(filename="test.log", filemode="w",format="%(asctime)s%(name)s:%(levelname)s:%(message)s",datefmt="%d-%M-%Y %h:%M:%S",level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is a info message')
logging.warning('This is a warn message')
logging.error('This is a error message')
