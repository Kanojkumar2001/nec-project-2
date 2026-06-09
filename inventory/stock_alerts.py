def generate_stock_alert(
    current_stock,
    reorder_point
):

    if current_stock <= reorder_point:

        return "⚠️ Low Stock Alert"

    return "✅ Stock Level Normal"