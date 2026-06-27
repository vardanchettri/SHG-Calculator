# loan_manage_01.py

def calculate_ledger(principal, monthly_rate, collection_total):
    """
    SHG Loan Ledger logic.

    Demand side:
        Interest = Principal x (Monthly Rate / 100)
        Total    = Principal + Interest

    Collection side:
        Total     = collection_total (entered by user)
        Interest  = same interest as demand side (cleared first)
        Principal = Total - Interest

    Next Principal = Demand Principal - Collection Principal
    """

    # --- Demand Section ---
    interest = principal * (monthly_rate / 100)
    demand_total = principal + interest

    # --- Collection Section ---
    collection_interest = interest
    collection_principal = collection_total - collection_interest

    # --- Next Month's Opening Principal ---
    next_principal = principal - collection_principal

    demand_table = {
        "Principal": [f"{principal:.2f}"],
        "Interest": [f"{interest:.2f}"],
        "Total": [f"{demand_total:.2f}"],
    }

    collection_table = {
        "Principal": [f"{collection_principal:.2f}"],
        "Interest": [f"{collection_interest:.2f}"],
        "Total": [f"{collection_total:.2f}"],
    }

    return demand_table, collection_table, next_principal