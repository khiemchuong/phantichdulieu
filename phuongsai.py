import pandas as pd
import numpy as np
import statistics
# Đọc dữ liệu từ file CSV
data = pd.read_csv("D:\ds_salaries (1).csv")

# Lấy cột dữ liệu cần tính phương sai
column_data = data['salary']

# Chuyển đổi dữ liệu thành mảng numpy
array_data = np.array(column_data)

# Tính phương sai
column_data1=statistics.mean(column_data)
phuongsai1=np.var(array_data, ddof=1)
phuongsai = np.var(array_data,ddof=0)


print("giá trị trung bình:",column_data1)
print('phương sai mẫu:',phuongsai1)
print("phương sai tồng thể :", phuongsai)
