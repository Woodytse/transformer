from terminaltables import AsciiTable
import datetime
import time
from util import get_logger
import os
import logging
a = [['Key', 'Value'], ['Source', '确切 地 说 是 政界 某些 人 这 方面 的 言行 正 反映 了 右翼 势力 的 政治 企望'], ['Target', 'to put it precisely  the words and deeds of some people of the political circles have reflected exactly the political intention of the rightwing forces \r'], ['Predict', 'the said said said that that said said to the the that the and and that the to the that to to and']]
print(a)
sampling_table = AsciiTable(a)

#print("\n" +str(sampling_table.table))
print(sampling_table.table.__str__())
print(str(a))

print(str(datetime.datetime.now()))

if not os.path.exists("log"):
    os.mkdir("log")

log_path = os.path.join(
    "log", "log-" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + ".txt"
)

fh = logging.FileHandler(log_path,encoding='utf-8')
logger = get_logger(log_path)
logger.addHandler(fh)

logger.info(str(a))