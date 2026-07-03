# error handling
while True:
    try:
        age = int(input("what is your age? "))
        10 / age
        # raise ValueError("hey cut it out")
        raise Exception("hey cut it out")
    except ZeroDivisionError:
        print("please enter age higher than 0")
        break
    else:
        print("thank you")
    finally:
        print("ok, i am finally done")
    print("can you hear me?")
