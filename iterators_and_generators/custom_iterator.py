class Counter:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        return iter([x for x in range(self.low, self.high + 1)])


c = Counter(0, 10)

for x in Counter(0, 10):
    print(x)
