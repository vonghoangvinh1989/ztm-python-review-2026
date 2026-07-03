# error handling
while True:
    try:
        age = int(input("what is your age? "))
        10 / age
    except ValueError:
        print("please enter a number")
    except ValueError:  # this will not run, since only one will run, above
        print("!!!!!")
    except ZeroDivisionError:
        print("please enter age higher than 0")
    else:
        print("thank you")
        break
