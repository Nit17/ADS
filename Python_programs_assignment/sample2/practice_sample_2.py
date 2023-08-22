#1.Python Program to Find the Largest Number in a List
import random


def find_largest_number(number):
    if not number:
        return 0  
    largest = number[0]  
    for num in number:
        if num > largest:
            largest = num
    return largest

#2.Python Program to Find the Second Largest Number in a List
def find_second_largest(numbers):
    if len(numbers) < 2:
        return None  
    
    largest = second_largest = float('-inf')  
    
    for n in numbers:
        if n > largest:
            second_largest = largest
            largest = n
        elif n > second_largest and n!= largest:
            second_largest = n
    
    return second_largest

#3.Python Program to Put Even and Odd elements in a List into Two Different Lists.
def separate_even_odd(input_list):
    even_list = []
    odd_list = []
    
    for n in input_list:
        if n % 2 == 0:
            even_list.append(n)
        else:
            odd_list.append(n)
    
    return even_list, odd_list

#4.Python Program to check whether two lists are same.
def are_lists_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    
    return True

#5.Python Program to Find the Union of Lists.
def find_union(list1, list2):
    union = list(set(list1) | set(list2))
    return union

#6.Python Program to Find the Intersection of Lists.
def find_intersection(list1, list2):
    intersection = list(set(list1) & set(list2))
    return intersection

#7.Python Program to find union and intersection of lists without repetition.
def find_union(list1, list2):
    union = list(set(list1).union(set(list2)))
    return union

def find_intersection(list1, list2):
    intersection = list(set(list1).intersection(set(list2)))
    return intersection

#8.Python Program to Create a List of Tuples with the First Element as the Number and
#  Second Element as the Square of the Number.
def tuples_squares(numbers):
    tuple_list = [(num, num ** 2) for num in numbers]
    return tuple_list

#9.Python Program to Remove the Duplicate Items from a List.
def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list

#10.Python Program to Read a List of Words and Return the Length of the Longest One.
def longest_word(word_list):
    if not word_list:
        return 0  
    
    max_length = len(word_list[0])  
    
    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)
    
    return max_length

#11.Python Program to Add a Key-Value Pair to the Dictionary
def add_to_dictionary(dictionary, key, value):
    dictionary[key] = value

my_dict = {
    'name': 'Nitin',
    'age': 23,
    'city': 'Tarikere'
}
new_key = 'student'
new_value = 'engineer'
add_to_dictionary(my_dict, new_key, new_value)

#12.Python Program to Concatenate Two Dictionaries Into One
def concatenate_dictionaries(dict1, dict2):
    concatenated_dict = {**dict1, **dict2}
    return concatenated_dict


dict_a = {'nit': 1, 'gow': 2}
dict_b = {'kub': 3, 'sac': 4}


result_dict = concatenate_dictionaries(dict_a, dict_b)

#13.Python Program to Check if a Given Key Exists in a Dictionary or Not
def check_key_in_dictionary(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

my_dict = {
    'name': 'Nitin',
    'age': 23,
    'city': 'Tarikere'
}

key_to_check = 'age'

key_exists = check_key_in_dictionary(my_dict, key_to_check)

#14.Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
def square_dictionary(n):
    square_dict = {x: x*x for x in range(1, n+1)}
    return square_dict

n = int(input("Enter a value for n: "))

dictionary = square_dictionary(n)

#15.Python Program to Sum All the Items in a Dictionary
def sum_values(dictionary):
    total_sum = sum(dictionary.values())
    return total_sum

my_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40
}

total_sum = sum_values(my_dict)

#16.Python Program to Multiply All the Items in a Dictionary
def multiply_dictionary_values(dictionary, multiplier):
    for key in dictionary:
        dictionary[key] *= multiplier
my_dictionary = {'a': 1, 'b': 2, 'c': 3}

multiplier = 1

multiply_dictionary_values(my_dictionary, multiplier)

