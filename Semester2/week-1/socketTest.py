import socket
import datetime
import sys

def testArgs(argc):
    if argc != 2:
        print("Enter an argument of the domain name or IP address.\nExample: python3 ./socketTest.py localhost")
        return 1

    return 0

def main(argc, argv):
    if testArgs(argc) == 0:
        # Main code goes into this if statement.
        MIN_PORT = 21
        MAX_PORT = 80

        hostname = argv[1]
        try:
            hostIP = socket.gethostbyname(hostname)

        except socket.gaierror:
            # If it can't resolve the domain/Figure out what tf the user entered.
            print("Could not resolve into an IP address. Run the program again.")
            return 1

        for port in range(MIN_PORT, MAX_PORT + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(.5)

            try:
                sock.connect((hostIP, port))
                print(f"{hostIP} port No {port}: open")

            except KeyboardInterrupt:
                print("The Program has been terminated")
                return 1

            except:
                pass
                




if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
