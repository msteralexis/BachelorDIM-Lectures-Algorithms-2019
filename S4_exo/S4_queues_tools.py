# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Test d'un flux d'information PC->CloudAMQP->PC
Test step 1: avec le mode 'SEND' ligne 14, lancer plusieurs fois le script pour lancer plusieurs messages dans la file dédiée dans cloudamqp
Test step 2: modifier la ligne 14 en mettant autre chose que 'SEND' dans la variable mode et lancer le script. Celui ci doit alors dépiler les messages envoyés dans le cloud et les afficher
"""
#import urlparse
import os
import pika
import argparse



## établir la connection 
def simple_queue_connection(url_para):
    ## lien vers RabbitMQ
    amqp_url=url_para
    
    # En pthon on doit créer une url 
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    ## une socket pour le temps d'attente 
    params.socket_timeout = 5
    
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    
    channel = connection.channel()
    
    channel.queue_declare(queue='presentation')
    return channel,connection


## envoi de message 
def simple_queue_publish(channel,connection,nom_utilisateur):
    channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body=nom_utilisateur)
                          
    print(" [x] nom utilisateur : ", nom_utilisateur)
   
    
    

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
   
## lecture des message  
def simple_queue_read(channel): 
    channel.basic_consume(queue='presentation',
                          on_message_callback=callback,                          
                          auto_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


    
    
alexis='amqp://idhgpxwt:3jWXg5wnsBCDsRgMaKCf0cTKpj-QjK_w@dove.rmq.cloudamqp.com/idhgpxwt'
nom_utilisateur='alexis escudero'
## appel fonction pour la connection 
channel,connection=simple_queue_connection(alexis)   
## appel fonction pour 
simple_queue_publish(channel,connection,nom_utilisateur) 




parser = argparse.ArgumentParser()

parser.add_argument("--read", action="store_true")
args = parser.parse_args()
if args.read:
    print("tralalalalalalala")
    simple_queue_read(channel)
## lors de l'envoi d'un message 
connection.close()
