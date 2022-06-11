
import subprocess
import json

# f = os.system("ipconfig")
##print(f)
x = subprocess.check_output("ipconfig")

y = x.decode('utf-8')
print(y)

array1 = y.split('\r\n')

dict1 = {
        "IPv6 Address": "", 
         "Temporary IPv6 Address": "",
         "Link-local IPv6 Address": "",
         "IPv4 Address": "", 
         "Subnet Mask": "",
         "Default Gateway": ""
        }


for n in range(len(array1)):
    for i in dict1:
        if i in array1[n]:
            if i == "Default Gateway":
                dict1[i.strip()] = [array1[n].split(i)[1].strip(". . . . . : "), array1[n+1].strip()]
            else:
                dict1[i.strip()] = array1[n].split(i)[1].strip(". . . . . : ")
            
               
print(dict1)

with open('networkinfo.json', 'w') as f:
    json.dump(dict1, f, indent=4)
