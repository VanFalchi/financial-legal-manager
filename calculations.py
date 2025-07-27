# calculations.py
# NOTE: The specific percentage values in this file have been anonymized 
# to protect client confidentiality. The core logic remains the same.

def calculate_division(action_type, gross_amount, value_type, has_consultant=False):
    """
    Calculates the division of values and returns a dictionary with pure numbers.
    The logic is now strict and only calculates valid combinations.
    """
    shares = {
        'client': 0.0,
        'FinanceManager': 0.0,
        'partner': 0.0,
        'consultant': 0.0
    }

    # --- Rule for Monthly Social Security Installment (always priority) ---
    if (action_type.startswith("Social Security") or action_type == "Administrative Social Security") and value_type == "Monthly Installment":
        shares['client'] = 0.0
        shares['FinanceManager'] = gross_amount / 2
        shares['partner'] = gross_amount / 2
        if has_consultant:
            commission = gross_amount * 0.1
            shares['consultant'] = commission
            shares['FinanceManager'] -= commission
        return shares

    # --- Fee Rules (30%) ---
    # Only calculates if the combination of action type and value type is valid.
    elif (action_type in ["Civil", "Labor"] and value_type in ["Provided Amount", "Remaining Amount"]) or \
         (action_type == "Social Security RPV/Court Order" and value_type in ["RPV", "Court Order", "Remaining Amount"]):
        
        total_fees = gross_amount * 0.25
        shares['client'] = gross_amount - total_fees
        shares['FinanceManager'] = total_fees / 2
        shares['partner'] = total_fees / 2

        # Consultant commission only applies to the main amount
        if has_consultant and value_type in ["Provided Amount", "RPV", "Court Order"]:
            commission = gross_amount * 0.1
            shares['consultant'] = commission
            shares['FinanceManager'] -= commission
        return shares

    # --- Procedural Costs Rules (50/50) ---
    # Does not apply to Administrative actions
    elif value_type == "Procedural Costs" and action_type != "Administrative Social Security":
        shares['client'] = 0.0
        shares['FinanceManager'] = gross_amount / 2
        shares['partner'] = gross_amount / 2
        return shares

    # If no rule applies, return zero values (safety behavior)
    return shares