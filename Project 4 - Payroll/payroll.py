"""
Project Name: Payroll Project
Author: Zhihui Chen
Due Date: 06/09/2022
Course: CS1410-X01

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.
"""

from payroll import *
from abc import abstractmethod, ABC
import os
import os.path
import shutil

PAY_LOGFILE = "paylog.txt"
TIMECARD_FILE = "timecards.csv"
SALES_FILE = "receipts.csv"
PAY_LOGFILE = "paylog.txt"


def find_employee_by_id(emp_id):
    pass


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

    def make_salaried(self, period):
        pass

    def make_commissioned(self, sales, rate):
        pass

    def make_hourly(self, hours):
        pass

    def issue_payment(self):
        pass


class Classification(ABC):
    @abstractmethod
    def compute_pay(self):
        pass


class Salaried(Classification):
    def __init__(self, salary):
        self.salary = salary

    def compute_pay(self):
        pass


class Hourly(Classification):
    def __init__(self, hour_rate, timecards):
        self.hour_rate = hour_rate
        self.timecards = timecards

    def compute_pay(self):
        pass

    def add_timecard(self):
        pass


class Commissioned(Salaried):
    def __init__(self, salary, commission_rate):
        super().__init__(salary)
        self.commission_rate = commission_rate
        self.receipts = []

    def compute_pay(self):
        pass

    def add_receipt(self):
        pass


def main():
    def load_employees():
        pass

    def process_timecards():
        pass

    def process_receipts():
        pass

    def run_payroll():
        pass

    # Save copy of payroll file; delete old file
    shutil.copyfile(PAY_LOGFILE, 'paylog_old.txt')
    if os.path.exists(PAY_LOGFILE):
        os.remove(PAY_LOGFILE)

    # Change Issie Scholard to Salaried by changing the Employee object:
    emp = find_employee_by_id('51-4678119')
    emp.make_salaried(134386.51)
    emp.issue_payment()

    # Change Reynard,Lorenzin to Commissioned; add some receipts
    emp = find_employee_by_id('11-0469486')
    emp.make_commissioned(50005.50, 27)
    clas = emp.classification
    clas.add_receipt(1109.73)
    clas.add_receipt(746.10)
    emp.issue_payment()

    # Change Jed Netti to Hourly; add some hour entries
    emp = find_employee_by_id('68-9609244')
    emp.make_hourly(47)
    clas = emp.classification
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    emp.issue_payment()


if __name__ == '__main__':
    main()
