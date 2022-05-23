# Shopify Intern Challenge 2022
## by: Ursula J'vlyn d'Ark

## Questions

### Question 1

(See included repo for program)
1. In order to get a more accurate picture of what the average order value was from this data set, I first took the median order value of all the orders. This was $284.00, which already seemed more reasonable.
2. Next, I took the simple mean (average) and median of each individual store's orders, which respectively came back as $3136.83 (mean, again seems very high) and $306.00 (median) which suggests something is still off with these values.
3. Finally, I took the IQR (Interquartile range) of the data, thus returning only the middle 50% of the data, which represents the more common values in the data set. This returned $293.71 (mean) and $280.00 (median), which both seem more reasonable and also backup the original median of all orders. Together, these values suggest that an average order value closer to $285.00 is more representative of the data.
4. Finally, I would note that based on what I'm seeing in the data and just using a basic sanity check, I wonder if perhaps a few orders had the decimal place in the wrong spot, thus adding two zeros to the order values. There are several orders at $704,000.00, which seems quite high for shoe orders. $7040.00 seems more likely, but this is just my guess.

### Question 2

1. How many orders were shipped by Speedy Express in total?
    1. 54
    2. Query: SELECT COUNT(OrderID) AS 'Orders shipped by Speedy Express' FROM Orders WHERE ShipperID IN (SELECT ShipperID FROM Shippers WHERE ShipperName='Speedy Express');

2. What is the last name of the employee with the most orders?
  1. Peacock
  2. Query: SELECT LastName FROM Employees WHERE EmployeeID IN (SELECT EmployeeID FROM Orders GROUP BY EmployeeID ORDER BY COUNT(OrderID) DESC LIMIT 1);

3. What product was ordered the most by customers in Germany?
  1. ProductID 40 - Boston Crab Meat, quantity: 140
  2. Query: SELECT ProductName FROM Products WHERE ProductID IN (SELECT ProductID FROM OrderDetails WHERE OrderID IN (SELECT OrderID FROM Orders Where CustomerID IN (SELECT CustomerID FROM ORDERS WHERE CustomerID IN (SELECT CustomerID FROM Customers WHERE Country='Germany'))) GROUP BY Quantity ORDER BY SUM(Quantity) DESC LIMIT 1);
