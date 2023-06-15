from utils import get_data, formatted_data, filter_data, get_last_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_filter_data(test_data):
    assert filter_data(test_data) == [(
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }
    )]


def test_get_last_data(test_data):
    data = get_last_data(test_data, 1)
    assert [x['date'] for x in data] == ['2018-09-12T21:27:25.241689']


def test_formatted_data(test_data):
    data = formatted_data([test_data[0]])
    assert data == ['        23.03.2018 Открытие вклада\n'
                    '         -> Счет**2431\n'
                    '        48223.05 руб.']
