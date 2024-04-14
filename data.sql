INSERT INTO Customer (name, email, phone_number, password, birthday, address, payment) VALUES
('John Doe', 'johndoe@example.com', '123-456-7890', 'hashed_password', '1985-10-12', '1234 Elm St, Yourtown', 'Credit Card'),
('Jane Smith', 'janesmith@example.com', '987-654-3210', 'another_password', '1990-07-23', '5678 Maple St, Othertown', 'PayPal');

INSERT INTO Drivers (name, vehicle, rating, availability, phone_number) VALUES
('Alice Johnson', 'Toyota Prius', 4.5, TRUE, '321-456-9870'),
('Bob Smith', 'Honda Civic', 3.6, TRUE, '123-456-7890'),
('Emma Davis', 'Ford Mustang', 4.5, FALSE, '987-654-3210'),
('Michael Brown', 'Chevrolet Tahoe', 4.3, TRUE, '555-123-4567'),
('Sophia Martinez', 'Tesla Model S', 5, TRUE, '888-222-3333'),
('Ethan Wilson', 'Jeep Wrangler', 4.7, TRUE, '444-555-6666'),
('Olivia Anderson', 'Subaru Outback', 4.5, FALSE, '777-888-9999'),
('Liam Thompson', 'BMW X5', 4.5, TRUE, '111-222-3333'),
('Ava White', 'Audi Q7', 4.3, TRUE, '333-444-5555'),
('Noah Harris', 'Lexus RX', 4.6, TRUE, '666-777-8888'),
('Isabella Wilson', 'Hyundai Sonata', 4.0, TRUE, '999-888-7777'),
('James Garcia', 'Kia Sportage', 4.0, FALSE, '777-666-5555'),
('Mia Rodriguez', 'Nissan Altima', 4.3, TRUE, '111-333-5555'),
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
(1, 3, 5, 'Excellent service, very polite driver!', '2023-05-12'),
(1, 7, 4, 'Fast delivery, but could improve on communication.', '2023-06-25'),
(1, 2, 4, 'Good experience overall, would use again.', '2023-07-18'),
(1, 6, 5, 'Amazing driver, arrived early and very friendly.', '2023-08-09'),

(2, 4, 4, 'Driver was polite and professional.', '2023-05-12'),
(2, 8, 3, 'Delivery was slightly delayed, but driver was apologetic.', '2023-06-25'),
(2, 6, 3, 'Average service, nothing exceptional.', '2023-07-18'),
(2, 2, 4, 'Good communication, arrived on time.', '2023-08-09'),
(2, 1, 3, 'Could improve on navigation skills.', '2023-09-21'),
(2, 9, 4, 'Pleasant experience overall.', '2023-10-14'),
(2, 5, 4, 'Driver was friendly and helpful.', '2023-11-27'),

(3, 4, 5, 'Driver was polite and professional.', '2023-05-12'),
(3, 8, 4, 'Delivery was slightly delayed, but driver was apologetic.', '2023-06-25'),

(4, 4, 5, 'Driver was polite and professional.', '2023-05-12'),
(4, 8, 5, 'Delivery was slightly delayed, but driver was apologetic.', '2023-06-25'),
(4, 6, 3, 'Average service, nothing exceptional.', '2023-07-18'),
(4, 2, 5, 'Good communication, arrived on time.', '2023-08-09'),
(4, 1, 3, 'Could improve on navigation skills.', '2023-09-21'),
(4, 9, 5, 'Pleasant experience overall.', '2023-10-14'),

(5, 7, 5, 'Excellent service, highly recommended!', '2023-05-12'),

(6, 4, 5, 'Driver was polite and professional.', '2023-05-12'),
(6, 8, 5, 'Delivery was slightly delayed, but driver was apologetic.', '2023-06-25'),
(6, 6, 5, 'Average service, nothing exceptional.', '2023-07-18'),
(6, 2, 5, 'Good communication, arrived on time.', '2023-08-09'),
(6, 1, 4, 'Could improve on navigation skills.', '2023-09-21'),
(6, 9, 4, 'Pleasant experience overall.', '2023-10-14'),

(7, 3, 5, 'Driver was polite and professional.', '2023-05-12'),
(7, 8, 4, 'Delivery was slightly delayed, but driver was apologetic.', '2023-06-25'),
(7, 6, 3, 'Average service, nothing exceptional.', '2023-07-18'),
(7, 2, 5, 'Good communication, arrived on time.', '2023-08-09'),

