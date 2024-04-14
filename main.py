import mysql.connector
from mysql.connector import Error

#logged in customer information
customer_name = ""
customer_email = ""
customer_phone_number = ""
customer_password = ""
customer_birthday = ""
customer_address = ""
customer_payment = ""

loggedIn = False

# Define a function to create a database connection.
def create_connection():
    """Create a database connection to the MySQL database."""
    # Initialize the connection variable as None, which will change if the connection is successful.
    connection = None
    try:
        # Attempt to create a connection using the connection parameters.
        connection = mysql.connector.connect(
            host='localhost',  # Address of the MySQL server, 'localhost' indicates it's on the local machine.
            user='root',  # Username to log in to MySQL, 'root' is the default admin user.
            password='HiMyNameIsBob1))',  # Password for the MySQL user, should be kept secret and secure.
            database='db_project'  # Name of the database to which to connect.
        )
        # If the connection is successful, print a confirmation message.
        print("Connection to MySQL DB successful")
    except Error as e:
        # If an error occurs during connection, print the error message.
        print(f"The error '{e}' occurred")
    # Return the connection object to be used in other functions.
    return connection




def list_menu_by_restaurant_name(connection, restaurant_name):
    # Use a parameterized query to safely pass the restaurant_name variable
    query = """ 
    SELECT m.item_name, m.description, m.price
    FROM Menu m
    JOIN Restaurants r ON m.restaurant_id = r.restaurant_id
    WHERE r.name = %s;
    """
    # Execute the query with the restaurant_name parameter
    cursor = connection.cursor()
    cursor.execute(query, (restaurant_name,))
    menu = cursor.fetchall()
    for item in menu:
        print(item)


def ensureLoggedIn(connection):
    global loggedIn, customer_id
    if not loggedIn:
        return customerLogin(connection)
    return True


def customerOrder(connection):
    if not ensureLoggedIn(connection):
        return  # Return after failed login attempt

    print("From the following Restaurants:")
    listAllRestaurants(connection)

    res_id = int(input("Enter Restaurant ID for the menu: "))
    print("Select from the following Menu:")
    menu_items = listMenuByRestaurantID(connection, res_id)

    try:
        order_number = input("Enter order number (e.g., 'ORD001'): ")
        order_date = input("Enter order date (YYYY-MM-DD): ")
        status = input("Enter status (pending, confirmed, delivered, cancelled): ")

        cursor = connection.cursor()

        # Insert the order into the Orders table
        insert_order_query = """
        INSERT INTO Orders (restaurant_id, customer_id, order_number, order_date, status)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_order_query, (res_id, customer_id, order_number, order_date, status))
        order_id = cursor.lastrowid

        # Get and insert order items
        addItemsToOrder(connection, order_id, menu_items)

        # Additional input for delivery details
        handleDelivery(connection, order_id, res_id)

        connection.commit()
        print("Order and delivery have been successfully recorded. This is your order id: " + str(order_id))
    
    except Exception as e:
        print("An error occurred: ", e)
        connection.rollback()
    
    finally:
        if cursor:
            cursor.close()
    

   



def listMenuByRestaurantID(connection, res_id):
    cursor = connection.cursor()
    query = "SELECT menu_id, item_name, price FROM Menu WHERE restaurant_id = %s"
    cursor.execute(query, (res_id,))
    items = cursor.fetchall()
    if items:
        for idx, item in enumerate(items, start=1):
            print(f"{idx}. {item[1]} - ${item[2]}")
    else:
        print("No items available for this restaurant.")
    cursor.close()
    return items

def addItemsToOrder(connection, order_id, menu_items):
    more_items = True
    while more_items:
        item_choice = int(input("Choose the item number to add: ")) - 1
        quantity = int(input("Enter quantity of the item: "))

        # Get the menu_id from the chosen item
        menu_id = menu_items[item_choice][0]

        insert_item_query = """
        INSERT INTO Order_Items (order_id, menu_id, quantity)
        VALUES (%s, %s, %s)
        """
        cursor = connection.cursor()
        cursor.execute(insert_item_query, (order_id, menu_id, quantity))

        more = input("Add more items to the order? (yes/no): ").lower()
        more_items = more == 'yes'

def handleDelivery(connection, order_id, restaurant_id):
    driver_id = int(input("Enter Driver ID (enter 0 if no driver): "))
    if driver_id > 0:
        delivery_address = input("Enter Delivery Address: ")
        driver_tip = float(input("Enter Driver Tip: "))
        delivery_time = input("Enter Delivery Time (HH:MM:SS): ")
        insert_delivery_query = """
        INSERT INTO Delivery (order_id, driver_id, restaurant_id, delivery_address, driver_tip, delivery_time)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor = connection.cursor()
        cursor.execute(insert_delivery_query, (order_id, driver_id, restaurant_id, delivery_address, driver_tip, delivery_time))
 

