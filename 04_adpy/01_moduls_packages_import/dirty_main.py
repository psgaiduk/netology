from application.db.people import *
from application.salary import *
from datetime import *

if __name__ == '__main__':
    now = datetime.now()
    print(f'Сегодня {now.strftime("%d-%m-%Y")}')
    get_employes()
    calculate_salary()
    
