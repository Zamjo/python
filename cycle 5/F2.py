f1 = open("demo.txt", "r")
list1 = []
for x in f1:
    list1.append(x)
c = len(list1)
f2 = open("democpy.txt", "x")
for i in range(0,c,2):
    f2.write(list1[i])
f1.close()
f2.close()