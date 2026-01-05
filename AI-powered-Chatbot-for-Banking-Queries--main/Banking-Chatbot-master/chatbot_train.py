from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


def setup():
    chatbot = ChatBot(
        'Bot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter'
    )

    # Update this path if your training data directory is different
    data_dir = r'C:\Users\Admin\Desktop\chatbot\Banking-Chatbot-master'

    trainer = ListTrainer(chatbot)

    for fname in os.listdir(data_dir):
        file_path = os.path.join(data_dir, fname)
        if not os.path.isfile(file_path):
            continue
        with open(file_path, encoding='latin-1') as f:
            convData = f.readlines()
        trainer.train(convData)

    print("Training completed")


if __name__ == '__main__':
    setup()
