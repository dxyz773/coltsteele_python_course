import re


def extract_phone(str):
    phone_regex = re.compile(r"\b(\d{3})([ | -]?)(\d{3})([ | -]?)(\d{4}\b)")
    match = phone_regex.search(str)
    if match:
        return match.group()
    else:
        return None


# print(extract_phone("Call me at 322-435-3246"))


def extract_all_phones(str):
    phone_regex = re.compile(r"\b(\d{3})([ | -]?)(\d{3})([ | -]?)(\d{4}\b)")
    match = phone_regex.findall(str)
    return match


# print(extract_all_phones("Call me at 322-435-3246 or 243-334-2354"))


def is_valid_phone(str):
    phone_regex = re.compile(r"(\d{3})([ | -]?)(\d{3})([ | -]?)(\d{4})")
    match = phone_regex.fullmatch(str)
    return True if match else False


print(is_valid_phone("203 334-5234"))
print(is_valid_phone("203-334-5234"))
print(is_valid_phone("Call me at 203 334-5234"))
