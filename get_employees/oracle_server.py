import pyodbc
from .abs_facade import AbsFacade
from . import SQL_CONNSTRA, SQL_QUERY


class GetEmployees(AbsFacade):
    def get_employees(self):
        print("List of students")