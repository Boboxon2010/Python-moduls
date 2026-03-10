import text_utils
import int_utils
import real_utils
import dict_utils
import list_utils

print("TEXT MODULE")
text = "Salom Dunyo"
print(text_utils.to_upper(text))
print(text_utils.reverse_text(text))
print(text_utils.count_words(text))
print(text_utils.is_palindrome("alla"))

print("\nINT MODULE")
print(int_utils.is_even(10))
print(int_utils.factorial(5))
print(int_utils.is_prime(17))
print(int_utils.to_binary(25))

print("\nREAL MODULE")
numbers = [1.5, 2.7, 3.2, 4.6]
print(real_utils.average(numbers))
print(real_utils.float_summary(numbers))
print(real_utils.percentage(25, 200))

print("\nDICT MODULE")
student = {"name": "Ali", "age": 18, "ball": 90}
print(dict_utils.get_keys(student))
print(dict_utils.add_item(student, "city", "Tashkent"))
print(dict_utils.sort_dict_by_key(student))

print("\nLIST MODULE")
items = [1, 2, 3, 2, 4, 5, 6]
print(list_utils.unique_items(items))
print(list_utils.filter_even_numbers(items))
print(list_utils.list_summary(items))