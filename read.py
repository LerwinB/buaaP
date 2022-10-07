infofile = open("info.txt", "r")
info = infofile.readlines()
username = info[0]
password = info[1]

print(username)
print(int(info[2]))
print(float(info[3]))
