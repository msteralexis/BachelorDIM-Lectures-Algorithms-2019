# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:44:01 2019

@author: escudera
"""

import os
import pika


def simple_queue_publishgg(url_para,nom_utilisateur):
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

    channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body=nom_utilisateur)
                          
    print(" [x] nom utilisateur : ", nom_utilisateur)
   
    return channel,connection