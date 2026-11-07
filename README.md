# FreshMart — Retail Sales Dashboard

**Individual Python mini project**  
**Presented by:** Harshit More  
**Programme:** B.Tech, Computer Science and Engineering — Jain University

## Project overview
FreshMart is a fictional supermarket case study. This project analyses transaction records stored in a CSV file with Python, Pandas and Matplotlib, turning raw sales records into business summaries and visualizations.

## Features
- Validates the required CSV columns and converts date/numeric fields.
- Calculates total revenue, number of orders, units sold and average order value.
- Summarizes revenue by category and identifies top products by units sold.
- Visualizes category revenue, monthly sales trend, top products and payment-mode share.
- Saves a dashboard image and category/monthly summary CSV files in the `output/` folder.

## Requirements
- Python 3.9 or later
- pandas
- matplotlib

## Installation
Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

## Run the working model
Keep `retail_dashboard.py` and `freshmart_sales.csv` in the same folder, then run:

```bash
python retail_dashboard.py
```

The program prints a sales summary, opens the Matplotlib dashboard, and saves generated files in `output/`.

## Dataset
`freshmart_sales.csv` contains 150 fictional transactions dated January–October 2026. Fields: `Order_ID`, `Date`, `Product`, `Category`, `Quantity`, `Unit_Price`, `Discount_Percent`, `Total_Sales`, and `Payment_Mode`.

All records are fictional and provided for educational demonstration.

## Repository files
- `retail_dashboard.py` — main Python program
- `freshmart_sales.csv` — input dataset
- `requirements.txt` — Python dependencies
- `Project_Presentation.pptx` — project presentation slides
- `output/` — generated dashboard and summary files (created on first run)

## Customizing
Replace the sample rows in `freshmart_sales.csv` with your own store data while keeping the column names unchanged. `Total_Sales` should contain the final transaction value after discount.
