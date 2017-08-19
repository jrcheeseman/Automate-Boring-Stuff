# Collatz sequence

# Infinite loop on last run...



def collatz(number):
    if number % 2 == 0:
        number = (number // 2) 
        return (number)
    elif number % 2 == 1:
        number = (3 * number + 1)
        return (number)
             
print('Input number.')
inputNumber = int(input())
temp = collatz(inputNumber)



while number != 1:
    temp = collatz(number)
    print(str(number))
    
if number != 1:
    temp = collatz(number)
    print(str(number))
else:
    break

