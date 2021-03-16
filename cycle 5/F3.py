with open('xl.csv','r') as f:
    f_contents=f.readlines()
    list1=list(f_contents)
    print(list1)
f.close()