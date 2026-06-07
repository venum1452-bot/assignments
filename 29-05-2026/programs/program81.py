class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generate(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i

# Example usage:
obj = DivisibleBySeven(50)
for num in obj.generate():
    print(num)
