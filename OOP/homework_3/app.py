from models import Programmer, Recruiter
from models import Candidate, Vacancy

if __name__ == '__main__':

    technologies = ['python', 'js', 'html', 'css']
    recruiter_anna = Recruiter('Anna', "anna@nomail.com", 50)
    programmer_oleg = Programmer('Oleg', "oleg@nomail.com", 100)
    programmer_vasya = Programmer('Vasya', "vasya@nomail.com", 75)
    candidate_grisha = Candidate('Grisha Vetrov', 'grisha@nomail.com', technologies, 'Python', 'Middle')
    candidate_petya = Candidate('Petr Vetrov', 'petr@nomail.com', technologies, 'Python', 'Junior')
    candidate_kolya = Candidate('Kolya Ivanov', 'kolya@nomail.com', technologies, 'Python', 'Senior')
    vacancy_python_middle = Vacancy('Python Middle on Project 1', 'Python', 'Middle')
    vacancy_python_senior = Vacancy('Python Senior on Project 2', 'Python', 'Senior')

    print(programmer_oleg.work())
    print(programmer_vasya.check_salary(15))
    print(programmer_oleg.__str__())
    print(recruiter_anna.work())
    print(recruiter_anna.check_salary(15))
    print(recruiter_anna.__str__())

    print(candidate_grisha.__str__())
    print(candidate_petya.__str__())
    print(candidate_kolya.__str__())
    print(vacancy_python_middle.__str__())
    print(vacancy_python_senior.__str__())
