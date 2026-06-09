from inventory.reorder_calculator import calculate_reorder_point
from inventory.safety_stock import calculate_safety_stock

def optimize_inventory(
    current_stock,
    average_daily_sales,
    lead_time
):

    reorder_point = calculate_reorder_point(
        average_daily_sales,
        lead_time
    )

    safety_stock = calculate_safety_stock(
        average_daily_sales,
        lead_time
    )

    recommended_stock = (
        reorder_point +
        safety_stock
    )

    status = (
        "Reorder Required"
        if current_stock < reorder_point
        else "Safe"
    )

    return {

        "reorder_point": reorder_point,

        "safety_stock": safety_stock,

        "recommended_stock": recommended_stock,

        "status": status
    }