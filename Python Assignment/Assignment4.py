########################### Assissment#######################
 # 2.Get the input from user 1.number of users 2.create a list or dict to store the number of dept.3.use for loop to
# get the dept information(every dept add to list or dict)  4.search department by dept id
#5.Add a function to serach department by name
class Department:
    def _init_(self, ID, name, location, head_of_department):
        self.ID = ID    
        self.name = name
        self.location = location
        self.head_of_department = head_of_department

    def display_department_info(self):
        print("\nDepartment Information:")
        print("------------------------------------------")
        print(f"Department ID: {self.ID}")
        print(f"Department Name: {self.name}")
        print(f"Department Location: {self.location}")
        print(f"Head of the Department: {self.head_of_department}")


no_of_departments = int(input("Enter the number of departments: "))

# Dictionary to store department objects using ID as key
departments = {}

# Input department details
for i in range(no_of_departments):
    print(f"\nEnter details for department {i+1}:")
    ID = input("Enter Department ID: ")
    name = input("Enter Department Name: ")
    location = input("Enter Department Location: ")
    head_of_department = input("Enter Head of Department: ") 
    department_instance = Department(ID, name, location, head_of_department)
    departments[ID] = department_instance


def search_by_id():
    dept_id = input("\nEnter Department ID to search: ")
    dept = departments.get(dept_id)
    if dept:
        dept.display_department_info()
    else:
        print("Department with the given ID is not available.")


def search_by_name():
    dept_name = input("\nEnter Department Name to search: ")
    found = False
    for dept in departments.values():
        if dept.name.lower() == dept_name.lower():
            dept.display_department_info()
            found = True
    if not found:
        print("Department with the given name is not available.")

# Call search functions
search_by_id()
search_by_name()