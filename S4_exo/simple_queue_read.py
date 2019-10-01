# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:44:02 2019

@author: escudera
"""

import os
import pika



def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
   
## lecture des message  
def simple_queue_read(channel): 
    channel.basic_consume(queue='presentation',
                          on_message_callback=callback,                          
                          auto_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

