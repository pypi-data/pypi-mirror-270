import src.rsa_api
import time
import numpy as np
from matplotlib import pyplot as plt


rsa = src.rsa_api.RSA("/home/aromaniello/W/tek-drivers/")

rsa.DEVICE_SearchAndConnect(True)

rsa.CONFIG_SetCenterFreq(2.425e9)
rsa.CONFIG_SetReferenceLevel(-35)
rsa.IQSTREAM_SetAcqBandwidth(10e6)


# fig, ax = plt.subplots()

times = []

for i in range(10):
    tic = time.perf_counter()
    iqdata, status = rsa.IQSTREAM_Acquire(400, True)
    toc = time.perf_counter()
    times.append(toc-tic)
    print(status)
    # ax.plot(iqdata.real)
    # plt.pause(0.01)
    # plt.clf()
# plt.show()
print(np.mean(times))
rsa.DEVICE_Disconnect()
print("Disconnected")
# rsa.DEVICE_Disconnect()
