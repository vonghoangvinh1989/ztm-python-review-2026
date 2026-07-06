import datetime
from array import array

print(datetime.time(5, 45, 2))
print(datetime.date.today())

# use array will be have better memory performance, array(typecode, ...) - "i": int
arr = array("i", [1, 2, 3])
print(arr)
print(arr[0])
