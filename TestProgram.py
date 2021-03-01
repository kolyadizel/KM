class Student:
    def __init__(self, name, age, fav_subject):
        self.name = name
        self.age = age
        self.fav_subject = fav_subject


s1 = Student("Nikolay", 18, "km")
print("Name: " + s1.name)
print("Age: " + str(s1.age))
print("Favourite subject: " + s1.fav_subject)
