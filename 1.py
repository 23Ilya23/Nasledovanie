class Employee:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def work(self):
        print(f"{self.name} работает")


class Student:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def study(self):
        print(f"{self.name} учится")


class WorkingStudent(Employee, Student):
    pass


ws = WorkingStudent("Вася")
ws.work()
ws.study()
