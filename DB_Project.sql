CREATE DATABASE `DB_Project` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

CREATE TABLE Customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    password VARCHAR(255) NOT NULL,
    birthday DATE,
    address TEXT,
    payment VARCHAR(255)
);

CREATE TABLE Drivers (
    driver_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    vehicle VARCHAR(255) NOT NULL,
    rating DECIMAL(3,2),
    availability BOOLEAN,
    phone_number VARCHAR(20)
);


CREATE TABLE Restaurants (
    restaurant_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL
);

CREATE TABLE Menu (
    menu_id INT AUTO_INCREMENT,
    restaurant_id INT NOT NULL,
    item_name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2),
    PRIMARY KEY (menu_id, restaurant_id),
    FOREIGN KEY (restaurant_id) REFERENCES Restaurants(restaurant_id)
);



CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT NOT NULL,
    customer_id INT NOT NULL,
    order_number VARCHAR(255) UNIQUE NOT NULL,
    order_date DATE NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    status ENUM('pending', 'confirmed', 'delivered', 'cancelled') NOT NULL,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurants(restaurant_id),  -- Corrected reference
    FOREIGN KEY (customer_id) REFERENCES Customer(id)  -- Corrected table name and reference
);


CREATE TABLE Pickup (
    pickup_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    pickup_time TIME,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

CREATE TABLE Delivery (
    delivery_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    driver_id INT,
    restaurant_id INT,
    delivery_address VARCHAR(255) NOT NULL,
    driver_tip DECIMAL(6,2),
    delivery_time TIME,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (driver_id) REFERENCES Drivers(driver_id),
    FOREIGN KEY (restaurant_id) REFERENCES Restaurants(restaurant_id)
);

CREATE TABLE Reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    driver_id INT NOT NULL,
    customer_id INT NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comments TEXT,
    review_date DATE NOT NULL,
    FOREIGN KEY (driver_id) REFERENCES Drivers(driver_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(id)
);

INSERT INTO Customer (name, email, phone_number, password, birthday, address, payment) VALUES
('John Doe', 'johndoe@example.com', '123-456-7890', 'hashed_password', '1985-10-12', '1234 Elm St, Yourtown', 'Credit Card'),
('Jane Smith', 'janesmith@example.com', '987-654-3210', 'another_password', '1990-07-23', '5678 Maple St, Othertown', 'PayPal');

INSERT INTO Drivers (name, vehicle, rating, availability, phone_number) VALUES
('Alice Johnson', 'Toyota Prius', 4.5, TRUE, '321-456-9870'),
('Bob Lee', 'Honda Civic', 4.7, FALSE, '654-321-4567');

INSERT INTO Restaurants (name, address) VALUES
('Good Eats', '123 Food Lane'),
('Tasty Treats', '456 Snack Blvd');

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



