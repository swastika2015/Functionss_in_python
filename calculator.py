def add(P,Q):
    return P+Q

def sub(P,Q):
    return P-Q

def mul(P,Q):
    return P*Q

def div(P,Q):
    return P/Q


print ("please select the operation.")
print("a. Add")
print("b. substract")
print("c. multiply")
print("d. division")

choice = input("please enter the choice..(a/ b/ c/ d)")


num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))


if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1,num_2))
elif choice == 'b':
    print(num_1, "-", num_2, "=", sub(num_1,num_2))
elif choice == 'c':
    print(num_1, "*", num_2, "=", mul(num_1,num_2))
elif choice == 'd':
    print(num_1, "/", num_2, "=", div(num_1,num_2))
else:
    print("number is invalid")



