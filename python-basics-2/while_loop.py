# else can use in case loop end normally and we want something happen after that
# it does not work when break happens
i = 0
while i < 50:
    print(i)
    i += 1
    break
else:  # else block only work when there is not a break
    print("done will all the work")
