
# ITERATOR EXAMPLE
class Countdown:

    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= 0:
            raise StopIteration

        value = self.current

        self.current -= 1

        return value

countdown = Countdown(5)

print("\n ======= Iterator Example =======")
for number in countdown:
    print(number)


print("\n ======= Generator Example =======")

# GENERATOR EXAMPLE

def first():

    yield 1
    yield 2

def second():
    yield 3
    yield 4

def all_numbers():
    yield from first()
    yield from second()

for number in all_numbers():
    print(number)
