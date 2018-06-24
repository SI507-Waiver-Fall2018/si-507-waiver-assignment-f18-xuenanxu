# Name: Xuenan Xu
# uniqname: xuenanxu
# UMID: 35069066

# these should be the only imports you need
import sys
import sqlite3

# write your code here
# usage should be 
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>

#input
request = sys.argv[1]

#connecting to the database file
conn = sqlite3.connect('Northwind_small.sqlite')
c = conn.cursor()



#python part2.py customers
if (request == "customers"):
	cursor_customers = c.execute('SELECT Id, CompanyName from Customer')
	print("ID" + "   " + "Customer Name")
	for row in cursor_customers:
		print(*row, sep = "   ")


#python part2.py employees
if(request == "employees"):
	cursor_employees = c.execute('SELECT Id, LastName, FirstName from Employee')
	print("Employee Name")
	for row in cursor_employees:
		print(*row)

#python part3.py orders cust=<customer id>
if (request == 'orders' and 'cust' in sys.argv[2]):
    customerId = sys.argv[2].replace("cust=", "")
    cursor_order_customer = c.execute('SELECT o.OrderDate FROM "Order" o WHERE o.CustomerId = ?', [customerId])
    print("Order Dates for All Orders Placed for Customer", customerId)
    for row in cursor_order_customer:
        print (*row, sep='\n')


#python part3.py orders emp=<employee last name>
if (request == 'orders' and 'emp' in sys.argv[2]):
    empLastname = sys.argv[2].replace("emp=", "")
    cursor_employeename = c.execute('SELECT OrderDate FROM "Order" o JOIN Employee e ON o.employeeId = e.Id WHERE e.LastName = ?', [empLastname])
    print("Order Dates for All Orders Managed by Employee", empLastname)
    for row in cursor_employeename:
        print (*row, sep='\n')

conn.close()


