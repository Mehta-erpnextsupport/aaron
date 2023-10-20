# import frappe

# from erpnext.accounts.utils import (
# 	get_balance_on
# )

# @frappe.whitelist()
# def get_outstanding_amount(company,date,party):
#     customer_outstanding_amount = get_balance_on(
# 	    party_type="Customer", party=party, date=date, company=company
# 				)
#     return customer_outstanding_amount


# def get_outstanding_amount_validation(self,method):
    # doc = frappe.db.get_value("Aaron Setting","Aaron Setting","apply_advance_payment_in_sales_invoice")
    # if doc:
#     if self.customer_outstanding_amount > 0:
#         frappe.throw("You are not eligible To Book Sales Invoice ")
    
#     if self.customer_outstanding_amount + self.net_total > 0:
#         frappe.throw("Your Amount is less Please Payment First")    
            