import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#dọc data từ file 
data = pd.read_excel("D:\ds_salaries (1).xlsx")
print(data.head())
#Kiểm tra xem dữ liệu có bao nhiêu dòng và cột
print(data.shape)
#Phát hiện các giá trị còn thiếu.
print(pd.isna(data))

# Đọc dữ liệu từ file Excel
data = pd.read_excel(r"D:\ds_salaries (1).xlsx")

# Lọc ra các cột cần thiết
filtered_data = data[["work_year", "salary"]]
# Chuyển đổi các thuộc tính dạng chuỗi sang dạng số
filtered_data['work_year'] = pd.Categorical(data['work_year']).codes
filtered_data['salary'] = pd.Categorical(data['salary']).codes
# Tính toán môi tương quan giữa các cột
correlation_matrix = filtered_data.corr()

# Vẽ biểu đồ ma trận môi tương quan bằng treemap
plt.subplots(figsize=(15, 5))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Ma trận tương quan")
plt.show()

