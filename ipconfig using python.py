
import subprocess
import json

# f = os.system("ipconfig")
##print(f)
x = subprocess.check_output("ipconfig")

y = x.decode('utf-8')
print(y)

array1 = y.split('\r\n')

dict1 = {
        "IPv6 Address. . . . . . . . . . .": "", 
         "Temporary IPv6 Address. . . . . .": "",
         "Link-local IPv6 Address . . . . .": "",
         "IPv4 Address. . . . . . . . . . .": "", 
         "Subnet Mask . . . . . . . . . . .": "",
         "Default Gateway . . . . . . . . .": ""
        }


for n in range(len(array1)):
    for i in dict1:
        if i in array1[n]:
            if i == "Default Gateway . . . . . . . . .":
                dict1[i.strip()] = [array1[n].split(i)[1].strip(":").strip().strip(":").strip(), array1[n+1].strip()]
            else:
                dict1[i.strip()] = array1[n].split(i)[1].strip(":").strip().strip(":").strip()
            
               
print(dict1)
# print("dict1",dict1)
# data = json.dumps(dict1, indent = 4)
# # print(data)

with open('networkinfo.json', 'w') as f:
    json.dump(dict1, f, indent=4)