def displayOrderTotal(connection, order_id):
    try:
        # Prepare a cursor to execute the query
        cursor = connection.cursor()

        # SQL query to calculate total price of the order
        query = """
        SELECT SUM(m.price * oi.quantity) AS total_price
        FROM Order_Items oi
        JOIN Menu m ON oi.menu_id = m.menu_id
        WHERE oi.order_id = %s;
        """

        # Execute the query with the provided order_id
        cursor.execute(query, (order_id,))
        
        # Fetch the result
        total_price = cursor.fetchone()[0]  # Fetchone returns a tuple, and we need the first element

        # Check if we got a result back
        if total_price is not None:
            print(f"Total price for Order ID {order_id} is: ${total_price:.2f}")
        else:
            print(f"No items found for Order ID {order_id}, cannot calculate total price.")

    except Exception as e:
        print(f"An error occurred while calculating the total price: {e}")
    
    finally:
        if cursor:
            cursor.close()



def customerLogin(connection):
    global loggedIn

    if loggedIn:
        print("You are already logged in!")
        return

    customer_email = input("Enter your email: ")
    customer_password = input("Enter your password: ")

    query = """
    SELECT password FROM Customer WHERE email = %s;
    """
    cursor = connection.cursor()
    cursor.execute(query, (customer_email,))
    result = cursor.fetchone()
    cursor.close()

    if result:
        if result[0] == customer_password:
            loggedIn = True
            print("Successfully logging you in...")
            customer_data = fetch_customer_information(connection, customer_email, customer_password)
            update_customer_information(customer_data)
        else:
            print("Password Incorrect.")
    else:
        print("\nNo user found with that email.")

def fetch_customer_information(connection, email, password):
    try:
        cursor = connection.cursor()

        query = """
            SELECT id, name, email, phone_number, birthday, address, payment
            FROM Customer
            WHERE email = %s AND password = %s;
            """
        
        cursor.execute(query, (email,password))
        result = cursor.fetchone()

        if result:
                # Assigning fetched data to variables
                customer_id, customer_name, customer_email, customer_phone_number, customer_birthday, customer_address, customer_payment = result
                print("Customer Data Retrieved Successfully")
                return {
                    "id": customer_id,
                    "name": customer_name,
                    "email": customer_email,
                    "phone_number": customer_phone_number,
                    "birthday": customer_birthday,
                    "address": customer_address,
                    "payment": customer_payment
                }
    except Error as e:
        print(f"Error fetching customer data: {e}")
        return None
    
    finally:
        if cursor:
            cursor.close()
            
def update_customer_information(customer_data):
    global customer_id, customer_name, customer_email, customer_phone_number
    global customer_birthday, customer_address, customer_payment

    if customer_data:
        customer_id = customer_data.get("id")
        customer_name = customer_data.get("name")
        customer_email = customer_data.get("email")
        customer_phone_number = customer_data.get("phone_number")
        customer_birthday = customer_data.get("birthday")
        customer_address = customer_data.get("address")
        customer_payment = customer_data.get("payment")
        print("Global variables updated successfully")
    else:
        print("Failed to update global variables, no data provided")


