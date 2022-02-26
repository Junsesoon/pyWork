# Data Loading, Storage

# 환경설정
all = [var for var in globals() if var[0] != "_"]
for var in all:
    del globals()[var]

import numpy as np
import pandas as pd
np.random.seed(12345)
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4,suppress=True)


# 예시
df = pd.read_csv('ex1.csv')
df

# 구분자를 쉼표로 지정
pd.read_table('ex1.csv', sep = ',')

# type examples/ex2.csv
pd.read_csv('ex2.csv', header=None)

# 컬럼명 지정
pd.read_CSV=