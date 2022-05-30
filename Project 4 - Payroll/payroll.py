"""
Project Name: Payroll Project
Author: Zhihui Chen
Due Date: 06/09/2022
Course: CS1410-X01

in order for this program to work, paylog.txt, timecards.csv, receipts.csv, and employees.csv are needed
this program can calculate the salaries of different types of employees
finally saves the information of employees who need to be paid into a file

through this program, I learn how to use abstract method
this program also deepened my understanding of class
"""
import os.path
from abc import abstractmethod, ABC

PAY_LOGFILE = "paylog.txt"
TIMECARDS_FILE = "timecards.csv"
RECEIPTS_FILE = "receipts.csv"
EMPLOYEE_FILE = "employees.csv"

employees = []


def find_employee_by_id(emp_id):
    """
    Find employee by id, throw an error if there is no matching ID
    """
    for emp in employees:
        if emp.emp_id == emp_id:
            return emp
    raise Exception("No such an employee.")


class Employee:
    def __init__(self, emp_id, first_name, last_name, address, city, state, zipcode, classification):
        """
        emp_id will be used to match data
            and classification will add components from other function, so keep these public
        """
        self.emp_id = emp_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        self.classification = classification

    def make_salaried(self, salary):
        self.classification = Salaried(salary)

    def make_commissioned(self, salary, rate):
        self.classification = Commissioned(salary, rate)

    def make_hourly(self, rate):
        self.classification = Hourly(rate)

    def issue_payment(self):
        salary = self.classification.compute_pay()
        with open(PAY_LOGFILE, "a") as pay_log_f:
            if salary > 0:
                pay_log_f.write(f"Mailing {salary:.2f} to {self.__first_name} {self.__last_name} "
                                f"at {self.__address} {self.__city} {self.__state} {self.__zipcode}\n")


class Classification(ABC):
    @abstractmethod
    def compute_pay(self):
        pass


class Salaried(Classification):
    def __init__(self, salary):
        """
        salary will be inherited to Commissioned class, so keep it public
        """
        self.salary = salary

    def compute_pay(self):
        """
        return float
        """
        return round(self.salary / 24, 2)


class Hourly(Classification):
    def __init__(self, hour_rate):
        self.__hour_rate = hour_rate
        self.__timecards = []

    def compute_pay(self):
        """
        clear employee timecard, after computing salary
        return float
        """
        salary = round(sum(self.__timecards) * self.__hour_rate, 2)
        self.__timecards.clear()
        return salary

    def add_timecard(self, hours):
        self.__timecards.append(hours)


class Commissioned(Salaried):
    def __init__(self, salary, commission_rate):
        super().__init__(salary)
        self.__commission_rate = commission_rate
        self.__receipts = []

    def compute_pay(self):
        """
        clear employee receipts, after computing salary
        return float
        """
        salary = round(self.salary / 24 + sum(self.__receipts) * self.__commission_rate / 100, 2)
        self.__receipts.clear()
        return salary

    def add_receipt(self, receipt):
        self.__receipts.append(receipt)


def load_employees():
    """
    skip the first line, process raw data
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
            classification = int(info[7])
            salary = float(info[8])
            commission = float(info[9])
            hourly = float(info[10])
            employee_classification = Salaried(salary) if classification == 1 else \
                Commissioned(salary, commission) if classification == 2 else Hourly(hourly)
            employees.append(Employee(*info[:7], employee_classification))


def process_timecards():
    """
    processing of raw data into a timecard list
    """
    with open(TIMECARDS_FILE, "r") as timecard_f:
        for line in timecard_f:
            info = line.strip().split(",")
            emp_id = info[0]
            timecards = list(map(float, info[1:]))
            employee = find_employee_by_id(emp_id)
            if isinstance(employee.classification, Hourly):
                for card in timecards:
                    employee.classification.add_timecard(card)


def process_receipts():
    """
    processing of raw data into a receipt list
    """
    with open(RECEIPTS_FILE, "r") as receipts_f:
        for line in receipts_f:
            info = line.strip().split(",")
            emp_id = info[0]
            receipts = list(map(float, info[1:]))
            employee = find_employee_by_id(emp_id)
            if isinstance(employee.classification, Commissioned):
                for receipt in receipts:
                    employee.classification.add_receipt(receipt)


def run_payroll():
    if os.path.exists(PAY_LOGFILE):
        os.remove(PAY_LOGFILE)
    for emp in employees:
        emp.issue_payment()
