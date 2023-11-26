from persistence import *

def main():

    printActivities()
    printBranches()
    printEmployees() #order by Name, Salary, Working location, total sales income.
    printProducts()
    printSuppliers() 
    print("")
    printEmployeesReport()
    print("")
    printActivitiesReport()




def printActivities():
    print("Activities")

    x = repo.execute_command(""" SELECT * FROM Activities
    ORDER BY date;
    """)
    for i in x:
        print (i)
    


    

def printBranches():
    print("Branches")
    x = repo.execute_command(""" SELECT * FROM branches
    ORDER BY id;
    """)
    for i in x:
        print (i)

   

def printEmployees():
    print("Employees")
    x = repo.execute_command(""" SELECT * FROM employees
    ORDER BY id
    """)
    for i in x:
        print (i)



def printProducts():
    print("Products")
    x = repo.execute_command(""" SELECT * FROM products
    ORDER BY id;
    """)
    for i in x:
        print (i)


def printSuppliers():
    print("Suppliers")
    x = repo.execute_command(""" SELECT * FROM suppliers
    ORDER BY id;
    """)
    for i in x:
        print (i)


def printActivitiesReport():
    print("ActivitiesReport")

    y = repo.execute_command(""" SELECT activities.date, products.description, activities.quantity, activities.activator_id 
    FROM activities JOIN products
    ON activities.product_id = products.id
    ORDER BY date;
    """)
    for i in range(len(y)):
        if y[i][2] >0:
            supplierOrm = repo.suppliers.find(id = y[i][3])
            name = supplierOrm[0].name
            x = (y[i][0],y[i][1],y[i][2],None,name)
            

        else:
            employeeOrm = repo.employees.find(id = y[i][3])
            name = employeeOrm[0].name
            x = (y[i][0],y[i][1],y[i][2],name,None)

        print(x)        

def printEmployeesReport():
    print("EmployeesReport")
   
    x = repo.execute_command(""" SELECT * FROM employees
    ORDER BY name
    """)
    #go over each employee from the activities 
    for i in range (len(x)):
        activitiesOrm = repo.activities.find(activator_id = x[i][0])
        branchesOrm = repo.branches.find(id = x[i][3])
        branche = branchesOrm[0].location
        sum = 0
        #go over eaech sel
        for j in range (len(activitiesOrm)):
            ProductId = activitiesOrm[j].product_id
            quantity = activitiesOrm[j].quantity
            
            productOrm = repo.products.find(id = ProductId)
            price = productOrm[0].price
            sum = sum + (price *  quantity*-1) 
             
        print(x[i][1] + " " + str(x[i][2]) + " " + branche + " " + str(sum))   

                

        

if __name__ == '__main__':
    main()