def print_customer_details():
    global loggedIn
    if loggedIn:
        print("Name: %s\nEmail: %s\nPhoneNumber: %s\nPassword: %s\nBirthday: %s\nAddress: %s\nPreferred Payment Type: %s" % 
      (customer_name, customer_email, customer_phone_number, customer_password, customer_birthday, customer_address, customer_payment))
    else:
        print("Currently not logged in...")

def customerSignUp(connection):
    global customer_name, customer_email, customer_phone_number, customer_password, customer_birthday, customer_address, customer_payment

    # Gathering customer details
    customer_name = input("Enter your name: ")
    customer_email = input("Enter your email: ")
    customer_phone_number = input("Enter your phone number: ")  # Keep as string input
    customer_password = input("Create your password: ")
    customer_birthday = input("Enter your birthday (YYYY-MM-DD): ")
    customer_address = input("Enter your address: ")
    customer_payment = input("Enter your preferred payment type: ")

    # Preparing to call the stored procedure
    try:
        cursor = connection.cursor()
        
        # Call the stored procedure
        cursor.callproc('AddCustomer', (customer_name, customer_email, customer_phone_number, customer_password, customer_birthday, customer_address, customer_payment))
        connection.commit()  # Ensure changes are committed to the database
        print("Customer added successfully!")
        
    except Error as e:
        print("Error adding customer to database:", e)
        connection.rollback()  # Roll back the transaction if an error occurs
    
    finally:
        if cursor:
            cursor.close()





def execute_read_query(connection, query):
    """Execute a read query and return the results."""
    # Create a cursor object using the connection to interact with the database.
    cursor = connection.cursor()
    result = None
    try:
        # Execute the SQL query provided as an argument.
        cursor.execute(query)
        # Fetch all rows of the query result and store them in 'result'.
        result = cursor.fetchall()
        return result
    except Error as e: # type: ignore
       
        print(f"The error '{e}' occurred")


def list_all_reviews(connection):
    """List all customers in the database."""
    query = "SELECT * FROM Customer;"

    reviews = execute_read_query(connection, query)
    for review in reviews:
        print(review)

def list_all_pickup(connection):
    """List all customers in the database."""
    query = "SELECT * FROM Customer;"

    pickups = execute_read_query(connection, query)
    for pickup in pickups:
        print(pickup)

def list_all_orders(connection):
    """List all customers in the database."""
    query = "SELECT * FROM Customer;"

    orders = execute_read_query(connection, query)
    for order in orders:
        print(order)


def list_all_customers_login(connection):
    """List all customers in the database."""
    
    query = "SELECT email, password FROM Customer;"
    
    customers = execute_read_query(connection, query)
    
    for customer in customers:
        print(customer)


def list_all_customers(connection):
    """List all customers in the database."""
    query = "SELECT * FROM Customer;"

    customers = execute_read_query(connection, query)
    for customer in customers:
        print(customer)

def list_all_delivery(connection):
    """List all customers in the database."""
    query = "SELECT * FROM delivery;"

    deliveries = execute_read_query(connection, query)
    for delivery in deliveries:
        print(delivery)

def listAllRestaurants(connection):
    
    query = "SELECT * FROM Restaurants;"
    restaurants = execute_read_query(connection, query)
    for restaurant in restaurants:
        print(restaurant)

def list_all_Menu(connection):
    
    query = "SELECT * FROM Menu;"

    menu = execute_read_query(connection, query)
    for item in menu:
        print(item)

    

def list_available_drivers(connection):
    """List all available drivers."""
    
    query = """
    SELECT name, vehicle, rating, phone_number FROM Drivers
    WHERE availability = TRUE;
    """
    
    drivers = execute_read_query(connection, query)
    
    for driver in drivers:
        print(driver)

