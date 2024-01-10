import matplotlib.pyplot as plt
import pandas as pd

# Read the dataset
df = pd.read_csv('Sample - Superstore.csv', encoding='ISO-8859-1')

# Create a 3x2 subplot grid
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 10))

# Plot 1: Total Sales per Category
category_sales = df.groupby('Category')['Sales'].sum()
category_sales.plot(kind='bar', color='skyblue', ax=axes[0, 0])
axes[0, 0].set_title('Total Sales per Category',fontweight='bold')
axes[0, 0].set_xlabel('Category')
axes[0, 0].set_ylabel('Total Sales')

# Plot 2: Total Profit per Sub-Category
subcategory_profit = df.groupby('Sub-Category')['Profit'].sum().nlargest(5)
subcategory_profit.plot(kind='bar', color='lightgreen', ax=axes[0, 1])
axes[0, 1].set_title('Total Profit per Sub-Category',fontweight='bold')
axes[0, 1].set_xlabel('Sub-Category')
axes[0, 1].set_ylabel('Total Profit')

# Plot 3: Total Quantity Sold per Region
region_quantity = df.groupby('Region')['Quantity'].sum()
region_quantity.plot(kind='bar', color='orange', ax=axes[1, 0])
axes[1, 0].set_title('Total Quantity Sold per Region',fontweight='bold')
axes[1, 0].set_xlabel('Region')
axes[1, 0].set_ylabel('Total Quantity Sold')

# Plot 4: Sales Distribution by Customer Segment (Pie Chart)
segment_sales = df.groupby('Segment')['Sales'].sum()
axes[1, 1].pie(segment_sales, labels=segment_sales.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'lightcoral'])
axes[1, 1].set_title('Sales Distribution by Customer Segment',fontweight='bold')

# Hide the empty subplot in the last row and second column
axes[1, 1].axis('off')
axes[2, 0].axis('off')
axes[2, 1].axis('off')

text = "1. Technology ranks the highest sales category\n" \
       "2. Copiers has the highest profits\n" \
       "3. West region sold the highest quantity of products\n" \
       "4. Consumer customer segment has the highest sales."

# Add a grid for text information
axes[2, 0].text(0.5, 0.5, text, ha='center', va='center', fontsize=15, color='black')

text = "Student Name : Manasa Golla\n" \
       "Student Id : 22101213"

# Add a grid for text information
axes[2, 1].text(0.5, 0.5, text, ha='center', va='center', fontsize=15, color='black',fontweight='bold')

# Add a main title
plt.suptitle('Superstore Sales and Profit Analysis Dashboard', fontsize=20, fontweight='bold')

# Adjust layout for better spacing
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.savefig('22101213.png',dpi=300)

# Show the dashboard
plt.show()
