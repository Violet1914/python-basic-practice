f = open("C:\\Users\\ZhuanZ\\Desktop\\word.txt", "r", encoding="utf-8")
"""count = 0
for line in f:
    print(line)
    print(type(line))
    list = line.strip("\n")
    list1 = list.split(" ")
    for word in list1:
        print(word)
        if word == "itheima":
            count += 1 
print(count)
f.close()
"""

content = f.read()

print(content)

print(str, type(str))

count = content.count("itheima")

print(count)