(8, 4, 5, 'Driver was polite and professional.', '2023-05-12'),
(8, 8, 5, 'Delivery was slightly delayed, but driver was apologetic.', '2023-06-25'),
(8, 6, 4, 'Average service, nothing exceptional.', '2023-07-18'),
(8, 2, 4, 'Good communication, arrived on time.', '2023-08-09'),

(9, 4, 5, 'Driver was polite and professional.', '2023-05-12'),
(9, 8, 5, 'Delivery was slightly delayed, but driver was apologetic.', '2023-06-25'),
(9, 6, 4, 'Average service, nothing exceptional.', '2023-07-18'),
(9, 2, 4, 'Good communication, arrived on time.', '2023-08-09'),
(9, 1, 4, 'Could improve on navigation skills.', '2023-09-21'),
(9, 9, 4, 'Pleasant experience overall.', '2023-10-14'),
(9, 5, 4, 'Driver was friendly and helpful.', '2023-11-27'),
(9, 3, 4, 'Great service, would use again.', '2023-12-30'),

(10, 2, 5, 'Very polite and professional.', '2023-05-12'),
(10, 8, 5, 'Excellent service, couldn\'t be happier!', '2023-06-25'),
(10, 4, 5, 'Arrived early, very helpful.', '2023-07-18'),
(10, 6, 4, 'Service was good overall, but room for improvement.', '2023-08-09'),
(10, 1, 4, 'Driver was friendly, but navigation could be better.', '2023-09-21'),

(11, 3, 4, 'Polite driver, but delivery was slightly late.', '2023-05-12'),
(11, 7, 5, 'Excellent service, driver was very friendly.', '2023-06-25'),
(11, 5, 4, 'Good experience overall, could improve on punctuality.', '2023-07-18'),
(11, 2, 3, 'Service was okay, but room for improvement.', '2023-08-09'),
(11, 8, 4, 'Driver was professional, but navigation was a bit off.', '2023-09-21'),
(11, 1, 5, 'Couldn\'t be happier with the service, driver was great!', '2023-10-14'),
(11, 9, 3, 'Service was average, nothing exceptional.', '2023-11-27'),
(11, 4, 4, 'Arrived on time, but could have been more polite.', '2023-12-30'),
(11, 6, 4, 'Good communication, driver was helpful.', '2024-01-15'),
(11, 10, 4, 'Driver was friendly, but service was a bit slow.', '2024-02-28'),

(12, 5, 4, 'Service was good overall, but could be improved.', '2023-05-12'),

(13, 2, 5, 'Excellent service, very professional!', '2023-05-12'),
(13, 8, 5, 'Driver was fantastic, highly recommend!', '2023-06-25'),
(13, 4, 4, 'Good experience overall, could be improved.', '2023-07-18'),
(13, 6, 4, 'Driver was polite, but service was slightly late.', '2023-08-09'),
(13, 1, 4, 'Service was good, but could be faster.', '2023-09-21'),
(13, 9, 4, 'Arrived on time, overall satisfied.', '2023-10-14'),
(13, 3, 4, 'Great experience, would use again!', '2023-11-27'),

(14, 2, 5, 'Fantastic service, highly recommended!', '2023-05-12'),
(14, 8, 5, 'Driver was exceptional, very satisfied.', '2023-06-25'),
(14, 4, 5, 'Excellent experience, couldn\'t be happier.', '2023-07-18'),
(14, 6, 5, 'Outstanding service, exceeded expectations.', '2023-08-09'),
(14, 1, 5, 'Great service, arrived on time.', '2023-09-21'),
(14, 9, 5, 'Amazing driver, very friendly and helpful.', '2023-10-14'),
(14, 3, 5, 'Superb service, will definitely use again.', '2023-11-27'),
(14, 7, 5, 'Driver was excellent, everything went smoothly.', '2023-12-30'),
(14, 5, 5, 'Top-notch service, couldn\'t ask for better.', '2024-01-15'),
(14, 10, 5, 'Absolutely fantastic, best driver ever!', '2024-02-28'),
(14, 2, 4, 'Service was good, but slight delay in arrival.', '2024-03-15'),
(14, 8, 4, 'Driver was polite, but took a longer route.', '2024-04-01'),
(14, 4, 4, 'Good service, could improve on punctuality.', '2024-04-18');





