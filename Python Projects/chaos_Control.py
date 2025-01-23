# File: chaos. py
# A simple program illustrating chaotic behavior.
def main():
    print("This program illustrates chaotic behaviour.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * 1-x
        print(x)
main()
# Using 2.0 as input just makes the numbers repeat for all iterations,
# Instead of diverging in value.