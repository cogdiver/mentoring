import pandas as pd
df_temp = pd.DataFrame({f"col_{i+1}": [j*i for j in range(20)] for i in range(10)})
# print(df_temp)
