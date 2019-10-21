#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:41:51 2019

@author: alexis
"""

import os
import pika
import argparse
import simple_queue_read as read
import simple_queue_publish as envoi
#" Script de connection de et interface utilisateur


# connection 
amqp_url='amqp://idhgpxwt:3jWXg5wnsBCDsRgMaKCf0cTKpj-QjK_w@dove.rmq.cloudamqp.com/idhgpxwt'
username='presentation'
# En pthon on doit créer une url 
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
## une socket pour le temps d'attente 
params.socket_timeout = 5
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel =connection.channel()
channel.queue_declare(queue=username)







## interagir aec l'utilisateur 
  
parser = argparse.ArgumentParser()
parser.add_argument("--sent", help="increase output verbosity", action="store_true")
parser.add_argument("--call", help="increase output verbosity", action="store_true")
args = parser.parse_args()

if args.sent:
    print("envoie d'un message à notre file")
    envoi.envoi_donne(channel,username)
    connection.close()
elif args.call:
    print("Réception des message en cours")
    read.recoit_message(channel,username)
else: 
    print("passer un argument de type --sent ou --call")
