SQL = 'sql_server'

SQL_CONNSTRA = (
    'DRIVER={SQL Server};'
    'SERVER=mhknbn2kdz.database.windows.net;'
    'DATABASE=AdventureWorks2012;'
    'UID=sqlfamily;PWD=sqlf@m1ly'
)


SQL_QUERY = '''
    SELECT DISTINCT TOP 5 FirstName, LastName 
    FROM Person.Person
    ORDER BY LastName, FirstName;
'''


ORACLE= 'oracle_server'