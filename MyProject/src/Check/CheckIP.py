
import ipaddress

class IPv4:
    def __init__(self,IP):
        self.IP=IP

class CheckIP(IPv4):
    def check(self):
        self.result = None
        try:
            ipaddress.ip_address(self.IP)
            self.result = True
        except:
            self.result = False
        return self.result

class InputIP(CheckIP):
    def __init__(self):
        self.IP = input("Input IP check: ")

class OutIP(InputIP):
    def outip(self):
        self.data = self.check()
        if(self.data==True):
            print(self.IP,"is IPv4")
        else:
            print(self.IP,"not IPv4")
