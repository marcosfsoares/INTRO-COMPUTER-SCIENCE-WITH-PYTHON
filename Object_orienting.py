class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (90,90,93,78,90)

    def average(self):
        return sum(self.grades)/len(self.grades)
    
        

student = Student()
print (student.name)
print (student.grades)
print (Student.average(student))
print (student.average())


class Studento:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades)/len(self.grades)

student2=Studento("Bob", (100,100,93,78,90))
student3=Studento("Rolf", (90,90,93,78,90))

print (student2.average())
print (Studento.average(student2))
print (student3.average())
print(Studento.average(student3))
print("="*124)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #def __str__(self):
     #   return f"Person {self.name}, {self.age} years old "

    def __repr__(self):
        return f"<Person('{self.name}',{self.age})>"

bob = Person("Bob", 35)
print(bob)


class ClassTest:
    def instance_method(self):
        print(f"Called an instance_methond of a {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print(f"Called static_method.")
test = ClassTest()
test.static_method()
ClassTest.static_method()


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighting {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)
    
        
        
book = Book.hardcover("Harry Potter",  1500)
light = Book.paperback("Python 101", 600)

print(book.name)
print(book)
print(light)
print(Book.TYPES)


