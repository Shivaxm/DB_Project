class Customer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Customer, cls).__new__(cls)
            cls._customer_name = ""
            cls._customer_email = ""
            cls._customer_phone_number = ""
            cls._customer_password = ""
            cls._customer_birthday = ""
            cls._customer_address = ""
            cls._customer_payment = 0
        return cls._instance

    def get_customer_name(self):
        return self._customer_name

    def set_customer_name(self, name):
        self._customer_name = name

    def get_customer_email(self):
        return self._customer_email

    def set_customer_email(self, email):
        self._customer_email = email

    def get_customer_phone_number(self):
        return self._customer_phone_number

    def set_customer_phone_number(self, phone_number):
        self._customer_phone_number = phone_number

    def get_customer_password(self):
        return self._customer_password

    def set_customer_password(self, password):
        self._customer_password = password

    def get_customer_birthday(self):
        return self._customer_birthday

    def set_customer_birthday(self, birthday):
        self._customer_birthday = birthday

    def get_customer_address(self):
        return self._customer_address

    def set_customer_address(self, address):
        self._customer_address = address

    def get_customer_payment(self):
        return self._customer_payment

    def set_customer_payment(self, payment):
        self._customer_payment = payment
