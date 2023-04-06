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
Artem = Developer("Artem", "Moskalenko", 700, 1)
Walter = Developer("Walter ", "White", 1500, 2)
John = Developer("John", "Snow", 2500, 3)
Rick = Designer("Rick", "Grimes", 500, 1, 0.7)
Carlo = Manager("Carlo", "Ancelotti", 4500, 4, [Artem, Walter, John, Rick])

# Другий менеджер та його команда
Jurgen = Developer("Jurgen ", "Klopp", 4100, 4)
Jose = Developer("Jose ", "Mourinho", 4500, 5)
Stefano = Designer("Stefano", "Pioli", 2100, 3, 0.9)
Julian = Designer("Julian", "Nagelsmann", 600, 1, 0.8)
Luciano = Designer("Luciano", "Spalletti", 5000, 8, 1)
Antonio = Designer("Antonio", "Conte", 3500, 6, 0.6)
Mikel = Manager("Mikel", "Arteta", 1500, 4, [Jurgen, Jose, Stefano, Julian, Luciano, Antonio])

dep = Department([Carlo, Mikel])
dep.give_salary()

