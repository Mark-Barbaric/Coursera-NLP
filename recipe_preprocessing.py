import pandas as pd
import nltk

num_words = ["quarter", "half", "one", "two", "three", "four", "five", "six", "seven", "eight"]
nums = ["1/4", "1/2", "1", "2", "3", "4", "5", "6", "7", "8"]
num_words_dict = dict(zip(num_words, nums))

words_to_ignore = ['of']
measure_words = ['oz', 'ounce', 
    'gram', 'g', 'grams',
    'kilogram', 'kg',
    'pinch',
    'tablespoons', 'tbsp', 'teaspoon', 'tsp',
    'cloves',
    'cup'
]

def is_ingredient(word)->bool:
    return (not word.isnumeric() and 
    word not in measure_words and 
    word not in words_to_ignore)

def preprocess_word(word: str)->str:
    lower_word = word.lower()
    if num_words_dict.get(lower_word, "N/A") != "N/A":
        return num_words_dict.get(lower_word)
    else:
        return lower_word

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

