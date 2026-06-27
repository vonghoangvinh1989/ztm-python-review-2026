# Short circuiting
is_friend = True
is_user = True

# if is_friend is true, it could never check is_user is true or not, because we use 'or'
if is_friend or is_user:
    print("best friends forever")

# if is_friend is false, it could never check is_user is true or not, because we use 'and'
if is_friend or is_user:
    print("best friends forever")
