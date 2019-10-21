#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:41:51 2019

@author: alexis
"""


## Script pour envoyer les message 
def envoi_donne(channel, username):
    channel.basic_publish(exchange='', routing_key=username, body='Hello World!')                    
    print(" [x] Sent 'Hello World!'")
    