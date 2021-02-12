from datetime import datetime

from models import Candidate, Vacancy
from models import Programmer, Recruiter
from models import UnableToWorkException


def write_log(exception):
    log_file = open('logs.py', 'a')
    try:
        message = exception.message
    except AttributeError:
        message = ''

    log_file.writelines(f"date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')},"
                        f" exception type:{exception.__repr__()}, "
                        f"Message: {message}, \n"
                        f"traceback: {exception.__traceback__}\n")
    log_file.close()


if __name__ == '__main__':
    try:
        f = open('emails.txt', 'w').close()

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

        """ Calls with exceptions """
        print(candidate_kolya.work())
        recruiter_kate = Recruiter('Kate', "anna@nomail.com", 50)
    except ValueError as e:
        write_log(e)
    except UnableToWorkException as e:
        write_log(e)
