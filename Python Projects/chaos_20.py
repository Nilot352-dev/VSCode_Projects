# File: chaos. py
# A simple program illustrating chaotic behavior.
def main():
    print("This program illustrates chaotic behaviour.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x = 3.9 * x * 1-x
        print(x)
main()