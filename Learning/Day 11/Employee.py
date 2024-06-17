import csv
import matplotlib.pyplot as plt

def read_data(filename):
    try:
        with open(filename, "r") as fp:
            data = []
            reader = csv.DictReader(fp)
            for row in reader:
                data.append(row)
            return data
    except FileNotFoundError:
        print("Please check the path")
        return None
    
def display_menu(): 
    print("\nWelcome to the Data Analysis Tool")
    print("1. Display data summary")
    print("2. Calculate statistics")
    print("3. Filter data")
    print("4. Generate report")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    return choice

def main():
    filename = "employee_data.csv"
    data = read_data(filename)
    
    if not data:
        return

    while True:
        choice  = display_menu()

        if choice == '1':
            print("Details of an employee")
            display_summary(data)
        elif choice == '2':
            print("Calculating Statistics")
            cal_statistics(data)
        elif choice == '3':
            print("Perform filetering or sorting")
            filtered_data = filter_data(data)
            display_filtered_data(filtered_data)        
        elif choice == '4':
            print("Create reports for better visualiztion")
            generate_report(data)
        elif choice == '5':
            print("Exit the program")
            exit()
        else: 
            print("Invalid choice. Please try again.")


def display_summary(data):
        for d in data:
            print(d)

def filter_data(data):
    filtered_data = []
    criteria = input("Enter filter criteria (e.g., Hire Date):").strip().title() 
    filter_value = input("Enter the {} value to filter by:".format(criteria)).strip()
    for item in data:
        if criteria in item.keys() and item[criteria].lower() == filter_value.lower():
            filtered_data.append(item)
    return filtered_data

def display_filtered_data(filter_data):
    if filter_data:
     print("\nFiltered Data")
     for item in filter_data:
        print(item)


def cal_statistics(data):
    salaries = []
    for emp in data:
        if 'Salary' in emp:
            salaries.append(int(emp['Salary']))
    if salaries: 
        avg_salary = sum(salaries)/len(salaries)
        print(f"Average Salary: ${avg_salary:.2f}")
    else:
        print("No salary data available.")


def generate_report(data):
    salary = []
    total_employees = len(data)
    for employee in data:
        if 'Salary' in employee:
            salary.append(int(employee['Salary']))
            avg_salary = sum(salary)/len(salary)
            highest_salary = max(salary)
            lowest_salary = min(salary)

    deparatment_counts = {}
    for emp in data:
        if 'Department' in emp:
            department = emp['Department']
            if department in deparatment_counts:
                deparatment_counts[department]+=1
            else:
                deparatment_counts[department] = 1
    print("\nEmployee Data Report:")
    print(f"Total number of employees: {total_employees}")
    print(f"Average salary: ${avg_salary:.2f}")
    print(f"Highest salary: ${highest_salary}")
    print(f"Lowest salary: ${lowest_salary}")
    print("Department-wise employee count:")
    

    for deparatment, count in deparatment_counts.items():
                print(f"- {department}: {count}")
 
    
if __name__== "__main__":
    main()



