from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
import settings
from pipelines import DatabasePipeline

chatbot = ChatBot("Risk Bot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#if you want to disable the learning feature, set read_only=True as a parameter when initializing the bot:
#chatbot = ChatBot("Bot's Name", read_only=True).

def db_connect():
    #Performs database connection using database settings from settings.py.
    #Returns sqlalchemy engine instance    
    return create_engine(URL(**settings.DATABASE))

DeclarativeBase = declarative_base()


def create_messages_table(engine):
    
    DeclarativeBase.metadata.create_all(engine)

class Messages(DeclarativeBase):
    """Sqlalchemy messages model"""
    __tablename__ = "messages"

    time = Column('time',DateTime, primary_key=True)
    text = Column('title', String)

conversation = [
    "Tere!",
    "Kuidas läheb?",
    "Võta heaks",
    "Aitäh",
    "Rõõm kuulda",
    "Hästi, aitäh!"
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

response = chatbot.get_response("Tere päevast!")
print(response) 

process_item = pipelines.DatabasePipeline.process_item
process_item(self, response)

