# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob
from gtts import gTTS
from bs4 import BeautifulSoup
import goslate


#client = LineClient()
client = LineClient(authToken='EnynllnyCzEIH2LJo1q5.v3xvwYAziog2B7evwhhLPq.UiB0cXNPf+ngk8I+Aw4skD3+Rr1jTs6qsN1BYbdI+dY=')

client.log("Auth Token : " + str(client.authToken))

poll = LinePoll(client)


# Receive messages from LinePoll
def RECEIVE_MESSAGE(op):
    msg = op.message

    text = msg.text
    msg_id = msg.id
    receiver = msg.to
    sender = msg._from
    
    # Check content only text message
    if msg.contentType == 0:
        # Check only group chat
        if msg.toType == 2:
            # Get sender contact
            contact = client.getContact(sender)
            txt = '[%s] %s' % (contact.displayName, text)
            # Send a message
            client.sendMessage(receiver, txt)
            # Print log
            client.log(txt)

# Add function to LinePoll
poll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: RECEIVE_MESSAGE
})

while True:
    poll.trace()