#17.Python Program to Remove the Given Key from a Dictionary
def remove_key(dictionary, key_to_remove):
    if key_to_remove in dictionary:
        del dictionary[key_to_remove]
        print(f"Key '{key_to_remove}' removed from the dictionary.")
    else:
        print(f"Key '{key_to_remove}' not found in the dictionary.")

my_dictionary = {'a': 1, 'b': 2, 'c': 3}

key_to_remove = 'b'  

remove_key(my_dictionary, key_to_remove)

#18.Write a function is_empty(my_dict)
#that takes a dictionary my_dict and returns True if my_dict is empty and False otherwise.
def is_empty(my_dict):
    return len(my_dict) == 0
empty_dict = {}
non_empty_dict = {'a': 1, 'b': 2}

#19.Write a function make_dict(key_value_list)
#that takes a list of tuples key_value_list where each tuple is of the form (key, value) 
#and returns a dictionary with these keys and corresponding values.
def make_dict(key_value_list):
    result_dict = {}
    for key, value in key_value_list:
        result_dict[key] = value
    return result_dict

key_value_list = [('a', 1), ('b', 2), ('c', 3)]

result = make_dict(key_value_list)

#20.A  simple  substitution  cipher  is  an  encryption  scheme  where  each  letter
#in  an alphabet  to replaced  by  a  different  letter  in  the  same  alphabet  with  the  restriction  that
#each  letter's replacement  is  unique.  The  template  for  this  question  contains  anexample  of  a 
#substitution cipher   represented   a   dictionary   
#CIPHER_DICTIONARY.Your   taskis   to   write   a   function encrypt(phrase,cipher_dict)  that  takes  a  string  phrase  and  a 
#dictionary  cipher_dict  and  returns the results of replacing each character in phrase by its corresponding value in 
#cipher_dict.CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}
#encrypt("cat", CIPHER_DICT) should return ”km “

def encrypt(phrase, cipher_dict):
    encrypted_phrase = ""
    for char in phrase:
        if char in cipher_dict:
            encrypted_phrase += cipher_dict[char]
        else:
            encrypted_phrase += char
    return encrypted_phrase

CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}

#21.Write a function make_cipher_dict(alphabet) that takes a string of unique characters and returns a randomly-generated cipher dictionary for the characters in alphabet .
#You should use the shuffle() method in the random module to ensure that your returned cipher dictionary is random

def make_cipher_dict(alphabet):
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    
    cipher_dict = {}
    for original, shuffled in zip(alphabet, shuffled_alphabet):
        cipher_dict[original] = shuffled
    
    return cipher_dict

#22.Write a python code to generate grade using dictionary. 
#Dictionary should have student names as keys (assuming names are unique)
#and subject_name and mark as value. There are 5 subjects for each student. 
# Marks should be converted to grades (90 –100 A+, 80-89 A etc).

def calculate_grade(mark):
    if mark >= 90:
        return 'A+'
    elif mark >= 80:
        return 'A'
    elif mark >= 70:
        return 'B'
    elif mark >= 60:
        return 'C'
    elif mark >= 50:
        return 'D'
    else:
        return 'F'

def generate_student_grades(student_marks):
    student_grades = {}
    for student, marks in student_marks.items():
        subject_grades = {}
        for subject, mark in marks.items():
            subject_grades[subject] = calculate_grade(mark)
        student_grades[student] = subject_grades
    return student_grades


student_marks = {
    'Nit': {'Math': 92, 'Science': 88, 'English': 75, 'History': 60, 'Art': 45},
    'Sac': {'Math': 78, 'Science': 95, 'English': 82, 'History': 70, 'Art': 58},
    'vsh': {'Math': 65, 'Science': 70, 'English': 58, 'History': 40, 'Art': 75}
}

student_grades = generate_student_grades(student_marks)

for student, grades in student_grades.items():
    print(f"{student}'s Grades:")
    for subject, grade in grades.items():
        print(f"  {subject}: {grade}")
