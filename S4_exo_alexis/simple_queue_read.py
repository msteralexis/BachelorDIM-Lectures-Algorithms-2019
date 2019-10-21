#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:41:51 2019

@author: alexis
"""

import os
import pika
import argparse

## Script pour lire les message

def callback(ch, method, properties, body):
    print("message n° " )
    print(method.delivery_tag)
    print(" [x] Received %r" % body)
    




def recoit_message(channel,username):
    if not( channel.basic_consume(queue=username, on_message_callback=callback, auto_ack=True)  ):
        raise ValueError( ' il faut passer un entier') 
    
    
    print("nombre de message lu")
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()  ## basic_consume vas bloquer le programme et attend qu'un message arriver  
    