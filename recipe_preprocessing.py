import pandas as pd
import re
import unicodedata

num_words = ["quarter", "half", "one", "two", "three", "four", "five", "six", "seven", "eight"]
nums = ["1/4", "1/2", "1", "2", "3", "4", "5", "6", "7", "8"]
num_words_dict = dict(zip(num_words, nums))

words_to_ignore = ['of']

measure_words = [
        "teaspoon",
        "t",
        "tsp.",
        "tablespoon",
        "T",
        "tbl.",
        "tb",
        "tbsp.",
        "fluid ounce",
        "fl oz",
        "gill",
        "cup",
        "c",
        "pint",
        "p",
        "pt",
        "fl pt",
        "quart",
        "q",
        "qt",
        "fl qt",
        "gallon",
        "g",
        "gal",
        "ml",
        "milliliter",
        "millilitre",
        "cc",
        "mL",
        "l",
        "liter",
        "litre",
        "L",
        "dl",
        "deciliter",
        "decilitre",
        "dL",
        "bulb",
        "level",
        "heaped",
        "rounded",
        "whole",
        "pinch",
        "medium",
        "slice",
        "pound",
        "lb",
        "#",
        "ounce",
        "oz",
        "mg",
        "milligram",
        "milligramme",
        "g",
        "gram",
        "gramme",
        "kg",
        "kilogram",
        "kilogramme",
        "x",
        "of",
        "mm",
        "millimetre",
        "millimeter",
        "cm",
        "centimeter",
        "centimetre",
        "m",
        "meter",
        "metre",
        "inch",
        "in",
        "milli",
        "centi",
        "deci",
        "hecto",
        "kilo",
    ]


def is_float(word)->bool:
    return re.match(r'^-?\d+(?:\.\d+)$', word) is not None


def convert_if_vulgar_string(frac)->str:
    
    # Can't handle normal strings
    assert(len(frac) == 1)

    unicode_name = unicodedata.name(frac)

    if unicode_name.find("VULGAR") == -1:
        return frac

    return unicodedata.normalize('NFKD', frac)


def convert_vulgar_fraction(word)->str:

    if len(word) == 1:
        return str(convert_if_vulgar_string(word))
    if len(word) == 3 and word[1] == '-':
        return str(convert_if_vulgar_string(word[0]))
    
    return word


def fraction_to_string_double(word):
    if len(word) == 3 and (word[1] == '/' or word[1] == '⁄'):
        converted_num = float(word[0]) / float(word[2])
        return str(converted_num)
    
    return word


def preprocess_word(word: str)->str:
    # conver to lower string
    lower_word = word.lower()
    # replace num strings with string numbers
    lower_word = num_words_dict.get(lower_word, lower_word)
    #convert vulgar fraction
    lower_word = convert_vulgar_fraction(lower_word)
    #convert fraction to decimal
    lower_word = fraction_to_string_double(lower_word)

    return lower_word


def is_ingredient(word)->bool:
    return (not word and
        not word.isnumeric() and
    not is_float(word) and
    word not in measure_words and 
    word not in words_to_ignore)


def get_ingredient_list(ingredient_lines):
    ingredient_words = []

    for ingredient_line in ingredient_lines:
        full_ingredient_word = ""
        for word in ingredient_line.split(' '):
            preprocessed_word = preprocess_word(word)

            if is_ingredient(preprocessed_word):
                if not full_ingredient_word:
                    full_ingredient_word = preprocessed_word
                else:
                    full_ingredient_word += " " + preprocessed_word
        
        ingredient_words.append(full_ingredient_word)
    
    return ingredient_words

