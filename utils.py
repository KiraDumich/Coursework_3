import json
from datetime import datetime


def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def filter_data(data):
    data = [i for i in data if 'state' in i and i['state'] == 'EXECUTED']
    return data


def get_last_data(data, count):
    data = sorted(data, key=lambda i: i['date'], reverse=True)
    data = data[:count]
    return data


def formatted_data(data):
    format_data = []
    for row in data:
        date = datetime.strptime(row['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row['description']
        recipent = f'{row["to"].split()[0]}**{row["to"][-4:]}'
        operations_amount = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["name"]}'
        if 'from' in row:
            if row['from'][:4] == 'Счёт':
                from_bill = row['from'].split()
                name = from_bill[0]
                number = f'**{from_bill[1][-4]}'
                sender_info = f'{name} {number}'
            elif row['from'][:4] == 'Visa':
                from_card = row['from'].split()
                name = from_card[0] + from_card[1]
                number = f'{from_card[2][0:6]}******{from_card[2][12:16]}'
                sender_info = f'{name} {number}'
        else:
            sender_info = ''
        format_data.append(f"""\
        {date} {description}
        {sender_info} -> {recipent}
        {operations_amount}""")
    return format_data

