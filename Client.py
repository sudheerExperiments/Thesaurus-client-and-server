# GUI-client program
# Run multiple times for multi-threading interaction with server

####################################################
# Credits
####################################################
# AppJar library installation tutorial:
# http://appjar.info/

# TCP client program sample:
# Citation: https://stackoverflow.com/questions/35993734/python-tcp-client-connection
####################################################

# Import statements
import socket as sk
from appjar import gui
import sys


class Client(object):
    # Default connection variables
    def __init__(self, ip="127.0.0.1", port=2345):
        """Server IP and Port variables"""
        self.ip = ip
        self.port = port
        # Initializes GUI
        # Program title 'Thesaurus Program',
        # Size '600x400'
        self.obj = gui('Thesaurus Program', '800x400')

    def set_ip(self, ip):
        self.ip = ip

    def set_port(self, port):
        self.port = port

    def new_connection(self, msg):
        """ Create new connection to clients
            Receives data from server
            Searches file and returns thesaurus to server
        """
        try:
            print("New connection start")
            new_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
            new_socket.connect((self.ip, int(self.port)))

            message = msg
            # while message:
            new_socket.send(message.encode('utf-8'))

            while True:
                # Again receive data from send
                thesaurus_receive = new_socket.recv(1024)
                print("Received message")
                print(thesaurus_receive)

                new_socket.close()

                return thesaurus_receive
        except TypeError:
            print("Port number should be a number")
        except ConnectionResetError:
            print("Threads limit reached")
            print("Supports up to 5 threads currently")
            sys.exit(0)
        except ConnectionRefusedError:
            print("Server is not running")
            sys.exit(0)

    def press(self, button):
        """Buttons event calls"""
        if button == 'Clear':
            self.obj.setEntry("Enter word", "")
            self.obj.setEntry("Thesaurus", "")
        elif button == 'Search':
            word = self.obj.getEntry("Enter word")
            search_entry = word
            if search_entry:
                thesaurus = self.new_connection(search_entry)
                print(search_entry)
                self.obj.setEntry("Thesaurus", thesaurus.decode().strip('\n'))
            else:
                print("Text not entered")
        else:
            print("Invalid button clicked")

    def gui_layout(self):
        # GUI Configuration
        self.obj.addLabel("title", "Thesaurus Search")
        self.obj.setLabelBg("title", "red")
        self.obj.addLabelEntry("Enter word")
        self.obj.addLabelEntry("Thesaurus")
        self.obj.addButtons(['Search', 'Clear'], self.press)
        self.obj.setBg("orange")
        self.obj.setFont(14)
        self.obj.setFocus('Enter word')

        self.obj.go()

    def main(self):
        """Interface setup"""
        if len(sys.argv) == 1:
            print("IP and Port number not provided")
            print("Refer help using --help command")
            sys.exit(0)
        elif len(sys.argv) == 2 and sys.argv[1] == '--default':
            print("Using default arguments")
            self.gui_layout()
        elif len(sys.argv) == 2 and sys.argv[1] == '--help':
            print("Program arguments:")
            print("python3 Client.py \"ip-address\" \"port-number\" ")
            sys.exit(0)
        elif len(sys.argv) == 2:
            print("Invalid arguments")
            print("Refer help(--help) for more information")
            sys.exit(0)
        elif len(sys.argv) == 3:
            self.set_ip(sys.argv[1])
            self.set_port(sys.argv[2])
            self.gui_layout()


if __name__ == '__main__':
    client_obj = Client()
    client_obj.main()