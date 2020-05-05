"""A5-08 ~ Francisco Lopez"""

from student import StudentListUtilities
from student import Student
import string
import random


def main():
    s1 = Student("Jacob", 12)

    s2 = Student("JP", 10)

    s3 = Student("Jonathan", 11)

    s4 = Student("Jasmine", 10)

    s5 = Student("Bresy", 11)

    students = [s1, s2, s3, s4, s5]
    for i in range(len(students)):
        try:
            students[i].phone = random_phone()
        except ValueError:
            print(f"The phone number for {students[i]} is incorrect")
        try:
            students[i].address = random_address()
        except ValueError:
            print(f"The address for {students[i]} was incorrect")

    # Prints string version of the given list of students
    print(StudentListUtilities.to_string(students))


def random_address():
    """Creates a random address using the other three methods"""
    house_num = random.randint(1000, 9999)
    st_name = "".join([str(random.choice(string.ascii_lowercase)) for _ in
                       range(random.randint(4, 9))])
    first_st_letter = f"{random.choice(string.ascii_uppercase)}"
    st_name = first_st_letter + st_name
    apt_num = random.randint(0, 100)
    return house_num, st_name, apt_num


def random_phone():
    """Creates a random phone number"""
    phone_num_list = "".join([str(random.randint(0, 9)) for _ in range(10)])
    return phone_num_list


if __name__ == "__main__":
    main()

