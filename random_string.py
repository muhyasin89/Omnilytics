

"""
make identifier of 
alphabetical strings
integer
alphanumeric
real numbers(float)
alphabetical strings
alphanumeric

create random length is not more than 10
separate by (,)
"""

import random
import string

MAX_LENGTH = 10

ALPHABETIC_STRING = 1
INTEGER = 2
ALPHANUMERIC = 3
FLOAT = 4

CHOICES = {
    ALPHABETIC_STRING: "alphabetic string",
    INTEGER:"integer",
    FLOAT: "real numbers",
    ALPHANUMERIC: "alphanumeric"
}
    

def max_value():
    max_limit = MAX_LENGTH + 1
    limit =  '1'
    str_of_ints = ['0' for i in range(max_limit)]
    str_of_ints = "".join(str_of_ints)
    str_of_ints = limit + str_of_ints
    return int(str_of_ints) - 1

def random_length():
    return random.randint(0, MAX_LENGTH)

def generate_alphabetical_string():
    chars = string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(MAX_LENGTH))

def generate_integer():
    return random.randint(0, max_value())

def generate_alphanumeric():
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(MAX_LENGTH))

def generate_float():
    #convert the string so the length of float not more than MAX_LENGTH
    float_number = random.uniform(0, max_value())
    # print(float_number)

    str_float_number = str(float_number)
    length_float = len(str_float_number)
    # print(length_float)
    extend_number = length_float - MAX_LENGTH if length_float > MAX_LENGTH else 0

    str_float_number = str_float_number[extend_number:length_float]
    return float(str_float_number)
    

def generate_random():
    strings = ""
    for i in range(800000):
    # for i in range(1000):
        choice = random.randint(1, 4)

        if i != 0:
            strings = strings + ", "
    
        if choice == ALPHABETIC_STRING:
            strings = strings + str(generate_alphabetical_string()) 
        elif choice == INTEGER:
            strings = strings + str(generate_integer())
        elif choice == ALPHANUMERIC:
            strings = strings + str(generate_alphanumeric())
        elif choice == FLOAT:
            strings = strings + str(generate_float())

    return strings


#challange 1
def write_file(file_name=None, strings=None):
    if not file_name:
        file_name = 'random_string.txt'
   
    f = open(file_name, 'w+')
    f.write(strings)
    
    print(f.read())
    f.close()

# write_file()

def check_is_digit_on_string(s):
    contains_digit = False
    for character in s:
        if character.isdigit():
            contains_digit = True

    return contains_digit

    
def test_check(s):
    results = ""
    if isinstance(s, str):
        if check_is_digit_on_string(s):

            try:
                int(s)
                results = CHOICES[INTEGER]
            except:
                try:
                    float(s)
                    results = CHOICES[FLOAT]
                except:
                    results = CHOICES[ALPHANUMERIC]
        else:
            results = CHOICES[ALPHABETIC_STRING]

    # if isinstance(s, float):
    #     results = CHOICES[FLOAT]

    # if isinstance(s, int):
    #     results = CHOICES[INTEGER]

    results = " - " + results + "\n"
    return results


def read_file():
    f = open("random_string.txt", "r")
    strings = f.read()
    list_strings = strings.split(",")
    result_strings = ""
    for item in list_strings:
        result_strings = result_strings + item + test_check(item)

    return result_strings



strings = generate_random()
write_file(strings=strings)

new_strings = read_file()
write_file(file_name='new_random_string.txt', strings=new_strings)

# print(max_value())