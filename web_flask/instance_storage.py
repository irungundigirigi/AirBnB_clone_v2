import pickle

class Student():
    def __init__(self, name):
        self.name = name

def reload(f):
    try:
        with open(f, 'rb') as file:
            students = pickle.load(f)
    except FileNotFoundError:
        student = []
    return students

def save(students, f):
    with open(f, 'wb') as file:
        pickle.dump(students, file)

filename = 'students_data.json'
students = reload(filename)
s = Student("Johm")
