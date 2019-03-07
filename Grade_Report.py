# Benjamin Readman
# Grade_Report
grade_report = {}
cont = 'y'
while cont == 'y':
    choice = input("Would you like to:\n1) Add a student\n2) View students in grade report\n3) View a student's grade\n4) Delete a student from the list\n5) Add a grade to a students list\n6) Save the grade report\n")
    if choice == '1':
        name = input("Please enter the students name: ")
        grade_report[name] = ''
    elif choice == '2':
        print("These are the students in the grade report: ")
        print(grade_report.keys())
    elif choice == '3':
    elif choice == '4':
    elif choice == '5':
    elif choice == '6':
    cont = input("Would you like to continue editing the grade report(y/n)? ")
    