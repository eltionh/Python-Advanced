def process_checkout_api(total_amount):
    tax = total_amount * 0.10
    final_total = total_amount + tax
    return {"tax": tax, "final": final_total}