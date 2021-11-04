import logging,sys
from terminaltables import AsciiTable
filelog = True
path = r'log.txt'

logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)

# 调用模块时,如果错误引用，比如多次调用，每次会添加Handler，造成重复日志，这边每次都移除掉所有的handler，后面在重新添加，可以解决这类问题
while logger.hasHandlers():
    for i in logger.handlers:
        logger.removeHandler(i)

# file log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
if filelog:
    fh = logging.FileHandler(path,encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

# console log
formatter = logging.Formatter('%(message)s')
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

if __name__ == '__main__':
    logger.info("这是一个测试")

    a = [['Key', 'Value'], ['Source', '确切 地 说 是 政界 某些 人 这 方面 的 言行 正 反映 了 右翼 势力 的 政治 企望'], ['Target',
                                                                                           'to put it precisely  the words and deeds of some people of the political circles have reflected exactly the political intention of the rightwing forces \r'],
         ['Predict',
          'the said said said that that said said to the the that the and and that the to the that to to and']]
    print(a)
    sampling_table = AsciiTable(a)
    logger.info(str(a))
    logger.info("\n"+str(sampling_table.table))