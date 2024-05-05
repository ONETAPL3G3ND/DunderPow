class Test:
    def __init__(self, value):
        self.value = value

    def __pow__(self, power, modulo=None):
        return self.value ** power

if __name__ == "__main__":
    t = Test(2)
    print(t ** 3)