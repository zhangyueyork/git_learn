#!/usr/bin/env python3.7
#
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#plt.style.use(["classic", "myself"])
print("-"*10,"import end","-"*10)
########
lst = [
        [1,2,3,4],
        [4,5,6,7],
        [7,8,9,10]
        ]
df1 = pd.DataFrame(lst, index=[1,2,3], columns=list('ABCD'))
