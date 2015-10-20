class Person:
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return '{name} {age}'.format(**self.__dict__)


class Employee(Person):
    def __init__(self, name, age, salary, dept):
        super().__init__(name, age)
        self.salary = salary
        self.dept = dept

    def __str__(self):
        return '{name} {age} {salary} {dept}'.format(**self.__dict__)


emp = Employee('Edna', 'Smith', 99275.00, 'IT')
print(emp)