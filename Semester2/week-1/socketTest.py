import socket
import datetime
import sys

def testArgs(argc):
    if argc != 2:
        print("Enter an argument of the domain name or IP address.\nExample: python3 ./socketTest.py localhost")
        return 1

    return 0

def main():
    argc = len(sys.argv)
    argv = sys.argv

    if testArgs(argc) == 0:
        # Main code goes into this if statement.
        hostname = argv[1]
        try:
            host_ip = socket.gethostbyname(hostname)
        except socket.gaierror:
            # If it can't resolve the domain/Figure out what tf the user entered.
            print("Could not resolve into an IP address. Run the program again.")
            return 1

        print(host_ip)


if __name__ == "__main__":
    main()
