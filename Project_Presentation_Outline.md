# FreshMart — Project Presentation Outline

**Retail Sales Dashboard Using CSV and Matplotlib**  
Individual Python Mini Project  
Presented by: Harshit More  
B.Tech — Computer Science and Engineering, Jain University

## Slide 1 — Title
FreshMart: Retail Sales Dashboard Using CSV and Matplotlib. Individual Python Mini Project by Harshit More, Jain University.

## Slide 2 — Project Overview
FreshMart is a fictional supermarket used as the project case study. The system analyses transaction records stored in a CSV file. Python processes the data and Matplotlib displays the results. The goal is to convert raw sales records into clear business insights.

## Slide 3 — Problem Statement
Retail stores generate many sales records. Manual calculations make it difficult to compare categories and trends. A simple dashboard can summarize sales performance quickly. This project automates basic sales analysis using Python.

## Slide 4 — Objectives
- Read and validate CSV sales data.
- Calculate revenue, orders, units sold and average order value.
- Find category-wise sales and top-selling products.
- Visualize monthly trends and payment-mode distribution.
- Save the dashboard and summary files.

## Slide 5 — Tools and Technologies
- Python — core programming language
- Pandas — reading, cleaning and grouping CSV data
- Matplotlib — charts and dashboard layout
- CSV — simple data storage format

## Slide 6 — Dataset Structure
The dataset contains 150 fictional transaction records from January–October 2026. Fields: Order_ID, Date, Product, Category, Quantity, Unit_Price, Discount_Percent, Total_Sales and Payment_Mode. Categories include Groceries, Dairy, Personal Care, Snacks and Beverages.

## Slide 7 — System Workflow
1. Load CSV file using Pandas.
2. Validate columns and convert data types.
3. Calculate KPIs and grouped summaries.
4. Create charts using Matplotlib.
5. Save dashboard PNG and summary CSV files.

## Slide 8 — Dashboard Visualizations
- KPI cards: total revenue, orders, units sold and average order value.
- Bar chart: revenue by product category.
- Line chart: monthly sales trend.
- Horizontal bar chart: top products by units sold.
- Pie chart: sales share by payment mode.

## Slide 9 — Working Model and Execution
Install dependencies using `pip install pandas matplotlib`. Keep `retail_dashboard.py` and `freshmart_sales.csv` in the same folder. Run `python retail_dashboard.py`. The program prints a summary, opens the dashboard and saves generated files in the output folder.

## Slide 10 — Benefits and Future Scope
The project is simple, low-cost and easy to customize. It makes sales comparisons easier to understand and can be adapted to real store transaction data. Future scope includes filters, a GUI, a live database, profit analysis and inventory analysis.

## Slide 11 — Conclusion
The project transforms CSV sales records into useful summaries and charts. Pandas handles data processing and Matplotlib provides visualization. FreshMart demonstrates a practical beginner-level retail analytics solution.

## Slide 12 — Thank You
Questions? FreshMart — Retail Sales Dashboard. Harshit More.
