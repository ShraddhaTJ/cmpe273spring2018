import zmq
import sys
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket for Request/ Response using the "Context"
req_res_sock = context.socket(zmq.REP)
req_res_sock.bind("tcp://127.0.0.1:5678")

# Define the socket for Request/ Response using the "Context" just to get the user names in server console for the server to check connected users
#get_name_sock = context.socket(zmq.REP)
#get_name_sock.bind("tcp://127.0.0.1:5680")

# Define the socket to Publish/ subscibe using the "Context"
pub_sub_sock = context.socket(zmq.PUB)
pub_sub_sock.bind("tcp://127.0.0.1:5679")

#Run the server
print("---------- Chat Server Initialized ----------")
while True:
    #user = get_name_sock.recv()          #receives from the socket tcp://127.0.0.1:5678
    #get_name_sock.send_string("ok")
    #print(user)

    message = req_res_sock.recv()
    message = message.decode('utf-8')
    #req_res_sock.send_string("\n")
    print(message)
    pub_sub_sock.send_string(message)

