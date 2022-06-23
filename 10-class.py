class proffessional:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o
    def do_work(self):
        print(self.name,"is a/an ",self.occupation)
    def speaks(self):
        print(self.name,"says how are you? ")


Johny=proffessional("johney depp","actor")
Johny.do_work()
Johny.speaks()
Arnold=proffessional("Arnold Prakash","famous security proffessional")
Arnold.do_work()
Arnold.speaks()
