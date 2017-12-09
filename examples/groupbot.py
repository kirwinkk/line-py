# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob
from gtts import gTTS
from bs4 import BeautifulSoup
import goslate

client = LineClient()
#client = LineClient(authToken='AUTHTOKEN')

client.log("Auth Token : " + str(client.authToken))

# Initialize LineChannel with LineClient
channel = LineChannel(client)
client.log("Channel Access Token : " + str(channel.channelAccessToken))

poll = LinePoll(client)

# Receive messages from LinePoll
def RECEIVE_MESSAGE(op):
    '''
        戦神FreeBOT
        [/help]→查看指令
        [/author]→作者顯示
    '''
    msg = op.message
    
    text = msg.text
    msg_id = msg.id
    receiver = msg.to
    sender = msg._from
    
    try:
        # Check content only text message
        if msg.contentType == 0:
            # Check only group chat
            if msg.toType == 2:
                # Chat checked request
                client.sendChatChecked(receiver, msg_id)
                # Get sender contact
                contact = client.getContact(sender)
                # Command list
                if text.lower() == '/help':
                    client.sendMessage(receiver, '戦神FreeBOT\n[/help]→查看指令\n[/author]→作者顯示')
                elif text.lower() == '/author':
                    client.sendMessage(receiver, '作者:戦神\nhttps://line.me/R/ti/p/%40cld3625n')
    except Exception as e:
        client.log("[RECEIVE_MESSAGE] ERROR : " + str(e))
    
# Auto join if BOT invited to group
def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        group_id=op.param1
        # Accept group invitation
        client.acceptGroupInvitation(group_id)
    except Exception as e:
        client.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))

# Add function to LinePoll
poll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: RECEIVE_MESSAGE,
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP
})

while True:
    poll.trace()
