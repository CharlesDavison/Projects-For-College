import socket
import sys

MIN_PORT = 21
MAX_PORT = 80

def getHostIP(hostname):
    try:
        return socket.gethostbyname(hostname)

    except socket.gaierror:
        # If it can't resolve the domain/Figure out what tf the user entered.
        print("Could not resolve into an IP address. Run the program again.")

def theScan(MIN_PORT, MAX_PORT, hostIP):
    for port in range(MIN_PORT, MAX_PORT + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(.5)

        try:
            sock.connect((hostIP, port))
            print(f"{hostIP} port No {port}: open")

        except KeyboardInterrupt:
            print("The Program has been terminated")
            sys.exit(1)

        except:
            pass


def main(argc, argv):
    if argc != 2:
        print("Enter an argument of the domain name or IP address.\nExample: python3 ./socketTest.py localhost")
        sys.exit(1)

    theScan(MIN_PORT, MAX_PORT, getHostIP(argv[1]))

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
