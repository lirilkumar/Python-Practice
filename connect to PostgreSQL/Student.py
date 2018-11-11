import psycopg2
class Student:
    def __init__(self):
        try:
            self.connection=psycopg2.connect(
                "dbname='school' user='postgres' host='localhost' password='123123123' port='5432'")

            self.connection.autocommit=True
            self.cursor=self.connection.cursor()
            print('Connected !!')
        except Exception as e:
            print('Error while connecting')
            print(e.__str__())


    def createTable(self):
        try:
            drop_table="DROP TABLE class_10a;"
            self.cursor.execute(drop_table)
            create_table_query="Create table class_10A(id serial primary key, name varchar(100), age int not null)"
            self.cursor.execute(create_table_query)
            print('table created')
        except Exception as e:
            print(e.__str__())

    def insert(self):
        try:
            insert_table_query="insert into class_10A(name,age) values('Liril','25')"
            self.cursor.execute(insert_table_query)
            print('record inserted')
        except Exception as e:
            print(e.__str__())

    def retrive(self):
        try:
            self.cursor.execute('select * from class_10A')
            students=self.cursor.fetchall()
            for student in students:
                print(student[1])
                print('record : {0}'.format(student))
        except Exception as e:
            print(e.__str__())

s=Student()
s.createTable()
s.insert()
s.retrive()
try:
    raise Exception("a")
except:
    import traceback
    print(traceback.print_stack())


