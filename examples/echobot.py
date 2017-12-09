# -*- coding: utf-8 -*-
from linepy import *

#client = LineClient()
cl = LineClient(authToken='EnH8AqzJkPZb8TnVpBh5./tas3oEOmVGhFlvr8nYeHq.fnWkZDhIFIzWs6dz26wUFAmnkTmDfkg+5TCW+98iCp8=')

cl.log("Auth Token : " + str(client.authToken))

poll = LinePoll(cl)


helpMessage ="""戦神FreeBOT
[/help]→查看指令
[/author]→作者顯示
[/set]→抓已讀者
[/read]→查看已讀名單
[/me]→顯示自己友資
[/mid]→顯示自己mid
[/gid]→顯示群組
[/ginfo]→顯示群組詳情
[/gc]→顯示創群者
[/url]→取得群組網址
[/cancel]→取消所有邀請
[/mid:]→顯示mid的友資
[/Mid:@]→顯示被標註者的mid
[/mc:@]→顯示被標註者的友資
[/user:@]→查看標註者詳情
[/gift]→發送禮物
[/time]→現在時間
[/運勢]→今日運勢
[/bye]→退出群組
注意:此機器僅能邀入50人以上之群組
作者:戦神
https://line.me/R/ti/p/%40cld3625n"""


KAC=[cl]
mid = cl.getProfile().mid

Bots=[mid,"uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74"]
admin=["uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74","udb100d34b3733cf8820982433a77d303","uddf9714006a1010bb6551fc107f52390"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":50},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"台湾戦神BOT\n作者:https://line.me/R/ti/p/%40cld3625n\n[Made In Taiwan]",
    "lang":"JP",
    "comment":"台湾戦神☆style",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":" ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "atjointicket":True,
    "Protectcancl":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
    
setTime = {}
setTime = wait2['setTime']
mulai = time.time()

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)    




#-------------------

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]) + "\n\n[" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")


        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.acceptGroupInvitation(op.param1)
                            try:
                                    a1, a2, a3, a4, a5, a6, a7, b1, b2, b3, b4, b5 = "(*｀＾´)=3", "(`皿´)", "(o｀з’*)", "ヽ(｀Д´)ﾉ", "Σ(´д｀;)","(*'A^q)", "(*´>д<)", "(>_<)", "σ(oдolll)", "( #｀Д´)", "(｀А´)", "(#ﾟДﾟ)"
                                    a = [a1,a2,a3,a4,a5,a6,a7,b1,b2,b3,b4,b5]
                                    cl.sendText(op.param1,"人數未達50人 " + random.choice(a) + "\n\nBOT作者:戦神\n戦神販賣所↓")
				                    c = Message(to=op.param1, from_=None, text=None, contentType=13)
                	                c.contentMetadata={'mid':"u85a9b62af4ce6248cfe05324e474e226"}
				                    cl.sendMessage(c)
		                    except:
			                     pass
                            cl.leaveGroup(op.param1)
                        else:
                                cl.acceptGroupInvitation(op.param1)
				try:
					a1, a2, a3, a4, a5, a6, a7, b1, b2, b3, b4, b5 = "ヾ(*´∀｀*)ﾉ", "σ(o'ω'o)", "p(^-^q)", "ψ(｀∇´)ψ", "(#ﾟДﾟ)","(´▽｀)", "p(^-^q)", "ヾ(*´∀｀*)ﾉ", "σ(o'ω'o)", "p(^-^q)", "ψ(｀∇´)ψ", "(´▽｀)"
                	a = [a1,a2,a3,a4,a5,a6,a7,b1,b2,b3,b4,b5]
					c = Message(to=op.param1, from_=None, text=None, contentType=13)
                	c.contentMetadata={'mid':"u85a9b62af4ce6248cfe05324e474e226"}
					cl.sendText(op.param1,"戦神功能機 " + random.choice(a) + "\n請打[/help]查看指令\n\nBOT作者:戦神\n戦神販賣所↓")
					cl.sendMessage(c)
				except:
					pass
                else:
                        pass
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
		
        if op.type == 13:
            if mid not in op.param3:
		        ginfo = cl.getGroup(op.param1)
                if ginfo.invitee is None:
                            sinvitee = "0"
                else:
                            sinvitee = str(len(ginfo.invitee))
		        try:
                        cl.sendText(op.param1,"招待中人數: " + sinvitee)
                except:
                        cl.sendText(op.param1,"招待中人數: " + sinvitee)
















# Add function to LinePoll
poll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: RECEIVE_MESSAGE
})

while True:
    poll.trace()
