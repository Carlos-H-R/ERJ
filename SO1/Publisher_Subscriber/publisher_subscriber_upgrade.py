import threading
import time
import os

from random import randint as rd
from queue import Queue

topics = ('esportes', 'noticias', 'tecnologia')


class Publisher():
    publisher: str
    queue: Queue
    lifetime: int

    def __init__(self, publisher, queue) -> None:
        threading.Thread(target=self.create, args=(publisher,queue)).start()
    
    def create(self, publisher, queue):
        self.publisher = publisher
        self.queue = queue

        self.lifetime()

        while(self.lifetime > 0):
            self.publish()
            self.lifetime -= 1
            time.sleep(2)

    def publish(self):
        current_topic = self.select_topic()
        message = f"Postagem do {self.publisher} no topico {current_topic}"
        self.queue.put((message,current_topic))

    def lifetime(self):
        self.lifetime = rd(10,50)

    def select_topic(self):
        return topics[rd(0,2)]


class Subscriber():
    name: str
    list_of_subscribers: dict
    channel: dict
    listening: bool
    topics = [str]

    def __init__(self, name: str, list_of_subscribers: dict, channel: dict, topics) -> None:
        threading.Thread(target=self.generate, args=(name, list_of_subscribers, channel, topics)).start()

    def generate(self, name, list_of_subscribers, channel, selected_topics):
        self.name = name
        self.list_of_subscribers = list_of_subscribers
        self.channel = channel

        self.channel[self.name] = Queue()

        self.subscription(selected_topics)

        self.recieve()


    def subscription(self, selected_topics):
        if(selected_topics == None):
            self.topics = [topics[rd(0,2)]]
            self.subscribe(self.topics[0])

        else:
            for topic in selected_topics:
                if topic in topics:
                    self.topics.append(topic)
                    self.subscribe(topic)

                else:
                    print(f"{topic} nao e um topico disponivel")

    def subscribe(self, topic):
        list_of_subscribers[topic].append(self.name)
        print(f"{self.name} inscrita no topico {topic}")

    def recieve(self):
        self.listening = True

        while(self.listening):
            try:
                message = self.channel[self.name].get(timeout=60)
                print(f"{self.name} recebeu mensagem: {message}")

            except:
                print("Timeout! Cancelando assinatura!")
                self.listening = False


class Broker():
    messages_queue: Queue
    list_of_subscribers: dict
    subscribers_channels: dict

    def __init__(self, messages_queue: Queue, list_of_subscribers: dict, subscribers_channels: dict) -> None:
        threading.Thread(target=self.create, args=(messages_queue, list_of_subscribers, subscribers_channels)).start()

    def create(self, messages_queue: Queue, list_of_subscribers: dict, subscribers_channels: dict):
        self.messages_queue = messages_queue
        self.list_of_subscribers = list_of_subscribers
        self.subscribers_channels = subscribers_channels
        
        while(threading.active_count() > 2):
            self.read_delegate()

        print("Encerrando...")

    def read_delegate(self):
        try:
            message, topic = self.messages_queue.get(timeout=5)
            self.post(message, topic)

        except:
            print("Sem mensagens novas")
            return None, None

    def post(self, message, topic):
        if len(list_of_subscribers[topic]) > 0:
                for sub in list_of_subscribers[topic]:
                    subscribers_channels[sub].put(message)

        else:
            print("Nao ha assinantes! Mensagem descartada")


if __name__ == "__main__":
    all_messages = Queue()
    list_of_subscribers = {'esportes': [], 'noticias': [], 'tecnologia': []}
    subscribers_channels = {}

    Publisher("Publicador A", all_messages)
    Publisher("Publicador B", all_messages)
    Publisher("Publicador Z", all_messages)
    Subscriber("Assinatura 1", list_of_subscribers, subscribers_channels, ['esportes'])
    Subscriber("Assinatura 2", list_of_subscribers, subscribers_channels, ['noticias'])
    Subscriber("Assinatura 3", list_of_subscribers, subscribers_channels, ['tecnologia'])
    Subscriber("Assinatura 13", list_of_subscribers, subscribers_channels, None)
    Subscriber("Assinatura 15", list_of_subscribers, subscribers_channels, None)
    Broker(all_messages, list_of_subscribers, subscribers_channels)
