import numpy as np
import pandas as pd

# some random data frames
df1 = pd.DataFrame(dict(x=np.random.randn(100), y=np.random.randint(0, 5, 100)))
df2 = pd.DataFrame(dict(x=np.random.randn(100), y=np.random.randint(0, 5, 100)))

print(df1)
print(df2)

# concatenate them
df_concat = pd.concat((df1, df2))
print(df_concat)

print(df_concat.mean())
# x   -0.163044
# y    2.120000
# dtype: float64

print(df_concat.median())
# x   -0.192037
# y    2.000000
# dtype: float64
#

by_row_index = df_concat.groupby(df_concat.index)
print(by_row_index)
df_means = by_row_index.mean()

print(df_means.head())
print(df_means.tail())
#           x    y
# 0 -0.850794  1.5
# 1  0.159038  1.5
# 2  0.083278  1.0
# 3 -0.540336  0.5
# 4  0.390954  3.5
