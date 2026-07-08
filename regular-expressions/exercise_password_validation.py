# at least 8 char long
# contain any sort letters, numbers
import re

password = "sdfsdfdfdsf5534@$9"
pattern = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")
check = pattern.fullmatch(password)
print(check)
