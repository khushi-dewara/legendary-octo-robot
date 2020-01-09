#AIM:Compute EMIs for a loan using the numpy or scipy libraries.
import numpy as np
# assume annual interest of 7.5%
def calc_interest(interest ,years , loan_value ):
   annual_rate = interest/100.0
   monthly_rate = annual_rate/12
   number_month = years * 12
   monthly_pay = abs(np.pmt(monthly_rate, number_month, loan_value))
   sf1 = "Paying off a loan of ${:,} over {} years at"
   sf2 = "{}% interest, your monthly payment will be ₹{:,.2f}"
   print(sf1.format(loan_value, years))
   print(sf2.format(interest, monthly_pay))
