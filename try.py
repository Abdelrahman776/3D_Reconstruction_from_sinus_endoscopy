# import torch
# print(torch.cuda.is_available())
# print(torch.version.cuda)

import pycuda.autoinit
import pycuda.driver as drv
import numpy as np

a = np.random.rand(4).astype(np.float32)
a_gpu = drv.mem_alloc(a.nbytes)
drv.memcpy_htod(a_gpu, a)

print("CUDA setup works!")