def viewOrderItems(connection, order_id):
    try:
        # Prepare a cursor to execute the query
        cursor = connection.cursor()

        # SQL query to fetch order details
        query = """
        SELECT m.item_name, m.price, oi.quantity
        FROM Order_Items oi
        JOIN Menu m ON oi.menu_id = m.menu_id
        WHERE oi.order_id = %s;
        """

        # Execute the query with the provided order_id
        cursor.execute(query, (order_id,))
        
        # Fetch all the results
        items = cursor.fetchall()

        # Check if any items were found
        if items:
            print(f"Items for Order ID {order_id}:")
            for item in items:
                item_name, price, quantity = item
                print(f"{quantity}x {item_name} at ${price} each")
        else:
            print(f"No items found for Order ID {order_id}.")

    except Exception as e:
        print(f"An error occurred while fetching order items: {e}")
    
    finally:
        if cursor:
            cursor.close()



# Define the main function that will run if the script is executed directly.
def main():
    # Print a message indicating the beginning of the database connection attempt.
    print("Connecting to Database...")
    # Call the function to create a database connection.
    connection = create_connection()
    
    if connection is not None:
        print("Welcome to Mobile Munchies!")
        while connection:
            user_input = input("\nMain Menu\n\nType '1' Sign Up\nType '2' to Log in"
                + "\nType '3' to see Account Details" +
                "\nType '4' to Order.\nType '5' to see all emails and passwords\n"
                +"Type '6' to Navigate to Print Tables Menu\n"
                +"Type '7' to see total price for an order\nType'8' to quit.")
            
            if user_input == '1':
                customerSignUp(connection)

            elif user_input == '2':
                customerLogin(connection)
                
            elif user_input == '3':
                print("Account Details:")
                print_customer_details()
            
            elif user_input == '4':
                customerOrder(connection)   

            elif user_input == '5':
                print("Here are all the Logins:")
                list_all_customers_login(connection)
                
            elif user_input == '6':
                
                while True:
                    table_input = input("\nPrint Tables Menu\n\nType '1' to print out the customer table"
                                        + "\nType '2' for delivery"
                                        + "\nType '3' for drivers"
                                        + "\nType '4' for menu"
                                        + "\nType '5' for orders"
                                        + "\nType '6' for pickup"
                                        + "\nType '7' for restaurant"
                                        + "\nType '8' for reviews"
                                        + "\nType '9' to return to Main Menu\n")
                    if table_input == '1':
                        print("\ncustomer Table List:")
                        list_all_customers(connection)

                    elif table_input == '2':
                        print("\ndelivery Table List:")
                        list_all_delivery(connection)

                    elif table_input == '3':
                        print("\ndrivers Table List:")
                        list_available_drivers(connection)

                    elif table_input == '4':
                        print("\nmenu Table List:")
                        list_all_Menu(connection)

                    elif table_input == '5':
                        print("\norders Table List:")
                        list_all_orders(connection)

                    elif table_input == '6':
                        print("\npickup Table List:")
                        list_all_pickup(connection)

                    elif table_input == '7':
                        print("\nrestaurants Table List:")
                        listAllRestaurants(connection)

                    elif table_input == '8':
                        print("\nreviews Table List:")    
                        list_all_reviews(connection)

                    elif table_input == '9':
                        print("\nReturning to Main Menu...")
                        break
                    else:
                        print("Invalid Input.")

            elif user_input == '7':
                order_id = input("Enter order ID: ")
                displayOrderTotal(connection, order_id)
                viewOrderItems(connection, order_id)
            elif user_input == '8':
                connection.close()
                break

            else: 
                print("Invalid Input!")

    # This conditional statement checks if the script is run as the main program.
if __name__ == "__main__":
    # If it is, it will call the main function.
    main()


