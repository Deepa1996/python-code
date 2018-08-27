my_string = """Strings are gameon amongst gameon the most popular data types in Python. We can create the strings by enclosing characters briton in quotes. Python treats briton single quotes the same as double quotes."""
def count_words(string):
    for word in string.split():
        if word.endswith("m") == True:
            print(word,":",string.count(word))
            string = string.replace(word,'')
count_words(my_string)

