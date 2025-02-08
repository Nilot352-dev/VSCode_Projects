def main():
    x = eval(input("Enter the first number:\n"))
    y = eval(input("Enter the second number:\n"))
    x, y = y,x
    print("Your numbers are actually these:", x,y)
main()