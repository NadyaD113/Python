class Employee:
    def __init__(self, first_name, second_name, base_salary, experience):
        self.first_name = first_name
        self.second_name = second_name
        self.base_salary = base_salary
        self.experience = experience
        self.countedSalary = base_salary

        if self.experience > 5:
            self.countedSalary = 1.2 * self.countedSalary + 500
        elif self.experience > 2:
            self.countedSalary += 200


class Developer(Employee):
    def __init__(self, first_name, second_name, base_salary, experience):
        super().__init__(first_name, second_name, base_salary, experience)


class Designer(Employee):
    def __init__(self, first_name, second_name, base_salary, experience, coefficient):
        super().__init__(first_name, second_name, base_salary, experience)
        self.coefficient = coefficient
        self.countedSalary = int(self.coefficient * self.countedSalary)


class Manager(Employee):
    def __init__(self, first_name, second_name, base_salary, experience, team):
        super().__init__(first_name, second_name, base_salary, experience)
        self.team = team

        if len(self.team) > 10:
            self.countedSalary += 300
        elif len(self.team) > 5:
            self.countedSalary += 200

        developers = len([employee for employee in self.team if isinstance(employee, Developer)])
        if developers > (len(self.team) / 2):
            self.countedSalary = int(1.1 * self.countedSalary)


class Department:
    def __init__(self, managers):
        self.managers = managers

    def give_salary(self):
        output = ""
        for manager in self.managers:
            output += f"{manager.first_name} {manager.second_name} отримав {manager.countedSalary} шекєлей\n"
            for employee in manager.team:
                output += f"{employee.first_name} {employee.second_name} отримав {employee.countedSalary} шекєлей\n"
        print(output)


# Перший менеджер та його команда
Nadiia = Developer("Nadiia", "Denyshchych", 850, 1.5)
Raven = Developer("Raven ", "Burgess", 2608, 4)
Robert = Developer("Robert", "Harris", 250, 5)
Sabrina = Designer("Sabrina", "Hooper", 5899, 5, 0.6)
Lori = Manager("Lori", "Wagner", 4010, 4, [Nadiia, Raven, Robert, Sabrina])

# Другий менеджер та його команда
Cheryl = Developer("Cheryl ", "Mills", 5557, 4)
Jessica = Developer("Jessica ", "Lopez", 5404, 4)
Amanda = Designer("Amanda", "Parks", 2780, 7, 0.6)
Dawn = Designer("Dawn", "Taylor", 3820, 8, 0.4)
Lisa = Designer("Lisa", "Patterson", 781, 10, 1)
Christopher = Designer("Christopher", "Davila", 1193, 1, 0.9)
Steven = Manager("Steven", "Tucker", 750, 2, [Cheryl, Jessica, Amanda, Dawn, Lisa, Christopher])

dep = Department([Lori, Steven])
dep.give_salary()

