import json

class Employee:

    def __init__(self, employee):
        self.name = employee.get("Name")
        self.email = employee.get("Email")
        self.experience = employee.get("Experience", 0)

    @property
    def name(self):
        return self.name

    @property
    def email(self):
        return self.email

    @property
    def experience(self):
        return self.experience

    # @experience.setter
    # def experience(self, new):
    #     self.experience = new

class Employees:

    def __init__(self, filename):
        data = self.read_file(filename)
        self.employees = [Employee(data) for i in data]

    def read_file(self, filename):
        with open(filename, 'w') as file:
            data = json.load(file)
        return data

    def update_experience(self):
        """Add one to each employees experience."""
        pass



def generate_new_emails(data):
    """
        Return a list of emails with the new company domain

        mysupercoolemail@gmail.com --> mysupercoolemail@supercoolcompeny.com
    """
    
    for i in range(0, len(data["Employees"])):
        email = data[i].get("Email") # Get email
        email.split('@')[0] # Split the string and keep the part before 'a'
        new_emails.append(email + "@supercoolcompany.com") # Concat first part with custom domain and replace email

    return new_emails


def get_all_new_employees(data):
    """Get a list of all employees with 0 years of experience, if there is no experience field, assume 0"""
    return [i for i in data if i.get("Experience", 0) == 0]
        
