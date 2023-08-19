import rpyc
from constRPYC import *
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
    value = []

    def exposed_append(self, data):
        self.value = self.value + [data]
        return self.value

    def exposed_value(self):
        return self.value

    def exposed_insert(self, index, data):
        self.value.insert(index, data)
        return self.value

    def exposed_find(self, data):
        try:
            index = self.value.index(data)
            return index
        except ValueError:
            return None

    def exposed_remove(self, data):
        try:
            self.value.remove(data)
            return self.value
        except ValueError:
            return None

    def exposed_sort(self):
        self.value.sort()
        return self.value

if __name__ == "__main__":
    server = ThreadedServer(DBList(), port=PORT)
    server.start()
