from model.dictinory import init_dictionary
import pypyodbc

connection = pypyodbc.connect("""Driver={SQL Server};
                           Server=172.16.10.45;
                           Database=yogesh;
                           uid=talend2019;
                           pwd=Mouri@123;""")


def sys_name(info):
    sys_info = init_dictionary()
    if info == "allinfo":
        return sys_info
    else:
        return sys_info[info], info


def database_check(uname, password):

    cursor = connection.cursor()
    cursor.execute("select * from login_validation where Name='" +
                   uname+"' and Password='"+password+"'")
    data = cursor.fetchone()
    if data:
        return 1
    else:
        return 0


def insert_data(uname, password, age, gender):

    cursor = connection.cursor()
    cursor.execute("insert into login_validation(Name,Password,Age,Gender) values('" +
                   uname+"','"+password+"',"+str(age)+",'"+gender+"')")
    cursor.commit()
    cursor.execute("select * from login_validation where Name='" + uname+"'")
    data = cursor.fetchone()
    if data:
        return 1
    else:
        return 0

