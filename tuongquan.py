import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Bước 1: Đọc dữ liệu từ tập tin "ds_salaries.csv"
data = pd.read_excel("D:\ds_salaries (1).xlsx")

# Bước 2: Khám phá dữ liệu
print(data.head())  # Xem 5 dòng đầu của dữ liệu
print(data.describe())  # Thống kê mô tả dữ liệu
#lấy 1000 hàng đầu tiên
data=data.iloc[1:1000]
# Bước 3: Chuẩn bị dữ liệu
# Chọn các thuộc tính cần sử dụng để xây dựng mô hình ước lượng
selected_features = ['experience_level']
target_variable = 'salary_in_usd'

# Chuyển đổi các thuộc tính dạng chuỗi sang dạng số
data['experience_level'] = pd.Categorical(data['experience_level']).codes


# Bước 4: Xây dựng mô hình ước lượng
# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X = data[selected_features]
y = data[target_variable]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Xây dựng mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X_train, y_train)

# Bước 5: Đánh giá mô hình
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# Bước 6: Sử dụng mô hình để ước lượng mức lương cho nhân viên mới
new_employee = pd.DataFrame({
    'experience_level': ['SE']
    
})
data['experience_level'] = data['experience_level'].astype('category')

# Chuyển đổi thuộc tính dạng chuỗi sang dạng số
new_employee['experience_level'] = pd.Categorical(new_employee['experience_level'], categories=data['experience_level'].cat.categories).codes

estimated_salary = model.predict(new_employee[selected_features])
print("Estimated Salary:", estimated_salary)


import matplotlib.pyplot as plt

# Vẽ biểu đồ dự đoán và thực tế
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('mức lương thực tế')
plt.ylabel('mức lương dự đoán')
plt.title('mức lương thưc tế so với dự đoán')
plt.show()
