INSERT INTO Customer (name, email, phone_number, password, birthday, address, payment) VALUES
('John Doe', 'johndoe@example.com', '123-456-7890', 'hashed_password', '1985-10-12', '1234 Elm St, Yourtown', 'Credit Card'),
('Jane Smith', 'janesmith@example.com', '987-654-3210', 'another_password', '1990-07-23', '5678 Maple St, Othertown', 'PayPal');

INSERT INTO Drivers (name, vehicle, rating, availability, phone_number) VALUES
('Alice Johnson', 'Toyota Prius', 4.5, TRUE, '321-456-9870'),
('Bob Lee', 'Honda Civic', 4.7, FALSE, '654-321-4567');

INSERT INTO Restaurants (name, address) VALUES
('Good Eats', '123 Food Lane'),
('Tasty Treats', '456 Snack Blvd'),
('Bob\'s Burgers', '459 Ocean Ave'),
('Walt\'s Candy Shop', '308 Negra Arroyo Ln'),
('Los Pollos Hermanos', '4590 Bell Ave'),
('Shaq Shack', '1010 BBQ Chicken Rd'),
('MacLaren\'s Pub', '103 Heart Ave'),
('JJ\'s Diner', '6031 Libertarian Rd'),
('Paunch Burger', '501 America Ave'),
('Krusty Krab', '406 Bikini Bottom Rd');

INSERT INTO Orders (restaurant_id, customer_id, order_number, order_date, total_price, status) VALUES
(1, 1, 'ORDER001', '2023-04-01', 19.99, 'delivered'),
(2, 2, 'ORDER002', '2023-04-02', 29.99, 'pending');

INSERT INTO Menu (restaurant_id, item_name, description, price) VALUES
(1, 'Burger', 'A classic burger with cheese', 9.99),
(2, 'Pizza', 'Large pepperoni pizza', 12.99);

INSERT INTO Pickup (order_id, pickup_time) VALUES
(1, '12:00:00'),
(2, '12:30:00');

INSERT INTO Delivery (order_id, driver_id, restaurant_id, delivery_address, driver_tip, delivery_time) VALUES
(1, 1, 1, '1234 Elm St, Yourtown', 3.00, '12:45:00'),
(2, 2, 2, '5678 Maple St, Othertown', 5.00, '13:15:00');

INSERT INTO Reviews (driver_id, customer_id, rating, comments, review_date) VALUES
(1, 1, 5, 'Great and timely delivery!', '2023-04-01'),
(2, 2, 4, 'Good service, but a bit late.', '2023-04-02');





