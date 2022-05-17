with open("employees.txt", mode="rt") as employees:
    for employee in employees:
        iban, fullname, salary = employee.split(",")
        print(f"{iban}\t{fullname}\t{salary}")
