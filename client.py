import rpyc
from constRPYC import *

class Client:
    conn = rpyc.connect(SERVER, PORT)

    print(conn.root.exposed_value())
    conn.root.exposed_append(5)
    conn.root.exposed_append(6)
    print(conn.root.exposed_value())

    print(conn.root.exposed_insert(1, 7))
    print(conn.root.exposed_value())

    print(conn.root.exposed_find(5))

    print(conn.root.exposed_remove(5))
    print(conn.root.exposed_value())

    print(conn.root.exposed_sort())
    print(conn.root.exposed_value())
