#test
class Nhanvien:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

class InNVM(Nhanvien):
    def __init__(self):
        self.name = input("Input name: ")
        self.age = int(input("Input age: "))
        self.address = input("Input address: ")

class OutNV(InNVM):
    def outnv(self):
        print("Ten: "+self.name,"\tTuoi: "+str(self.age),"\tAddress: "+self.address)

if __name__ == '__main__':
    nv = OutNV()
    nv.outnv()

