from lib.tyre import Tyre

def test_history_updates_on_initialisation():
    tyre = Tyre('left front', '30', '25', '01/01/26')
    assert tyre.history == [
        {
            pressure: '25'
            tread: '20'
            date: '03/03/26'
        },
    ]

