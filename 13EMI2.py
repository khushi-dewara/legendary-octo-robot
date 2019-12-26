import numpy as np

 

interestRate        = 0.07

numberOfMonths      = 25*12;

principalBorrowed   = 3500000

 

principal2Pay   = np.ppmt(interestRate/12, 1, numberOfMonths, principalBorrowed);

interest2Pay    = np.ipmt(interestRate/12, 1, numberOfMonths, principalBorrowed);

 

print("Loan amount:%7.2f"%principalBorrowed);

print("Loan duration in months:%d"%numberOfMonths);

print("Annual Interest Rate in percent:%2.2f"%(interestRate*100));

 

print("Principal to be paid:%5.2f"%abs(principal2Pay));

print("Interest to be paid:%5.2f"%abs(interest2Pay));

print("Principal+Interest, to be paid:%5.2f"%abs(principal2Pay+interest2Pay));
