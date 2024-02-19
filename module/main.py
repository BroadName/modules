from module.application.db.people import get_employees
from module.application.salary import calculate_salary
from module.dirty_main import *
from datetime import datetime


def get_info():
    print(datetime.today())
    get_employees()
    calculate_salary()


if __name__ == '__main__':
    get_info()
