import re
import sys
pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8,}'
if re.fullmatch(pattern, sys.argv[1]):
    print('good password')
else:
    print('bad password')
