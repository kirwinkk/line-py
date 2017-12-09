# -*- coding: utf-8 -*-
from linepy import *

client = LineClient()
#client = LineClient(authToken='AUTHTOKEN')

client.log("Auth Token : " + str(client.authToken))

poll = LinePoll(client)


# Add function to LinePoll
poll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: RECEIVE_MESSAGE
})

while True:
    poll.trace()
