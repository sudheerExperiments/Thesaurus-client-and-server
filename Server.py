# Server Program

####################################################
# Credits
####################################################
# Tutorial to implement Client-Server program using TCP:
# https://www.youtube.com/watch?v=XiVVYfgDolU&t

# Multi-threading approch:
# https://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client

# Expected exception corrections:
# Citation: https://stackoverflow.com/questions/35993734/python-tcp-client-connection
####################################################


# Import statements
import socket as sk
from threading import Thread
import sys


class Server(Thread):
    """Server class to handle multiple clients.
        Returns synonyms from dictionary file
    """
    def __init__(self, ip, port):
        # Initialize TCP variables, create new socket
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clients_count = 0
        self.new_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.new_socket.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1)
        self.new_socket.bind((self.ip, self.port))
        print("New connection initiated")

    def receive_data(self):
        """Process client data and handle clients"""
        self.new_socket.listen(5)
        while True:
            channel, address = self.new_socket.accept()
            if self.clients_count < 5:
                Thread(target=self.listen_clients, args=(channel, address)).start()
                self.clients_count += 1
                print("No. of clients connected:" + str(self.clients_count))
            else:
                print("No new threads allowed")
                break

    def listen_clients(self, channel, address):
        """Returns synonyms
           Accepts channel and address of socket connection
           """
        print("New Connection established")
        try:
            message = channel.recv(1024)
            # Write procedure to process data here
            print("Message received: " + str(message.decode()))
            # Send again
            thesaurus = self.thesaurus(message.decode())
            channel.send(thesaurus.encode('utf-8'))
            print("Message response sent")

            # Close channel after data transfer is done.
            channel.close()
        except ConnectionResetError:
            print("Threads limit reached")
            print("Supports up to 5 threads currently")
            sys.exit(0)
        except ConnectionRefusedError:
            print("Client is not running")
            sys.exit(0)

    def thesaurus(self, message):
        """Find synonyms for a given word
           Accepts word and returns synonyms
        """
        read_pointer = open('Thesaurus.txt')

        for line in read_pointer:
            split_line = line.split(':', 1)
            if split_line[0] == message:
                return split_line[1]


class Main(object):
    def main(self):
        """Handle command line arguments"""
        if len(sys.argv) == 1:
            print("""IP and Port number not provided
                     Refer help using --help command""")
            sys.exit(0)
        elif len(sys.argv) == 2 and sys.argv[1] == '--default':
            print("Using default arguments")
            server_object = Server(ip="127.0.0.1", port=2345)
            server_object.receive_data()
        elif len(sys.argv) == 2 and sys.argv[1] == '--help':
            print("""Program arguments:
                     python3 Client.py "ip-address" "port-number" """)
            sys.exit(0)
        elif len(sys.argv) == 2:
            print("""Invalid arguments
                      Refer help(--help) for more information""")
            sys.exit(0)
        elif len(sys.argv) == 3:
            server_object = Server(sys.argv[1], sys.argv[2])
            server_object.receive_data()


if __name__ == '__main__':
    main_object = Main()
    main_object.main()
