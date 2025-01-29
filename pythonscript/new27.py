class computer:


    def __init__(self,cpu,ram,ssd):
        self.cpu=cpu
        self.ram=ram
        self.ssd=ssd


    def config(self):
        print(f"the cpu is {self.cpu}, ram is {self.ram} and ssd {self.ssd}")



#comp1=computer("i5", "8gb", "1tb")
#comp2=computer("i7", "16gb", "2td")

#computer.config(comp1)
#computer.config(comp2)


cpu=input("enter the cpu type:\n")
ram=input("enter the ram capacity:\n")
ssd=input("enter the ssd capacity:\n")




comp1=computer(cpu, ram, ssd)
comp1.config()
