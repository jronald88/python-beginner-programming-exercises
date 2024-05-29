def fizz_buzz():
    # ✅↓ Write your code here ↓✅
    for i in range(0,101):
        if i%3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i % 5 == 0:
            if i % 3 == 0:
                print("FizzBuzz")
            else:
                print("Buzz")
        else:
            print(i)
# ❌↓ DON'T CHANGE THE CODE BELOW ↓❌
fizz_buzz()
