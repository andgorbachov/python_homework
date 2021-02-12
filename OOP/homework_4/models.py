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


class Candidate(object):
    full_name = ''
    email = ''
    technologies = []
    main_skill = ''
    main_skill_grade = ''

    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def __str__(self):
        return f"{self.__class__.__name__} : {self.full_name}"


class Vacancy(object):
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level

    def __str__(self):
        return f"{self.__class__.__name__} : {self.title}"
