class Guitar():
    def __init__(self, colour, string_no):
        self.colour = colour
        self.string_no = string_no

    def play(self):
        print("NOISE!")

ana_guitar = Guitar("Blue", 6)

ana_guitar.play()

example_variable_1 = 3.14152

print(type(example_variable_1))

example_variable2 = "Hello World"

print(type(example_variable2))

var = 'string example blah blah'

example_list = [
    1, 2, 3, 4, 5, 6, 7, 8
]

some_list = []
print(type(example_list))

example_list.pop()

print(ana_guitar)
