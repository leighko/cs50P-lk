"""
implement a class called Jar with these methods:

    __init__ should initialize a cookie jar with the given capacity, 
        which represents the maximum number of cookies that can fit 
        in the cookie jar. If capacity is not a non-negative int, 
        though, __init__ should instead raise a ValueError.
    __str__ should return a str with n 🍪, where n is the number of 
        cookies in the cookie jar. For instance, if there are 3 cookies 
        in the cookie jar, then str should return "🍪🍪🍪"
    deposit should add n cookies to the cookie jar. If adding that many 
        would exceed the cookie jar’s capacity, though, deposit should 
        instead raise a ValueError.
    withdraw should remove n cookies from the cookie jar. Nom nom nom. 
        If there aren’t that many cookies in the cookie jar, though, 
        withdraw should instead raise a ValueError.
    capacity should return the cookie jar’s capacity.
    size should return the number of cookies actually in the cookie jar, 
        initially 0.

Structure your class per the below. You may not alter these methods’ 
parameters, but you may add your own methods.

Either before or after you implement jar.py, additionally implement, 
in a file called test_jar.py, four or more functions that collectively 
test your implementation of Jar thoroughly, each of whose names should 
begin with test_ so that you can execute your tests.

Note that it’s not as easy to test instance methods as it is to test 
functions alone, since instance methods sometimes manipulate the same 
“state” (i.e., instance variables). To test one method (e.g., withdraw), 
then, you might need to call another method first (e.g., deposit). But 
the method you call first might itself not be correct!

And so programmers sometimes mock (i.e., simulate) state when testing 
methods, as with Python’s own mock object library, so that you can call 
just the one method but modify the underlying state first, without calling 
the other method to do so.

For simplicity, though, no need to mock any state. Implement your tests as 
you normally would!
"""

class Jar():
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return (self._size * "🍪")

    def deposit(self, n):
        if n < 0:
            raise ValueError("You can't add negative cookies, silly.")
        if self._size + n > self._capacity:
            raise ValueError("Too many cookies in the cookie jar!")
        self._size += n
        return self._size

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Cookie jar doesn't have that many cookies!")
        self._size -= n
        return self._size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    

if __name__ == "__main__":
    jar = Jar()
    jar.deposit(12)
    print(jar)
    jar.withdraw(5)
    print(jar)
    print(jar.size)










# def deposit(self, n):
#         self._size += n
#         if n < 0:
#             raise ValueError("You can't add negative cookies, silly.")
#         if self._size > self._capacity:
#             raise ValueError("Too many cookies in the cookie jar!")
#         return self._size

#     def withdraw(self, n):
#         if n > self._size:
#             raise ValueError("Cookie jar doesn't have that many cookies!")
#         self._size -= n






























# class Jar:
#     def __init__(self, capacity=12):
#         self.capac = capacity
#         if self.capac < 0:
#             raise ValueError("Must enter positive integer.")

#     def __str__(self):
#         cookie_list = []

#         for i in range(self.capac):
#             cookie_list.append("🍪")
#         return str(cookie_list)

#     def deposit(self, n):
#         self.addcook = n
#         if self.addcook > 12:
#             raise ValueError("Cookie jar can't hold that much!")

#     def withdraw(self, n):
#         self.minuscook = n
#         if self.minuscook > self.capac:
#             raise ValueError("Don't have that many cookies to take away.")

#     @property
#     def capacity(self):
#         return self.capacity

#     @property
#     def size(self):
#         return self.size