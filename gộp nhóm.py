import pandas as pd

ch = pd.read_csv(r"D:\ds_salaries (1).csv")

# Gộp nhóm dữ liệu theo cột 'employment_type'
def gop_nhom(ch):
    chuong = ch.groupby('employment_type').sum()
    print(chuong)
    return chuong

# Gộp nhóm có cùng thuộc tính 'job_title' là 'Data Scientist'
def gop_nhom_theo_thuoc_tinh(ch):
    chuong1 = ch[ch['job_title'] == 'Data Scientist'].groupby('job_title').sum()
    print(chuong1)
    return chuong1

gop_nhom(ch)
gop_nhom_theo_thuoc_tinh(ch)

