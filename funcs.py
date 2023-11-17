import re

letter_dict = {"а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "ej", "ж": "j", "з": "z", "и": "i",
               "й": "iq", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t",
               "у": "u", "ф": "f", "х": "h", "ц": "ce", "ч": "ch", "ш": "sh", "щ": "shh", "ъ": "tz", "ы": "yui",
               "ь": "mz", "э": "ye", "ю": "yu", "я": "ya"}
letter_dict_2 = {v: k for k, v in letter_dict.items()}


def encrypt(str_):
    res_str = ""

    for i in str_:
        if i.isalpha() and i.lower() in list(letter_dict.keys()):
            if i.islower():
                res_str += ":" + letter_dict[i.lower()] + ":"
            else:
                res_str += ":" + letter_dict[i.lower()].upper() + ":"
        else:
            res_str += i

    return res_str


def decrypts(str_):
    pattern = r":\w+:"

    l = re.findall(pattern, str_)
    r = str_
    for i in l:
        r = r.replace(i, "#")

    it = 0
    ms = ""
    for i in r:
        if i == "#":
            if l[it][1:-1].islower():
                ms += letter_dict_2[l[it][1:-1]]
            else:
                ms += letter_dict_2[l[it][1:-1].lower()].upper()
            it += 1
        else:
            ms += i

    return ms