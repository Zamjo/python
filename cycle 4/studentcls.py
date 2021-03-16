class student:
    def __init__(self, name,department, mark):
        self.name = name
        self.department = department
        self.mark = mark

    def display(self):
        print ("Name : ",self.name,", department : ", self.department,  ", Mark : ",self.mark)

std1 = student("Sam","MCA",75)
std2 = student("John","MCA",90)
std1.display()
std2.display()