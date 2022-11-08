from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

def create_bot(name):
    Bot = ChatBot(name = name,
    read_only = False,
    logic_adapters = ["chatterbot.logic.BestMatch"],
    storage_adapter = "chatterbot.storage.SQLStorageAdapter")

    return Bot


def train_all_data(Bot):
    corpus_trainer = ChatterBotCorpusTrainer(Bot)
    corpus_trainer.train("chatterbot.corpus.english")


def custom_train(Bot, conversation):
    trainer = ListTrainer(Bot)
    trainer.train(conversation)


def start_chatbot(Bot):
    print('\033c')
    print("Hello, I am Jordan. How can I help you")
    bye_list = ["bye jordan", "bye", "good bye"]

    while True:
        user_input = input("me: ")

        if user_input.lower() in bye_list:
            print("Shutting down")
            break
        
        response = Bot.get_response(user_input)
        print("Jordan: ", response)
