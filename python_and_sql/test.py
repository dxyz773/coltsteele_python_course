def vowel_count(str1):
    lower_str = [x.lower() for x in str1]
    test_str = {x: lower_str.count(x) for x in str1 if x in ("a", "e", "i", "o", "u")}

    return test_str


print(vowel_count("Elie"))  # {'e': 2, 'i': 1})
