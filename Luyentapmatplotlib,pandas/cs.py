import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:\BT Python\Bài tập Python\Luyentapmatplotlib,pandas\sales-data-sample.csv', encoding='utf-8')

df['OrderDate'] = pd.to_datetime(df['OrderDate'])

df['Year'] = df['OrderDate'].dt.year
df['Month'] = df['OrderDate'].dt.month
df['Quarter'] = df['OrderDate'].dt.quarter

# 1. Vẽ biểu đồ doanh thu theo tháng (từ tháng 1 -> 12)
monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='bar', color='skyblue')
plt.title('Doanh thu theo tháng')
plt.xlabel('Tháng')
plt.ylabel('Tổng Doanh thu')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('doanh_thu_theo_thang.png')
plt.close()

# 2. Vẽ biểu đồ doanh thu theo năm
yearly_sales = df.groupby('Year')['Sales'].sum()

plt.figure(figsize=(8, 5))
yearly_sales.plot(kind='bar', color='lightgreen')
plt.title('Doanh thu theo năm')
plt.xlabel('Năm')
plt.ylabel('Tổng Doanh thu')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('doanh_thu_theo_nam.png')
plt.close()

# 3. Vẽ biểu đồ doanh thu theo quý
quarterly_sales = df.groupby('Quarter')['Sales'].sum()

plt.figure(figsize=(8, 5))
quarterly_sales.plot(kind='bar', color='orange')
plt.title('Doanh thu theo quý')
plt.xlabel('Quý')
plt.ylabel('Tổng Doanh thu')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('doanh_thu_theo_quy.png')
plt.close()

# 4. Vẽ biểu đồ doanh thu theo các loại mặt hàng (Category)
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
category_sales.plot(kind='bar', color='purple')
plt.title('Doanh thu theo các loại mặt hàng')
plt.xlabel('Danh mục')
plt.ylabel('Tổng Doanh thu')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('doanh_thu_theo_mat_hang.png')
plt.close()