import frappe

def execute():
    allowed_currencies = ["ZAR", "USD"]
    
    # Get all currencies except allowed ones
    currencies = frappe.get_all("Currency", filters={"enabled": 1}, pluck="name")
    
    # Find currencies to disable
    currencies_to_disable = [c for c in currencies if c not in allowed_currencies]

    if not currencies_to_disable:
        frappe.logger().info("No additional currencies found to disable.")
        return

    # Disable currencies
    for currency in currencies_to_disable:
        frappe.db.set_value("Currency", currency, "enabled", 0)
        frappe.logger().info(f"Disabled currency: {currency}")

    frappe.db.commit()  
