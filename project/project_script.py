from random import choice
from string import ascii_lowercase as letters

list_of_domains = ['yaexample.com','goexample.com','example.com']

quotes = ['Luck is what happens when preparation meets opportunity','All cruelty springs from weakness',
          'Begin at once to live, and count each separate day as a separate life',
          'Throw me to the wolves and I will return leading the pack']

def generate_name(length_of_name):
    return ''.join(choice(letters) for i in range(length_of_name))

def get_domain(list_of_domains):
    return choice(list_of_domains)

def get_qoutes(list_of_qoutes):
    return choice(quotes)

def generate_record(length_of_name, list_of_domains, total_record, list_of_qoutes):
    with open("data.txt", "w") as to_write:
        for num in range(total_record):
            key = generate_name(length_of_name) + "@" + get_domain(list_of_domains)
            value = get_qoutes(list_of_qoutes)
            to_write.write(key + ":" + value + "\n")

generate_record(10, list_of_domains, 10000, quotes)
