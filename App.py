def Easy_Buy():
    print("EASY BUY LOAN AMOUNT CALCULATOR")

Easy_Buy()

I = float(input("Initial Payment?: "))
C = float(input("Gadget's Cost Price?: "))
R = float(input("Payment Rate?: "))
N = float(input("Monthly Payment Term?: "))

if N == 3 or N == 4:
    print("Valid Payment Term...")
else:
    print("Invalid Payment Term!!!")

D = (C - I)
Result = ((D / 10) * R)

print(Result)
print("Thanks for using my program...")