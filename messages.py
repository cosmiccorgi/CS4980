# Function for taking in a message

def getHawkID():
    myID = 'hstmn'
    return [myID]

# Assumes message is given in this format:
# "name;char1;char2;x;y"
def parseMessage(message):
    message_list = message.split(';')
    message_list[3] = int(message_list[3])
    message_list[4] = int(message_list[4])
    return message_list

# Test run
# print(parseMessage('Cozzie;F;R;200;300'))
