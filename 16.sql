/*AIM:Find the total number of customers from each country in the table
  (customer ID,customer name,country) using group by.*/
 Select country , count(distinct customer_ID) as number_of_customers
From customer
Group by country ;
