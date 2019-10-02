while True:
    try:
        n = input("Please input integer: ")
        n = int(n)
        break
    except ValueError:
        print("Input not integer, please try again.")
print("Correct input")  # until user correct input, then run out of the loop
