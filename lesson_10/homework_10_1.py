class Employee:
    def __init__(self, name, salary, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department


class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language
        )
        self.team_size = team_size


team_lead = TeamLead(name="Oleksandr", salary=5000, department="IT", programming_language="Python", team_size=8)

print(team_lead.name)
print(team_lead.salary)
print(team_lead.department)
print(team_lead.programming_language)
print(team_lead.team_size)