class Employee(object):
    name = ''
    email = ''
    salary = 0

    def work(self):
        return "I've come to the office "

    def check_salary(self, working_days):
        return self.salary * working_days


class Recruiter(Employee):
    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary

    def work(self):
        return super().work() + 'and start hiring.'

    def __str__(self):
        return f"{self.__class__.__name__} : {self.name}"


class Programmer(Employee):
    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary

    def work(self):
        return super().work() + 'and start coding.'

    def __str__(self):
        return f"{self.__class__.__name__} : {self.name}"


####################

programmer = Programmer('Oleg', "oleg@nomail.com", 100)
recruiter = Recruiter('Anna', "anna@nomail.com", 50)

print(programmer.work())
print(programmer.check_salary(15))
print(programmer.__str__())
print(recruiter.work())
print(recruiter.check_salary(15))
print(recruiter.__str__())
