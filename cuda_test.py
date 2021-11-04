from numba import cuda
#print(cuda.gpus)
#
# import torch
# # device
# print('GPU: ',torch.cuda.is_available())
# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# print("Device: {}".format(device))
# print('GPU: ',torch.cuda.is_available())
#
# # print(dir(torch))
# import os
# a = os.environ.get('PYTORCH_CUDA_ALLOC_CONF','')
# print('PYTORCH_CUDA_ALLOC_CONF')
# print(dir(a))
# print(type(a))

import subprocess
import sys
import time
cmd = r"validate.sh corpora\en.test.txt C:\Users\woody\AppData\Local\Temp\tmpw_r2a9qi"
# C:\Program Files\Git\\bin\\bash.exe
# print(cmd.split())
#subprocess.run(["time"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# for i in cmd.split():
#     print(i)
#     print('-------------')
    #subprocess.run([i],shell=True)
#     #subprocess.Popen([i], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print('test',subprocess.call(cmd.split()))
cmd_list = cmd.split()
cmd_list.insert(0,'C:\Program Files\Git\\bin\\bash.exe')
print(cmd_list)
p = subprocess.Popen(cmd_list,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# time.sleep(5)
out, err = p.communicate()
print(out,float(out))
print(str(err))
sys.stderr.write(str(err))
