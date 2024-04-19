#01
def calc_factorial():
    factorial_num = int(input("Write a number: "))
    
    if(factorial_num > 0):
        for i in range(1, factorial_num + 1):
            factorial_num *= i
            
        print(factorial_num)
    else:
        print("negative number")
    
        
calc_factorial()

#02      
def calc_prime():
    num_desired = int(input("Enter a number: "))
    
    for num in range(2, num_desired + 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, "is a prime number")


    print(f"current number: {num_desired} is not a prime number")

calc_prime()

#03
def calc_decimais():
    
    num_wanted = float(input("Insert the number you want: "))
    floated_desired = int(input("Insert the numbers of decimals you want: "))
    
    print(f"your number: {num_wanted:.{floated_desired}f}")
        

calc_decimais()

#04 
def calc_fees():
    
    initial_money = float(input("Enter your desired balance: "))
    fees_to_pay = float(input("Enter your desired fees: "))
    fees_to_pay_years = float(input("Enter your desired years: "))
    
    result = initial_money * (1 + fees_to_pay ) ** fees_to_pay_years
    
    while fees_to_pay_years <= fees_to_pay_years:
        print(f"Your new balance is: {result:.2f}")
        break
    
calc_fees()

#05
def show_messages():

    while True:
        desired_message = str(input("Enter your desired message: "))
        print("Message received")
        want_quit = str(input("Wanna quit? type: quit if dont, type: stay -> ").lower())
        
        
        if(want_quit == "quit" ):
            break
        else:
            continue
        
show_messages()