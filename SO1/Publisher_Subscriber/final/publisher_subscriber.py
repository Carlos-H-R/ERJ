import threading
import time
import os

from random import randint as rd
from queue import Queue

topics = ('esportes', 'noticias', 'tecnologia')


def publisher(publisher:str ,queue: Queue):
    # Envia mensagens para tópicos específicos (esportes, noticias, tecnologia)
    k = 15  # variavel criada para limitar o numero de mensagens enviadas por um publicador

    while(k >= 0):
        # Seleciona um tópico aleatoriamente, cria uma mensagem, posta a mensagem e aguarda 2 segundos antes de refazer esses passos

        current_topic = rd(0,2)
        message = f"Postagem do {publisher} no topico {topics[current_topic]}"
        queue.put((message,topics[current_topic]))
        k -= 1
        time.sleep(2)


def subscriber(name: str, list_of_subscribers: dict, channel):
    # Assinam um ou mais tópicos e recebem mensagens de acordo com esses tópicos
    
    # Escolhe aleatoriamente um topico para a assinatura, incluia a assinatura na lista de assinantes por topico
    subscription = topics[rd(0,2)]
    list_of_subscribers[subscription].append(name)

    # Adiciona um canal (Queue) entre o Assinante e o Broker
    channel[name] = Queue()
    print(f"{name} inscrita no topico {subscription}")

    # Deixa o assinante pronto para receber mensagens
    listening = True

    while(listening):
        try:
            # Lê as mensagens enviadas para o assinante
            message = channel[name].get(timeout=60)
            print(f"{name} recebeu mensagem: {message}")
            # time.sleep(1)

        except:
            # Se passado um minuto sem receber mensagem a assinatura é encerrada
            print("Timeout! Cancelando Assinatura!")
            listening = False


def broker(messages_queue: Queue, list_of_subscribers: dict, subscribers_channels: dict):
    # Enquanto a houverem Threads além da Main e do Broker, o broker vai executar em loop

    while(threading.active_count() > 2):
        try:
            # Tenta ler a mensagem que está na fila
            message, topic = messages_queue.get(timeout=5)

            # Se houver assinantes para o tal tópico, será enviada a mensagem para cada um deles
            if len(list_of_subscribers[topic]) > 0:
                for sub in list_of_subscribers[topic]:
                    subscribers_channels[sub].put(message)

            # Se não houver nenhum assinante a mensagem será descartada
            else:
                print("Nao ha assinantes! Mensagem descartada")

        except: 
            # Se a fila de mensagens publicadas estiver vazia o broker aguarda 2 segundos para continuar sua execução
            
            print("Sem mensagens novas")
            time.sleep(2)
        
    print("Only one thread running now!")
    print("Encerrando... ")



if __name__ == "__main__":

    # Inicia a lista de mensagens, a lista de assinaturas e os canais
    all_messages = Queue()
    list_of_subscribers = {'esportes': [], 'noticias': [], 'tecnologia': []}
    subscribers_channels = {}

    # Criação dos objetos Thread para cada publicador, assinante e para o broker
    p1 = threading.Thread(target=publisher, args=("Publicador A", all_messages, ))
    p2 = threading.Thread(target=publisher, args=("Publicador B", all_messages, ))
    s1 = threading.Thread(target=subscriber, args=("Assinatura 1", list_of_subscribers, subscribers_channels))
    s2 = threading.Thread(target=subscriber, args=("Assinatura 2", list_of_subscribers, subscribers_channels))
    b0 = threading.Thread(target=broker, args=(all_messages, list_of_subscribers, subscribers_channels))

    # Iniciada todas as Threads
    p1.start()
    p2.start()
    s1.start()
    s2.start()
    b0.start()
