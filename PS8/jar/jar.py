class Jar:
    def __init__(self, capacity=12):
        # __init__ should initialize a cookie jar with the given capacity, which represents the maximum number of
        # cookies that can fit in the cookie jar. If capacity is not a non-negative int,
        # though, __init__ should instead raise a ValueError.
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity

        self.size = 0
    def __str__(self):
        # __str__ should return a str with 🍪, where is the number of cookies in the cookie jar.
        # For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
        if self._size == 0:
            return ''
        return '🍪' * self._size


    def deposit(self, n):
        # deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity,
        # though, deposit should instead raise a ValueError.
        if n + self._size > self._capacity:
            raise ValueError
        else:
            self._size += n


    def withdraw(self, n):
        # withdraw should remove n cookies from the cookie jar. Nom nom nom.
        # If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
        if n > self._size:
            raise ValueError
        else:
            self._size -= n

    @property
    def capacity(self):
        # capacity should return the cookie jar’s capacity.
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        self._capacity = n


    @property
    def size(self):
        # size should return the number of cookies actually in the cookie jar.
        return self._size

    @size.setter
    def size(self, n):
        self._size = n