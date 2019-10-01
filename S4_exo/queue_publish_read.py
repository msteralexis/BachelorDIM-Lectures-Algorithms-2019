# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:44:02 2019

@author: escudera
"""


import os
import pika  
import simple_queue_publish as publish

url_para='amqp://idhgpxwt:3jWXg5wnsBCDsRgMaKCf0cTKpj-QjK_w@dove.rmq.cloudamqp.com/idhgpxwt'
nom_utilisateur='alexis escudero'
## appel fonction pour la connection + envoi message
channel,connection=publish.simple_queue_publishgg(url_para,nom_utilisateur) 

connection.close()
