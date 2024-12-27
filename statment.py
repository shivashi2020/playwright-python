while True:
    try:
        x = int(input("Enter Integer :"))
        break
    except ValueError:
        print("Invalid input! Please enter an integer.")

if x < 0:
    x=0
    print("Negative Changed to Zero")
elif x == 0:
    print("Zero")
else:
    print("Grater than Zero")

