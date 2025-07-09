# === Tuple ===
programming_languages = ("c", "c++", "java", "rust", "python",
                         "go", "javascript", "typescript", "ruby")

# === Access Tuple Items ===
index = 3
# print(f"{index} index language is", programming_languages[index])


# === Negative Indexing ===
# Negative indexing means start from the end. -1 refers to the last item, -2 refers to the second last item etc.
negative_index = -4
# print(f"{negative_index} negative index language is",
#       programming_languages[negative_index])


# === Range of Indexes ===
# print(f"range of indexes", programming_languages[2:4])

# === Update Tuples ===
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
programming_languages_list = list(programming_languages)
programming_languages_list[0] = "html"
new_programming_languages = tuple(programming_languages_list)

# print(new_programming_languages)

# === Unpacking a Tuple ===
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

# === Join Two Tuples ===
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
# print("Join Two Tuples:", tuple3)

# === Tuple count() Method ===
tuple_count_method = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 7, 7)
count = tuple_count_method.count(7)
# print(count)

# === Tuple index() Method ===
tuple_index_method = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 7, 7)
index = tuple_index_method.index(7)
print(index)
