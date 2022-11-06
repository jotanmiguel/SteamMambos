import threading
import time
import requests


threadLock = threading.Lock()

lista = []

class testclass(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):

        while List:
            threadLock.acquire()
            print ('This is thread :', self.name )
            testclass.test()
            threadLock.release()
            time.sleep(0.001)


    def test():
        req = requests.get(f"https://steamcommunity.com/id/{List[0]}")
        cont = str(req.content)
        #The specified profile could not be found.
        #No group could be retrieved for the given URL.
        if "The specified profile could not be found." in cont:
            print("Found ! " + str(List[0]))
            lista.append(str(List[0]))
        List.pop(0)


List = [x for x in range(10**4)]


test1 = testclass('test1')
test2 = testclass('test2')
test3 = testclass('test3')
test1.start()
test2.start()
test3.start()

test1.join()
test2.join()    
test3.join()