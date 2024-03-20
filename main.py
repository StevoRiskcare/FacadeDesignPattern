from get_employees import SQL
from get_employees import ORACLE
from get_employees.facade_factory import FacadeFactory


def main():
    for dbase in SQL, ORACLE:
        factory = FacadeFactory.create_facde(dbase)
        factory.get_employees()




if __name__ == '__main__':
    main()
