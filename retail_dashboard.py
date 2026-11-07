"""
FRESHMART - Retail Sales Dashboard
Run: python retail_dashboard.py
Dependencies: pandas, matplotlib
Install: pip install pandas matplotlib
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "freshmart_sales.csv"
OUTPUT_DIR = "output"


def load_data(path=DATA_FILE):
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Could not find {path}. Keep the CSV in the same folder as this script."
        )
    data = pd.read_csv(path)
    required = {"Order_ID", "Date", "Product", "Category", "Quantity",
                "Unit_Price", "Discount_Percent", "Total_Sales", "Payment_Mode"}
    missing = required.difference(data.columns)
    if missing:
        raise ValueError(f"CSV is missing columns: {', '.join(sorted(missing))}")
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["Total_Sales"] = pd.to_numeric(data["Total_Sales"], errors="coerce")
    data["Quantity"] = pd.to_numeric(data["Quantity"], errors="coerce")
    data = data.dropna(subset=["Date", "Total_Sales", "Quantity"])
    return data


def print_summary(data):
    revenue = data["Total_Sales"].sum()
    orders = data["Order_ID"].nunique()
    units = data["Quantity"].sum()
    average = revenue / orders if orders else 0
    print("\n" + "=" * 48)
    print("       FRESHMART - RETAIL SALES SUMMARY")
    print("=" * 48)
    print(f"Total revenue       : Rs. {revenue:,.2f}")
    print(f"Number of orders    : {orders}")
    print(f"Units sold          : {units:,.0f}")
    print(f"Average order value : Rs. {average:,.2f}")
    print("\nSales by category:")
    print(data.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False).to_string())
    print("\nTop 5 products:")
    print(data.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(5).to_string())
    print("=" * 48)


def create_dashboard(data):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    revenue = data["Total_Sales"].sum()
    orders = data["Order_ID"].nunique()
    units = data["Quantity"].sum()
    avg_order = revenue / orders if orders else 0

    category_sales = data.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)
    monthly_sales = data.set_index("Date").resample("ME")["Total_Sales"].sum()
    top_products = data.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(7)
    payment_sales = data.groupby("Payment_Mode")["Total_Sales"].sum()

    fig = plt.figure(figsize=(15, 9))
    fig.suptitle("FRESHMART | RETAIL SALES DASHBOARD", fontsize=20, fontweight="bold")
    fig.text(0.5, 0.93, "Sales performance overview", ha="center", fontsize=11, color="gray")

    kpis = [
        ("TOTAL REVENUE", f"Rs. {revenue:,.0f}"),
        ("TOTAL ORDERS", f"{orders:,}"),
        ("UNITS SOLD", f"{units:,.0f}"),
        ("AVG. ORDER VALUE", f"Rs. {avg_order:,.0f}")
    ]
    for i, (label, value) in enumerate(kpis):
        ax = fig.add_axes([0.055 + i * 0.235, 0.78, 0.205, 0.105])
        ax.set_facecolor("#eaf2f8")
        ax.text(0.5, 0.68, label, ha="center", va="center", fontsize=9, color="#34495e")
        ax.text(0.5, 0.28, value, ha="center", va="center", fontsize=15,
                fontweight="bold", color="#154360")
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)

    ax1 = fig.add_axes([0.08, 0.43, 0.38, 0.27])
    category_sales.plot(kind="bar", ax=ax1, color="#3498db")
    ax1.set_title("Revenue by Category")
    ax1.set_ylabel("Sales (Rs.)")
    ax1.tick_params(axis="x", rotation=25)
    ax1.grid(axis="y", alpha=0.25)

    ax2 = fig.add_axes([0.56, 0.43, 0.36, 0.27])
    monthly_sales.plot(kind="line", marker="o", linewidth=2, ax=ax2, color="#e67e22")
    ax2.set_title("Monthly Sales Trend")
    ax2.set_ylabel("Sales (Rs.)")
    ax2.grid(alpha=0.25)
    ax2.tick_params(axis="x", rotation=30)

    ax3 = fig.add_axes([0.08, 0.10, 0.38, 0.24])
    top_products.sort_values().plot(kind="barh", ax=ax3, color="#27ae60")
    ax3.set_title("Top Products by Units Sold")
    ax3.set_xlabel("Quantity")
    ax3.grid(axis="x", alpha=0.25)

    ax4 = fig.add_axes([0.60, 0.12, 0.27, 0.22])
    ax4.pie(payment_sales, labels=payment_sales.index, autopct="%1.1f%%",
            startangle=90, wedgeprops={"edgecolor": "white"})
    ax4.set_title("Sales by Payment Mode")

    fig.savefig(os.path.join(OUTPUT_DIR, "freshmart_dashboard.png"),
                dpi=180, bbox_inches="tight")
    plt.show()
    plt.close(fig)

    category_sales.rename("Total_Sales").to_csv(
        os.path.join(OUTPUT_DIR, "category_sales_summary.csv")
    )
    monthly_sales.rename("Total_Sales").to_csv(
        os.path.join(OUTPUT_DIR, "monthly_sales_summary.csv")
    )
    print(f"\nDashboard saved to {OUTPUT_DIR}/freshmart_dashboard.png")


def main():
    try:
        data = load_data()
        if data.empty:
            raise ValueError("No valid sales records were found in the CSV file.")
        print_summary(data)
        create_dashboard(data)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
