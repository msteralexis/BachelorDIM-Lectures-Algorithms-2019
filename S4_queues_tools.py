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


mode='SEND' #set 'SEND' mode is you will to send rather than receive messages


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


## lien vers RabbitMQ
amqp_url=''


# En pthon on doit créer une url 
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
## une socket pour le temps d'attente 
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP

channel = connection.channel()

channel.queue_declare(queue='hello')



## lors de l'envoi d'un message 
if mode == 'SEND':
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
                          
    print(" [x] Sent 'Hello World!'")
    
    connection.close()
## lors de la réception d'un message 
else: 
    ## basic_consume vas bloquer le programme et attend qu'un message arriver  
    channel.basic_consume(queue='hello',
                          on_message_callback=callback,                          
                          auto_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

