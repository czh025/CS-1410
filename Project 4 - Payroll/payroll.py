"""
Project Name: Payroll Project
Author: Zhihui Chen
Due Date: 06/09/2022
Course: CS1410-X01

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.
"""
import os.path
from abc import abstractmethod, ABC

PAY_LOGFILE = "paylog.txt"
TIMECARDS_FILE = "timecards.csv"
RECEIPTS_FILE = "receipts.csv"
EMPLOYEE_FILE = "employees.csv"

employees = []


def find_employee_by_id(emp_id):
    for emp in employees:
        if emp.emp_id == emp_id:
            return emp
    raise Exception("No such an employees.")


class Employee:
    def __init__(self, emp_id, first_name, last_name, address, city, state, zipcode, classification):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.classification = classification

    def make_salaried(self, salary):
        self.classification = Salaried(salary)

    def make_commissioned(self, salary, rate):
        self.classification = Commissioned(salary, rate)

    def make_hourly(self, rate):
        self.classification = Hourly(rate)

    def issue_payment(self):
        salary = self.classification.compute_pay()
#         TODO


class Classification(ABC):
    @abstractmethod
    def compute_pay(self):
        pass


class Salaried(Classification):
    def __init__(self, salary):
        self.salary = salary

    def compute_pay(self):
        return round(self.salary / 24, 2)


class Hourly(Classification):
    def __init__(self, hour_rate):
        self.hour_rate = hour_rate
        self.timecards = []

    def compute_pay(self):
        salary = round(sum(self.timecards) * self.hour_rate, 2)
        self.timecards.clear()
        return salary

    def add_timecard(self, hours):
        self.timecards.append(hours)


class Commissioned(Salaried):
    def __init__(self, salary, commission_rate):
        super().__init__(salary)
        self.commission_rate = commission_rate
        self.receipts = []

    def compute_pay(self):
        salary = round(self.salary / 24 + sum(self.receipts) * self.commission_rate / 100, 2)
        self.receipts.clear()
        return salary

    def add_receipt(self, receipt):
        self.receipts.append(receipt)


def load_employees():
    """
    EMPLOYEE_FILE's info:
    id, first_name, last_name, address, city, state, zipcode, classification, salary, commission, hourly

    classification 1: salary
    classification 2: commission
    classification 3: hourly
    """
    with open(EMPLOYEE_FILE, "r") as emp_f:
        emp_f.readline()
        for line in emp_f:
            info = line.rstrip().split(",")
            # emp_id = info[0]
            # first_name = info[1]
            # last_name = info[2]
            # addr = info[3]
            # city = info[4]
            # state = info[5]
            # zipcode = info[6]
            classification = int(info[7])
            salary = float(info[8])
            commission = float(info[9])
            hourly = float(info[10])
            employee_classification = Salaried(salary) if classification == 1 else \
                Commissioned(salary, commission) if classification == 2 else Hourly(hourly)
            # employees.append(Employee(emp_id, first_name, last_name, addr, city, state, zipcode, classification))
            employees.append(Employee(*info[:7], employee_classification))


def process_timecards():
    pass


def process_receipts():
    pass


def run_payroll():
    if os.path.exists(PAY_LOGFILE):
        os.remove(PAY_LOGFILE)
    for emp in employees:
        emp.issue_payment()
