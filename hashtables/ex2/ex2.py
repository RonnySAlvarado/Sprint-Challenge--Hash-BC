from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for x in range(0, length):
      hash_table_insert(hashtable, tickets[x].source, tickets[x].destination)

    route[0] = hash_table_retrieve(hashtable, "NONE")
    for x in range(1, length):
      temp = hash_table_retrieve(hashtable, route[x-1])
      route[x] = temp

    return route