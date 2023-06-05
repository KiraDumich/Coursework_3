from utils import get_data, filter_data, formatted_data, get_last_data


def main():
    count = 5
    data = get_data()

    data = filter_data(data)
    data = get_last_data(data, count=count)
    data = formatted_data(data)
    print('INFO: Вывод транзакций...')
    for row in data:
        print(row, end='\n\n')


if __name__ == "__main__":
    main()
