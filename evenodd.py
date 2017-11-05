def limit(b):
    for num in range(1,b):
        if num%2==0:
            print(str(num) + " is Even number")
        else:
            print(str(num)+ " is Odd number")
limit(100)
