# Python-technical-interview

FileReader is a simple class that takes in a json file and parses out employee data.

Three methods are defined:

1. **read_file()** reads the file `data.json` and converts the json object to a python Dictionary
1. **generate_new_emails()** takes in this dict and generates a list of users' emails with their domain (yahoo.com, gmail.com) replaced with the companies custom domain
1. **get_all_new_employees()** generates a list of employees who have "0" experience
1. **update_experience()** Implement this method to increment each employees experience in the employees list by one

Employee class is a simple data class to store details from each item in the `data.json` file.

Steps

1. Run tests, and fix errors
1. Add functionality to increment each employees experience by 1 year (Uncomment final test in `tests.py`)
1. Fill out the Cloudformation so that it will create an S3 bucket with the given BucketName and output that name in the outputs section.

Bonus
1. Rewrite "generate_new_emails" method to conform to python recommendations
