USE db_project;

#List all the customers
SELECT * FROM Customer;
SELECT * FROM delivery;
#display all of the drivers that are available
SELECT name, vehicle, rating, phone_number FROM Drivers
WHERE availability = TRUE;

#get restaurant id from the restaurant name
SELECT m.item_name, m.description, m.price
FROM Menu m
JOIN Restaurants r ON m.restaurant_id = r.restaurant_id
WHERE r.name = 'Good Eats';  -- Replace 'Restaurant Name' with the actual name of the restaurant

SELECT * FROM orders;
#INSERT INTO Customer (name, email, password, phone_number, birthday, address, payment)
#VALUES ('Collin Meeker', 'collinmeeker@example.com', 'collin_password', '609-111-1111', '2001-03-12', '123 This Street', 'Credit Card');

#need better  way tp update order number
#INSERT INTO Orders (restaurant_id, customer_id, order_number, order_date, total_price, status)
#VALUES (1, 2, 'ORDER023', '2023-04-23', 50.00, 'pending');

# START TRANSACTION;
#INSERT INTO Orders (restaurant_id, customer_id, order_number, order_date, total_price, status)
#VALUES (1, 1, 'ORD001', CURDATE(), 50.00, 'pending');
#INSERT INTO Delivery (order_id, driver_id, restaurant_id, delivery_address, driver_tip, delivery_time)
#VALUES (LAST_INSERT_ID(), 2, 1, '123 Customer St.', 5.00, '18:00:00');
#COMMIT;

SELECT * FROM Orders;

 SELECT m.item_name, m.description, m.price
    FROM Menu m
    JOIN Restaurants r ON m.restaurant_id = r.restaurant_id
    WHERE r.name = 'Good Eats';