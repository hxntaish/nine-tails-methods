import os
import sys


def cooldown(time):
    print("Cooldown:")
    print("time:", time)
    os.system("sleep {0}".format(time))
    os.system("pkill screen")


def Sender(host, port, time):
    print("Sender:")
    print("host:", host)
    print("port:", port)
    print("time:", time)
    os.system("sh start-stdnospoof.sh {0} {1}".format(host, port))
    cooldown(time)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 main.py <host> <port> <time>")
        sys.exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2])
    time = int(sys.argv[3])
    Sender(host, port, time)
