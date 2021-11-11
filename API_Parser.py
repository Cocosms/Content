import os
import time
import Postgre_con

connection = Postgre_con.db_connection("user_info", "remote", "1Q@w3E$r", "127.0.0.1", "5432")
cursor = connection.cursor()
cursor.execute("SELECT username,salary,location,other_income from user_information")
info_get = cursor.fetchall()
info_get_parsed = str(info_get[0]).strip("()").split(",")
get_username = str(info_get_parsed[0]).strip("'")
get_location = str(info_get_parsed[2]).strip(" '")
get_salary = str(info_get_parsed[1]).strip(" '")
get_oth_inc = str(info_get_parsed[3]).strip(" '")
cursor.close()
print(info_get_parsed)
print('Content-type: text/html\n')
print("<td>{}</td>".format(get_username))
print("<td>{}</td>".format(get_location))
print("<td>{}</td>".format(get_salary))
print("<td>{}</td>".format(get_oth_inc))
