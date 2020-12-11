from application.db.people import get_employes
from application.salary import calculate_salary
from datetime import datetime

if __name__ == '__main__':
    now = datetime.now()
    print(f'Сегодня {now.strftime("%d-%m-%Y")}')
    get_employes()
    calculate_salary()
    
