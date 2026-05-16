def process_checkout_api(total_amount):

    tax = total_amount * 0.05
    final_total = total_amount + tax
    return {"subtotal": total_amount, "tax": tax, "final": final_total}