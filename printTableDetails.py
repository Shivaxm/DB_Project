def tableMenu():
    while True:
        table_input = input("Type '1' to print out the customer table"
                            + "Type '2' for delivery"
                            + "Type '3' for drivers"
                            + "Type '4' for menu"
                            + "Type '5' for orders"
                            + "Type '6' for pickup"
                            + "Type '7' for restaurant"
                            + "Type '8' for reviews")
        if table_input == '1':
            print("dustomer Table List:")
            list_all_customers()

        elif table_input == '2':
            print("delivery Table List:")
            list_all_delivery()

        elif table_input == '3':
            print("drivers Table List:")
            list_available_drivers()

        elif table_input == '4':
            print("menu Table List:")
            list_all_Menu()

        elif table_input == '5':
            print("orders Table List:")
            list_all_orders()

        elif table_input == '6':
            print("pickup Table List:")
            list_all_pickup()

        elif table_input == '7':
            print("restaurants Table List:")
            listAllRestaurants()

        elif table_input == '8':
            print("reviews Table List:")    
            list_all_reviews()

        elif table_input == '9':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid Input.")
# Define a function to execute read (SELECT) queries.
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
        # If an error occurs during the query execution, print the error message.
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

# Define a function to list all customers from the Customer table.
def list_all_customers_login(connection):
    """List all customers in the database."""
    # SQL query to select all records from the Customer table.
    query = "SELECT email, password FROM Customer;"
    # Execute the query and get the results.
    customers = execute_read_query(connection, query)
    # Iterate over the query result and print each customer.
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

    
# Define a function to list all available drivers from the Drivers table.
def list_available_drivers(connection):
    """List all available drivers."""
    # SQL query to select certain fields from drivers that are available.
    query = """
    SELECT name, vehicle, rating, phone_number FROM Drivers
    WHERE availability = TRUE;
    """
    # Execute the query and get the results.
    drivers = execute_read_query(connection, query)
    # Iterate over the query result and print each available driver.
    for driver in drivers:
        print(driver)

