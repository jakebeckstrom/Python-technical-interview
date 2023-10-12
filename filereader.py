import json

class Employee:
    """Data Class to store employee details from file"""

    def __init__(self, employee):
        self.employee = employee

    @property
    def name(self):
        return self.employee.get("name", None)

    @property
    def email(self):
        return self.employee.get("email", None)

    @property
    def experience(self):
        return self.employee.get("Experience", "0")



class FileReader:

    def __init__(self, filename):
        self.filename = filename
        data = self.read_file()
        self.employees = [Employee(i) for i in data["Employees"]]


    def read_file():
        """Open the file and read contents into a dictionary"""
        with open(self.filename, 'r') as file:
            data = json.load(file)
        return data


    def update_experience(self):
        """Add one to each employees experience."""
        pass


    def generate_new_emails(self, data):
        """
            Return a list of emails with the new company domain

            mysupercoolemail@gmail.com --> mysupercoolemail@supercoolcompeny.com
        """
        employees = data["Employees"]
        new_emails = []

        for i in range(0, len(employees)):
            email = employees[i].get("Email") # Get email
            email.split('@')[0] # Split the string and keep the part before '@'
            new_emails.append(email + "@supercoolcompany.com") # Concat first part with custom domain and replace email

        return new_emails


    def get_all_new_employees(self, data):
        """Get a list of all employees with 0 years of experience, if there is no experience field, assume 0"""
        return [i for i in data["Employees"] if i["Experience"] == "0"]
        
