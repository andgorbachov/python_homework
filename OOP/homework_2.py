class Employee(object):
    name = ''
    email = ''
    salary = 0

    def work(self):
        return "I've come to the office "

    def check_salary(self, working_days):
        return self.salary * working_days


class Recruiter(Employee):
    def work(self):
        return super().work() + 'and start hiring.'

    def __str__(self):
        return f"{self.__class__.__name__} : {self.name}"


class Programmer(Employee):
    def work(self):
        return super().work() + 'and start coding.'

    def __str__(self):
        return f"{self.__class__.__name__} : {self.name}"


####################

programmer = Programmer()
programmer.name = 'Oleg'
programmer.email = "oleg@nomail.com"
programmer.salary = 100
recruiter = Recruiter()
recruiter.name = 'Anna'
recruiter.email = "anna@nomail.com"
recruiter.salary = 50

print(programmer.work())
print(programmer.check_salary(15))
print(recruiter.work())
print(recruiter.check_salary(15))
