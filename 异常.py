
try:
    print(1 / 0)
except Exception as e:
    print("错误")
    print(type(e))
else:
    print("没有错误")
print("结束") 