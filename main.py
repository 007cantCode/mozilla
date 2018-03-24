from chatterbot.trainers import ListTrainer # method to train chatbot
from chatterbot import ChatBot #import the chatbot

bot = ChatBot('Test') #create the chatbot

conv = open('chats.txt', 'r').readlines()

bot.set_trainer(ListTrainer) #set the trainer

bot.train(conv) #train the bot

while True:
    request = input('You: ')
    response = bot.get_response(request)
    
    print('Bot: ', response)

