from functions import *

bot = create_bot('Jordan')

train_all_data(bot)

city_born = [
    "Where was I born?",
    "Mark, you were born in Seattle."
]

fav_book = [
    "What is my favourite book?",
    "That is easy. Your favourite book is The Great Gatsby."
]

fav_movie = [
    "What is my favourite movie?",
    "You have watched Interstellar more times than I can count."
]

fav_sports = [
    "What is my favourite sport?",
    "You have always loved baseball."
]

custom_train(bot, city_born)
custom_train(bot, fav_book)
custom_train(bot, fav_movie)
custom_train(bot, fav_sports)

start_chatbot(bot)