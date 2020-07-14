from functools import reduce
class Person:
    def __init__(self, firstName, lastName, idNumber):
		    self.firstName = firstName
		    self.lastName = lastName
		    self.idNumber = idNumber

    
    def printPerson(self):
		    print("Name:", self.lastName + ",", self.firstName)
		    print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName,lastName,idNumber,scores,):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self): 
        self.scores = scores
        result = reduce(lambda x, y: x + y, self.scores) 
        result = result/numScores
        if result >= 90:
            return  "O"
        elif result >=80 and result < 90:
            return "E"
        elif result >=70 and result < 80:
            return "A"
        elif result >=55 and result < 70:
            return "P"
        elif result >=40 and result < 55:
            return "D"
        elif result < 40:
            return ("T")
       

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

