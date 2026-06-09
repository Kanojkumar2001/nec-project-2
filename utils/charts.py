import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from utils.helper_functions import prepare_chart_data

CHART_COLORS = px.colors.qualitative.Set2


def sales_trend_chart(df):

    chart_df = prepare_chart_data(df)

    daily_sales = (
        chart_df.groupby("order_date", as_index=False)["total_sales"]
        .sum()
        .sort_values("order_date")
    )

    fig = px.area(
        daily_sales,
        x="order_date",
        y="total_sales",
        title="Daily Sales Trend",
        labels={
            "order_date": "Date",
            "total_sales": "Revenue (₹)"
        },
        color_discrete_sequence=["#2563eb"]
    )

    fig.update_layout(
        hovermode="x unified",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    return fig


def product_sales_chart(df):

    product_df = (
        df.groupby("product_name", as_index=False)["total_sales"]
        .sum()
        .sort_values("total_sales", ascending=True)
    )

    fig = px.bar(
        product_df,
        x="total_sales",
        y="product_name",
        orientation="h",
        title="Revenue by Product",
        labels={
            "product_name": "Product",
            "total_sales": "Revenue (₹)"
        },
        color="total_sales",
        color_continuous_scale="Blues"
    )

    fig.update_layout(showlegend=False)

    return fig


def region_sales_chart(df):

    region_df = (
        df.groupby("region", as_index=False)["total_sales"]
        .sum()
        .sort_values("total_sales", ascending=False)
    )

    fig = px.pie(
        region_df,
        names="region",
        values="total_sales",
        title="Regional Revenue Share",
        hole=0.45,
        color_discrete_sequence=CHART_COLORS
    )

    return fig


def category_sales_chart(df):

    category_df = (
        df.groupby("category", as_index=False)["total_sales"]
        .sum()
    )

    fig = px.bar(
        category_df,
        x="category",
        y="total_sales",
        title="Sales by Category",
        labels={
            "category": "Category",
            "total_sales": "Revenue (₹)"
        },
        color="category",
        color_discrete_sequence=CHART_COLORS
    )

    fig.update_layout(showlegend=False)

    return fig


def monthly_sales_chart(df):

    chart_df = prepare_chart_data(df)

    chart_df["month"] = (
        chart_df["order_date"].dt.to_period("M").astype(str)
    )

    monthly_df = (
        chart_df.groupby("month", as_index=False)["total_sales"]
        .sum()
    )

    fig = px.bar(
        monthly_df,
        x="month",
        y="total_sales",
        title="Monthly Revenue",
        labels={
            "month": "Month",
            "total_sales": "Revenue (₹)"
        },
        color="total_sales",
        color_continuous_scale="Teal"
    )

    fig.update_layout(showlegend=False)

    return fig


def quantity_distribution_chart(df):

    fig = px.box(
        df,
        x="product_name",
        y="quantity",
        title="Quantity Distribution by Product",
        labels={
            "product_name": "Product",
            "quantity": "Units Sold"
        },
        color="product_name",
        color_discrete_sequence=CHART_COLORS
    )

    fig.update_layout(showlegend=False)

    return fig


def price_quantity_scatter(df):

    fig = px.scatter(
        df,
        x="quantity",
        y="unit_price",
        size="total_sales",
        color="region",
        hover_name="product_name",
        title="Price vs Quantity (bubble size = revenue)",
        labels={
            "quantity": "Quantity",
            "unit_price": "Unit Price (₹)",
            "region": "Region"
        },
        color_discrete_sequence=CHART_COLORS
    )

    return fig


def region_product_heatmap(df):

    pivot_df = (
        df.pivot_table(
            index="product_name",
            columns="region",
            values="total_sales",
            aggfunc="sum",
            fill_value=0
        )
    )

    fig = px.imshow(
        pivot_df,
        title="Product × Region Revenue Heatmap",
        labels={
            "x": "Region",
            "y": "Product",
            "color": "Revenue (₹)"
        },
        color_continuous_scale="Blues",
        aspect="auto"
    )

    return fig


def forecast_comparison_chart(actual, predicted):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            y=actual,
            mode="markers+lines",
            name="Actual Sales",
            line=dict(color="#2563eb", width=2),
            marker=dict(size=8)
        )
    )

    fig.add_trace(
        go.Scatter(
            y=predicted,
            mode="markers+lines",
            name="Predicted Sales",
            line=dict(color="#f59e0b", width=2, dash="dash"),
            marker=dict(size=8)
        )
    )

    fig.update_layout(
        title="Model: Actual vs Predicted Sales",
        xaxis_title="Test Sample Index",
        yaxis_title="Sales (₹)",
        hovermode="x unified",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    return fig


def forecast_timeline_chart(historical_df, forecast_df):

    hist = prepare_chart_data(historical_df)

    daily_hist = (
        hist.groupby("order_date", as_index=False)["total_sales"]
        .sum()
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=daily_hist["order_date"],
            y=daily_hist["total_sales"],
            mode="lines+markers",
            name="Historical Sales",
            line=dict(color="#2563eb", width=2)
        )
    )

    fig.add_trace(
        go.Scatter(
            x=forecast_df["forecast_date"],
            y=forecast_df["predicted_sales"],
            mode="lines+markers",
            name="Forecasted Sales",
            line=dict(color="#10b981", width=2, dash="dot")
        )
    )

    fig.update_layout(
        title="Sales Forecast Timeline",
        xaxis_title="Date",
        yaxis_title="Revenue (₹)",
        hovermode="x unified"
    )

    return fig


def inventory_gauge_chart(current_stock, reorder_point, recommended_stock):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number+delta",
            value=current_stock,
            delta={
                "reference": reorder_point,
                "relative": False,
                "valueformat": ",.0f"
            },
            title={"text": "Current Stock Level"},
            gauge={
                "axis": {"range": [0, max(recommended_stock * 1.2, current_stock + 1)]},
                "bar": {"color": "#2563eb"},
                "steps": [
                    {"range": [0, reorder_point], "color": "#fecaca"},
                    {
                        "range": [reorder_point, recommended_stock],
                        "color": "#fef08a"
                    },
                    {
                        "range": [recommended_stock, recommended_stock * 1.2],
                        "color": "#bbf7d0"
                    }
                ],
                "threshold": {
                    "line": {"color": "#dc2626", "width": 4},
                    "thickness": 0.8,
                    "value": reorder_point
                }
            }
        )
    )

    fig.update_layout(height=320)

    return fig


def sales_chart(df):

    return sales_trend_chart(df)
