import logging
logging.basicConfig(filename='test.log',filemode='w',format="%(asctime)s %(name)s:%(levelname)s:%(message)s",datefmt="%d-%M-%Y %H:%M:%s",level=logging.DEBUG)
a = 5
b = 0
try:
    c = a / b
except Exception as e:
    # 推荐这种形式
    logging.exception("Exception occurred")
    logging.error("Exception occurred", exc_info=True)
    logging.log(level=logging.DEBUG,msg="Exception occurred", exc_info=True)
