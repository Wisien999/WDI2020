# 2. Zastosowanie listy odsyłaczowej do implementacji tablicy rzadkiej. Proszę napisać trzy funkcje:
# – inicjalizującą tablicę,
# – zwracającą wartość elementu o indeksie n,
# – podstawiającą wartość value pod indeks n.


class Node:
    def __init__(self, val = None, i = 0):
        self.val = val
        self.next = None
        self.i = i
        self.max = float("inf")


def init(n):
    a = Node()
    a.max = n
    return a

