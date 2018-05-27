def singleton(cls):
    instances = {}
    def getinstance(*args):
        if cls not in instances:
            instances[cls] = cls(*args)
        return instances[cls]
    return getinstance

@singleton
class Myclass:
    def __init__(self,name):
        self.name = name
    def say(self):
        print("HELLO SINGLETON : ", self.name)

ob1 = Myclass('1')
ob2 = Myclass('2')

ob1.say()
ob2.say()
