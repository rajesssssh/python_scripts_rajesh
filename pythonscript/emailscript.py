import re

email_data="rajesh <rajeshRAJ076@gmail.com>, santhu <santhu@gmail.com>, pavan <pavan908@gmail.com>"
result=re.search(r"raj",email_data)
print(result)

result=re.search(r"raj[s,e]",email_data)
print(result)

result=re.search(r"raj[a-z]{2}",email_data)
print(result)


result=re.search(r"raj[a-z]+",email_data)
print(result)

result=re.search(r"raj[a-z,A-Z,0-9]+",email_data)
print(result)

result=re.findall(r"raj[a-z,A-Z,0-9]+",email_data)
print(result)

result=re.findall(r"raj[a-zA-Z0-9]+@[a-zA-Z0-9]",email_data)
print(result)

result=re.findall(r"raj[a-zA-Z0-9]+@[a-zA-Z0-9]+",email_data)
print(result)

result=re.findall(r"raj[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]+",email_data)
print(result)


result=re.findall(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]+",email_data)
print(result)


result=re.findall(r"(\w+)@(\w+)\.(\w+)",email_data)
print(result)

result=re.search(r"(\w+)@(\w+)\.(\w+)",email_data)
print(result)


