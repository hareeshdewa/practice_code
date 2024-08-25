#Recursion:
def main():
    example_one(1)

def example_one(n):
    print(n)
    example_two(2)  # Calls example_two

def example_two(n):
    print(n)
    example_three(3)  # Calls example_three

def example_three(n):
    print(n)
    example_four(4)

def example_four(n):
    print(n)
    example_five(5)

def example_five(n):
    print(n)

# Call the first function to start the sequence
main()


    





    