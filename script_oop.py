class Division:
    def __init__(self, a, b):
        print("Division init")
        super().__init__(a, b)  # Call next in MRO

class Modulus:
    def __init__(self, a, b):
        print("Modulus init")
        self.n = a
        self.d = b
        super().__init__(a, b)  # Cooperative call to keep the chain

class DivMod(Division, Modulus):
    def __init__(self, a, b):
        print("DivMod init")
        super().__init__(a, b)  # Start the MRO chain

x = DivMod(10, 3)
print(DivMod.__mro__)
