# 01-regex.py
import re

pattern = r'abcdefg'
s = 'abcdefghijklmn'

# re模块直接调用
l = re.findall(pattern,s)
print(l)

# compile对象调用
regex = re.compile(pattern)
l1 = regex.findall(s)
print(l1)