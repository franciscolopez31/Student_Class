"""A5-08 ~ Francisco Lopez"""

from array1 import Array


class Student:
    # class constants
    DEFAULT_NAME = "Unknown"
    ORIGINAL_DEFAULT_YEAR = 1
    NAME_LEN_MAX = 20
    MIN_YEAR = 6
    MAX_YEAR = 12
    DEFAULT_PHONE_NUM = "000-000-0000"
    DEFAULT_ADDRESS = "<None>"

    # class variables aka class attributes
    next_id = 0
    default_year = ORIGINAL_DEFAULT_YEAR

    def __init__(self, name=DEFAULT_NAME, year=None):
        """Initializes the student tracker"""
        if year is None:
            year = self.default_year

        # Exception Handling for each property
        try:
            self.name = name
        except (ValueError, TypeError):
            self._name = Student.DEFAULT_NAME

        try:
            self.year = year
        except ValueError:
            self._year = self.default_year

        try:
            self._phone = self.Phone()
        except ValueError:
            self._phone = Student.DEFAULT_PHONE_NUM

        try:
            self._address = self.Address()
        except ValueError:
            self._address = Student.DEFAULT_ADDRESS

        self._classes = Array()

        self.update_next_id()
        self._id = self.next_id

    @staticmethod
    def which_student_earlier(s1, s2):
        """Compare 2 students and return the student with the lower year.
        If year is same, return the one whose name is ahead alphabetically.
        """
        # If years are the same, checks which name is ahead alphabetically
        if s1.year == s2.year:
            if s1.name > s2.name:
                return s1
            else:
                return s2

        # Checks which student is in the lower grade
        if s1.year > s2.year:
            return s2
        else:
            return s1

    def __gt__(self, other):
        """Incorporates criteria from which_student_earlier and sorts two
        students to have the greatest first."""
        # Checks which student is in the lower grade
        if self.name > other.name:
            return True
        # else
        return False

    def __lt__(self, other):
        """Incorporates criteria from which_student_earlier and finds which
        student name is lower than the other."""
        if self.name < other.name:
            return True
        # else
        return False

    @classmethod
    def get_default_year(cls):
        """Getter for the default year."""
        return cls.default_year

    @classmethod
    def set_default_year(cls, new_default_year):
        """Sets the value for the default year."""
        if cls.valid_year(new_default_year):
            cls.default_year = new_default_year
        else:
            raise ValueError

    @classmethod
    def valid_year(cls, year_given):
        """Checks if the year given by the user is valid or not."""
        if Student.MIN_YEAR <= year_given <= Student.MAX_YEAR:
            return True
        else:
            return False

    @classmethod
    def update_next_id(cls):
        """Updates the id for each student."""
        cls.next_id += 1

    @property
    def address(self):
        """Getter for address"""
        return f"{self._address.house_num} {self._address.street_name}," \
               f"#{self._address.apt_num}"

    @address.setter
    def address(self, new_address):
        """Uses tuple unpacking to get the three parts of address"""
        if type(new_address) is not tuple:
            raise ValueError
        house_num, street_name, apt_num = new_address
        self._address.house_num = house_num
        self._address.street_name = street_name
        self._address.apt_num = apt_num

    @property
    def phone(self):
        """Getter for phone"""
        return str(self._phone)

    @phone.setter
    def phone(self, new_number):
        """Setter for phone"""
        if len(new_number) > 10:
            raise ValueError
        self._phone.phone_number = new_number

    @property
    def classes(self):
        """Getter for self._classes"""
        return f"{self._classes}"

    def add_class(self, period_num, new_class):
        """Adds a class to the array in the Array class"""
        self._classes[period_num] = new_class

    @property
    def name(self):
        """Getter for the name variable."""
        return self._name

    @name.setter
    def name(self, new_name):
        """Sets the name with exception handling."""
        if type(new_name) is not str:
            raise TypeError
        elif len(new_name) > Student.NAME_LEN_MAX:
            raise ValueError
        else:
            self._name = new_name

    @property
    def year(self):
        """Getter for the year variable."""
        return self._year

    @year.setter
    def year(self, year_given):
        """Sets the grade level of the student as an instance variable."""
        if self.valid_year(year_given) is False:
            raise ValueError
        self._year = year_given

    def same_grade(self, other):
        """Checks if two students are in the same grade."""
        if self.year == other.year:
            return True
        # else
        return False

    def print_info(self):
        """Prints out all the info on the student that was given."""
        print(self)

    def __str__(self):
        """Returns appropriate information of the student."""
        return f"Student ID: {self._id}, Name: {self._name}, " \
               f"Year: {self._year}\nAddress: {self._address}" \
               f"Phone: {self._phone}\nClasses: {self._classes}"

    class Phone:
        MIN_LEN = 10
        MAX_LEN = 20
        DEFAULT_PHONE_NUMBER = "000-000-0000"

        def __init__(self, number=DEFAULT_PHONE_NUMBER):
            try:
                self.phone_number = number
            except ValueError:
                print(f"{number} is either shorter than 10 digits, or "
                      f"is larger than 20 digits.")
                self._phone_number = Student.Phone.DEFAULT_PHONE_NUMBER

        @property
        def phone_number(self):
            """Sets the phone number"""
            return self._phone_number

        @phone_number.setter
        def phone_number(self, number):
            """Getter for the phone number"""
            if self.get_valid_num(number) is None:
                raise ValueError
            self._phone_number = self.get_valid_num(number)

        @classmethod
        def get_valid_num(cls, number):
            """Checks if the phone number is """
            if Student.Phone.MIN_LEN <= len(number) <= Student.Phone.MAX_LEN:
                return cls.extract_digits(number)
            # else
            return None

        @staticmethod
        def extract_digits(number):
            """Extracts all the symbols from a phone number and keeps the
            numbers"""
            extracted_num = ""
            for char in number:
                if char.isdigit():
                    extracted_num += char
            if len(extracted_num) >= Student.Phone.MIN_LEN:
                return extracted_num
            # else
            return None

        def __str__(self):
            """Returns the wanted info of the user"""
            return f"({self._phone_number[:3]}) {self._phone_number[3:6]}-" \
                   f"{self._phone_number[6:]}"

    class Address:
        DEFAULT_HOUSE_NUM = 1
        DEFAULT_STREET_NAME = "Unknown Street"
        DEFAULT_APT_NUM = 1

        MAX_APT_NUM = 1000
        MIN_APT_NUM = 0
        MIN_HOUSE_NUM = 0

        def __init__(self, house_num=DEFAULT_HOUSE_NUM,
                     street_name=DEFAULT_STREET_NAME, apt_num=DEFAULT_APT_NUM):
            try:
                self.house_num = house_num
            except ValueError:
                self._house_num = self.DEFAULT_HOUSE_NUM

            try:
                self.street_name = street_name
            except TypeError:
                self._street_name = self.DEFAULT_STREET_NAME

            try:
                self.apt_num = apt_num
            except ValueError:
                self._apt_num = self.DEFAULT_APT_NUM

        @property
        def house_num(self):
            """Returns the house number variable (getter)"""
            return self._house_num

        @house_num.setter
        def house_num(self, given_num):
            """Sets the value of the house number variable"""
            if given_num < Student.Address.MIN_HOUSE_NUM:
                raise ValueError
            self._house_num = given_num

        @property
        def street_name(self):
            """Returns the street name (getter)"""
            return self._street_name

        @street_name.setter
        def street_name(self, given_street):
            """Sets the value for the street name variable"""
            if type(given_street) is not str:
                raise TypeError
            self._street_name = given_street

        @property
        def apt_num(self):
            """Returns the apartment number (getter)"""
            return self._apt_num

        @apt_num.setter
        def apt_num(self, given_apt_num):
            """Sets the value for the apartment number variable"""
            if not self.valid_apt_num(given_apt_num):
                raise ValueError
            self._apt_num = given_apt_num

        @classmethod
        def valid_apt_num(cls, given_apt_num):
            """Checks to make sure the given apt number was valid"""
            if Student.Address.MIN_APT_NUM < given_apt_num < \
                    Student.Address.MAX_APT_NUM:
                return True
            # else
            return False

        @staticmethod
        def which_address_closer(a1, a2):
            """Checks which address is first alphabetically"""
            if a1.street_name > a2.street_name:
                return a2
            return a1

        def display(self):
            """Utilizes the __str__ method to print out the address"""
            print(self)

        def __str__(self):
            """Returns the appropriate info for the display method"""
            if self._house_num == Student.Address.DEFAULT_HOUSE_NUM or \
                    self._street_name == Student.Address.DEFAULT_STREET_NAME \
                    or self._apt_num == Student.Address.DEFAULT_APT_NUM:
                return "<None>"
            # else
            return f"{self._house_num} {self._street_name}, #{self._apt_num}\n"


class StudentListUtilities:
    NOT_FOUND = -1

    @classmethod
    def to_string(cls, students):
        """Translates the students list into a string to be printed out."""
        student_info = ""
        for i in range(len(students)):
            student_info += "\n"
            student_info += str(students[i])
            student_info += "\n"
        return student_info
