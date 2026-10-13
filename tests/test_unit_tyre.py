from lib.tyre import Tyre

def test_history_updates_on_initialisation():
    tyre = Tyre('left front', '30', '25', '01/01/26')
    assert tyre.history == [
        {
            'pressure': '30',
            'tread': '25',
            'date': '01/01/26',
        },
    ]

def test_add_reading_ipdates_history():
    tyre = Tyre('left front', '30', '25', '01/01/26')
    tyre.add_reading('25', '20', '03/03/26')
    assert tyre.history == [
        {
            'pressure': '30',
            'tread': '25',
            'date': '01/01/26',

        },
        {
            'pressure': '25',
            'tread': '20',
            'date': '03/03/26',
        },
    ]

