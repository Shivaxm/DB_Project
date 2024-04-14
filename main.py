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
            password='(put ur password in here)',  # Password for the MySQL user, should be kept secret and secure.
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


def customerOrder(connection):
    global loggedIn, customer_id

    if not loggedIn:
        customerLogin(connection)
        return  # Return after login attempt to give the user feedback and possibly retry

    print("From the following Restaurants:")
    listAllRestaurants(connection)

    restaurant_name = input("Enter a restaurant name: ")
    
    print("Select from the following Menu:")
    list_menu_by_restaurant_name(connection, restaurant_name)

    try:
        res_id = int(input("Enter Restaurant ID: "))
        order_number = input("Enter order number (e.g., 'ORD001'): ")
        order_date = input("Enter order date (YYYY-MM-DD): ")
        total_price = float(input("Enter total price: "))
        status = input("Enter status (pending, confirmed, delivered, cancelled): ")

        cursor = connection.cursor()

        # Insert the order into the Orders table
        insert_order_query = """
        INSERT INTO Orders (restaurant_id, customer_id, order_number, order_date, total_price, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_order_query, (res_id, customer_id, order_number, order_date, total_price, status))
        order_id = cursor.lastrowid

        # Additional input for delivery details
        driver_id = int(input("Enter Driver ID: "))
        delivery_address = input("Enter Delivery Address: ")
        driver_tip = float(input("Enter Driver Tip: "))
        delivery_time = input("Enter Delivery Time (HH:MM:SS): ")

        # Insert the delivery details into the Delivery table
        insert_delivery_query = """
        INSERT INTO Delivery (order_id, driver_id, restaurant_id, delivery_address, driver_tip, delivery_time)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_delivery_query, (order_id, driver_id, res_id, delivery_address, driver_tip, delivery_time))

       
        connection.commit()
        print("Order and delivery have been successfully recorded.")
    
    except Exception as e:
        print("An error occurred: ", e)
       
        connection.rollback()
    
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
    customer_phone_number = input("Enter your phone number: ")  # Changed to string input
    customer_password = input("Create your password: ")
    customer_birthday = input("Enter your birthday (YYYY-MM-DD): ")
    customer_address = input("Enter your address: ")
    customer_payment = input("Enter your preferred payment type: ")

    # SQL Query to insert the new customer
    query = """
    INSERT INTO Customer (name, email, phone_number, password, birthday, address, payment)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    
    try:
        # Prepare cursor and execute the insert statement
        cursor = connection.cursor()
        cursor.execute(query, (customer_name, customer_email, customer_phone_number, customer_password, customer_birthday, customer_address, customer_payment))
        connection.commit()  # Ensure changes are committed to the database
        print("Customer added successfully!")
    except Error as e:
        print("Error adding customer to database:", e)
        connection.rollback()  # Roll back the transaction if error occurs
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
                +"Type '6' to Navigate to Print Tables Menu\nType '7' to Quit.\n")
            
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
                connection.close()
                break

            else: 
                print("Invalid Input!")

    # This conditional statement checks if the script is run as the main program.
if __name__ == "__main__":
    # If it is, it will call the main function.
    main()


