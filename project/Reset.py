# DOn't Run this file , This will clear all the data you have

import numpy as np


do = int(input("1.clear data    , 2. history   :"))

if do == 1:

    a = np.array(["Name:", "DOB:"])
    np.save("data",a)
    
else:
    data = np.load("data.npy")
    print(data)
    