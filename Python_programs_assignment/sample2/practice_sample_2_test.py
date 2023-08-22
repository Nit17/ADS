from practice_sample_2 import *


assert(find_largest_number([2,3,1,5,3,7,4])==7)
assert(find_second_largest([2,3,1,5,3,7,4])==5)
assert(separate_even_odd([2,3,1,5,3,7,4])==([2,4],[3,1,5,3,7]))
assert(are_lists_equal([1,2,4,3,4],[1,2,3,4,4])==True)
assert(find_union([1,2,3],[3,1,4,5])==[1,1,2,3,3,4,5])
assert(find_intersection([1,2,3],[3,1,4,5])==[1,3])
assert(find_union([1,2,3],[3,1,4,5])==({1,2,3,4,5},{1,3}))
assert(tuples_squares(5)==[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])
assert(remove_duplicates([1,2,4,2,1,3,5])==([4,2,1,3,5]))
assert(longest_word(["Nitin","Nithin B M","Nithin B M N"])==12)

assert(add_to_dictionary())
assert(concatenate_dictionaries({1:1,2:4},{3:9})==({1:1,2:4,3:9}))
assert(check_key_in_dictionary({1:1,2:4,3:9},2)==True)
assert(square_dictionary(4)==({1:1,2:4,3:9,4:16}))
assert(sum_values({1:1,2:4,3:9})==14)
assert(multiply_dictionary_values({1:1,2:4,3:9})==36)
assert(remove_key({1:1,2:4,3:9},2)==({1:1,3:9}))
assert(is_empty({})==True)
assert((make_dict([(1,1),(2,4)]))==({1:1,2:4}))

dict={'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 
'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 
'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 
'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': 
' ', 'w': 't'}
assert(encrypt(dict,"cat")=="km ")

