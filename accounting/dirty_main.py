from datetime import *
from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    current_date = date.today()
    print(f"Current date: {current_date}")

    calculate_salary()
    get_employees()
