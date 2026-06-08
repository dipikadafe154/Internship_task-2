import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
data = pd.read_csv("sales_data.csv")

print("\nSales Trend Visualization")
print("-" * 30)

# Total Sales
total_sales = data["Sales"].sum()
print("Total Sales:", total_sales)

# Average Sales
average_sales = data["Sales"].mean()
print("Average Sales:", round(average_sales, 2))

# Product-wise sales
sales_by_product = data.groupby("Product")["Sales"].sum()

print("\nProduct-wise Sales:")
print(sales_by_product)

# Best Selling Product
best_product = sales_by_product.idxmax()
best_sales = sales_by_product.max()

print("\nBest Selling Product:")
print(f"{best_product} : {best_sales}")

# Create 2 charts in one window
plt.figure(figsize=(12,5))

# Bar Chart
plt.subplot(1,2,1)
sales_by_product.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")

# Pie Chart
plt.subplot(1,2,2)
plt.pie(
    sales_by_product,
    labels=sales_by_product.index,
    autopct="%1.1f%%"
)
plt.title("Sales Distribution")

plt.tight_layout()
plt.show()