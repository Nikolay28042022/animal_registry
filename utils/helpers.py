import datetime

def parse_birth_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Неверный формат даты. Используйте YYYY-MM-DD.")
        return None
