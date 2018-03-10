import zmq
from threading import Thread
import sys

# ZeroMQ Context
context = zmq.Context()

# Define the socket for Request/ Response using the "Context"
req_res_sock_cli = context.socket(zmq.PUSH)
req_res_sock_cli.connect("tcp://127.0.0.1:5678")

user = " ".join(sys.argv[1:])
#user1 = "User [" + user + "] Connected to the chat server"
print("User [" + user + "] Connected to the chat server")
#get_name_sock.send_string(user1)



def run():

    

    # Define the socket to Publish/ subscibe using the "Context"
    pub_sub_sock_cli = context.socket(zmq.SUB)
    pub_sub_sock_cli.connect("tcp://127.0.0.1:5679")
    pub_sub_sock_cli.setsockopt_string(zmq.SUBSCRIBE, b"")


    #register_sub = zmq.Poller()
    #register_sub.register(pub_sub_sock, zmq.POLLIN)

    while True:
        message = pub_sub_sock_cli.recv()
        message1=message.decode('utf-8')
        if(message1):
            if("[{}]:".format(user) not in message1):
                print("\n{}".format(message1)+"/n[{}] > ".format(user))

def new_th():
    thread=Thread(target=run)
    thread.start()

new_th()
while True:
    msg= input("[{}] > ".format(user))
    msg="[%s]: %s" %(user,msg)
    req_res_sock_cli.send_string(msg)

#if __name__ == '__main__':
 #   run()

