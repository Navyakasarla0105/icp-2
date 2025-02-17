# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Lq3liERqm8nBZv6xkXXPJQx3hTtZf09F

Kasarla Navya - 700766043
ICP-2 (01/21/25)
"""



"""**Create a class Employee and then do the following**
 Create a data member to count the number of Employees
* Create a constructor to initialize name, family, salary, department
* Create a function to average salary
* Create a Fulltime Employee class and it should inherit the properties of Employee class
*  Create the instances of Fulltime Employee class and Employee class and call their member functions.
"""

# Employee Class creation
class Employee():
    # create data members to track count of employee and list of salaries
    emp_count = 0
    # constructor for initializing the variables
    def __init__(self,name,family,salary,department):
        self.name = name,
        self.family = family,
        self.salary = salary,
        self.department = department,
        Employee.emp_count += 1

    # function to return average of salary
    def avg_salary(employees:list):
        salaries_list = [emp.salary[0] for emp in employees] # method 1 : generic
        # print(emp.salary[0] for emp in employees)
        avg_sal = sum(salaries_list)/Employee.emp_count      # method 2 : using numpy
        # avg_sal = np.mean(salaries_list)
        return avg_sal

# create FullTimeEmployee class and inherit the properties from Employee class
class FullTimeEmployee(Employee):
    def __init__(self,name,family,salary,department):
        # calling parent class constructor
        super().__init__(name,family,salary,department)

employees = []
employees.append(Employee("Navya","Reddy",300000,"Finance"))
employees.append(Employee("Krishna","Kanth",10000,"Artificial Intelligence"))
employees.append(FullTimeEmployee("kavya","Vuragayala",600000,"Marketing"))
employees.append(FullTimeEmployee("Nandu","Prasad",700000,"Data Science"))


print("Output using employee class : ",  Employee.avg_salary(employees))
print("Output using fulltime employee class : ",FullTimeEmployee.avg_salary(employees))

"""Using NumPy create random vector of size 20 having only float in the range 1-20.

Then reshape the array to 4 by 5
Then replace the max in each row by 0 (axis=1)
"""

import numpy as np
#generating a vector
vector = np.random.uniform(1, 20, 20)

#reshaping the vector into 4 * 5 matrix
matrix = vector.reshape(4, 5)

print("Original Matrix: \n",matrix)

#finding the index of the max element along axis = 1
indices = np.argmax(matrix, axis=1)

#Create a range of indices for each row
row_indices = np.arange(matrix.shape[0])

#Use advanced indexing to replace max values with 0
matrix[row_indices, indices] = 0

print("Resultant Matrix: \n",matrix)