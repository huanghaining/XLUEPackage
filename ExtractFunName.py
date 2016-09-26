import re


reg = re.compile(r'(?<=function).*(?=\(.*\))',re.M)
luafile = open("C:/Users/hhn/Desktop/test.lua")
content = luafile.read()
print(reg.findall(content))


oo
