import threading
import time
import os

from random import randint as rd
from queue import Queue

topics = ('esportes', 'noticias', 'tecnologia')


def publisher(publisher:str ,queue: Queue):
    # Envia mensagens para tópicos específicos (esportes, noticias, tecnologia)
    k = 20

    while(k >= 0):
        current_topic = rd(0,2)
        message = f"Postagem do {publisher} no topico {topics[current_topic]}"
        queue.put((message,topics[current_topic]))
        k -= 1
        time.sleep(2)


def subscriber(name: str, topics_queue: Queue, list_of_subscribers: dict):
    # Assinam um ou mais tópicos e recebem mensagens de acordo com esses tópicos
    
    # assinando
    subscription = topics[rd(0,2)]
    list_of_subscribers[subscription].append(name)
    print(f"{name} inscrita no topico {subscription}")

    # receive message
    listening = True

    while(listening):
        try:
            message = topics_queue[subscription].get(timeout=60)
            print(f"{name} recebeu mensagem: {message}")
            # time.sleep(1)

        except:
            print("Timeout! Cancelando Assinatura!")
            listening = False


def broker(messages_queue: Queue, topics_queue: dict(), list_of_subscribers):
    while(threading.active_count() > 2):
        try:
            message, topic = messages_queue.get(timeout=5)

            if len(list_of_subscribers[topic]) > 0:
                for i in range(len(list_of_subscribers[topic])):
                    topics_queue[topic].put(message)

            else:
                print("Nao ha assinantes! Mensagem descartada")

        except:    
            print("Sem mensagens novas")
            time.sleep(2)
        
    print("Only one thread running now!")
    print("Encerrando... ")



if __name__ == "__main__":
    all_messages = Queue()
    topics_queue = {'esportes': Queue(), 'noticias': Queue(), 'tecnologia': Queue()}
    list_of_subscribers = {'esportes': [], 'noticias': [], 'tecnologia': []}

    p1 = threading.Thread(target=publisher, args=("Publicador A",all_messages, ))
    p2 = threading.Thread(target=publisher, args=("Publicador B",all_messages, ))
    s1 = threading.Thread(target=subscriber, args=("Assinatura 1",topics_queue, list_of_subscribers))
    s2 = threading.Thread(target=subscriber, args=("Assinatura 2",topics_queue, list_of_subscribers))
    s3 = threading.Thread(target=subscriber, args=("Assinatura 3",topics_queue, list_of_subscribers))
    b0 = threading.Thread(target=broker, args=(all_messages, topics_queue, list_of_subscribers))

    p1.start()
    p2.start()
    s1.start()
    s2.start()
    s3.start()
    b0.start()
