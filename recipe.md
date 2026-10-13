# Car Class System Design Recipe

## 1. Describe the Problem

As a car owner
So that I can keep a record of details about my tyres
I want to keep track of the tyres individually, by their position on my car. -------

As a car owner
So that I have the two important pieces of data for a tyre
I want to be able to record both tyre pressure and tyre tread depth.      --------

As a car owner
So that I have a history of tyre readings
I want to be able to keep a record of historical readings, when those were, as well as current readings.  ------- 

As a car owner
So that I can see the details of my car at a glance
I want to list the tyres' positions, latest readings and when those were.  ---------


car class:
- list of tyres = []

+ add_tyre()
+ add_readings() ->
            for tyre in car.list_of_tyres:
                 tyre.addreading(30, 25, date)

+ list_tyre_pos_and_readings()


tyre class:
- pressure
- tread depth
- position = for example left_front, right_front, rear etc
- history

+ current -> history[-1]
+ add_reading()

tyre.history = [
    {
        pressure: string
        tread: string
        date: string

    },
    {
        pressure: string
        tread: string
        date: string
    },
]


for tyre in car.list_of_tyres:
    tyre.addreading(30, 25, date)
tyre.add_reading




## 2. Design the Class System

```python
class Car:
    # User-facing properties:
    #   list_of_tyres: list of instances of Tyres

    def __init__(self):
        list_of_tyres = []

    def add_tyre(self, tyre):
        # Parameters:
        #   tyre: an instance of Tyre
        # Side-effects:
        #   Adds the tyre to the list of tyres
        pass # No code here yet

    def list_tyre_pos_and_readings(self):
        # Parameters:
        #   None
        # Returns:
        #    A text with position of tyre and their info
        pass # No code here yet


class Tyre:
    # User-facing properties:
    #   position: string
    #   pressure: string
    #   tread: string
    #   date: string
    #   history: []

    def __init__(self, position, pressure, tread, date):
        # Parameters:
        #   position: string
        #   pressure: string
        #   tread: string
        #   date: string
        #   history: []
        # Side-effects:
        #   Updates history list with its initialising reading
        pass # No code here yet

    def add_reading(self, pressure, tread, date):
        # Parameters:
        #   pressure: string
        #   tread: string
        #   date: string
        # Returns:
        #   Nothing
        # Side-effects:
        #   Updates history list with its new reading and its pressure, tread, and date attributes
        pass # No code here yet

```

## 3. Create Examples as Integration Tests

```python

"""
integration test to see if tyres can be add
if tyres can hold history
"""
car = Car()
left_front_tyre = Tyre('left front', '30', '25', '01/01/26')
right_front_tyre = Tyre('right front', '33', '27', '01/01/26')
car.add_tyre(left_front_tyre)
car.add_tyre(right_front_tyre)
car.list_of_tyres => [left_front_tyre, right_front_tyre]


"""
given car has tyres with history
can it be viewed
"""
car = Car()
left_front_tyre = Tyre('left front', '30', '25', '01/01/26')
right_front_tyre = Tyre('right front', '33', '27', '01/01/26')
car.add_tyre(left_front_tyre)
car.add_tyre(right_front_tyre)

left_front_tyre.add_reading('25', '20', '03/03/26')
car.list_tyre_pos_and_readings() => 
f'{position} = {recent_results}'

```

## 4. Create Examples as Unit Tests

```python

"""
Given a pressure and tread and date
add_reading adds those new readings to the relevant tyre
"""
tyre = Tyre('left front', '30', '25', '01/01/26')
tyre.history => [
    {
        pressure: '25'
        tread: '20'
        date: '03/03/26'
    },
]

"""
Given a history of readings is recorded on a Tyre
I want to see the history
"""
tyre = Tyre('left front', '30', '25', '01/01/26')
tyre.add_reading('25', '20', '03/03/26')
tyre.history => [
    {
        pressure: '30'
        tread: '25'
        date: '01/01/26'

    },
    {
        pressure: '25'
        tread: '20'
        date: '03/03/26'
    },
]
```
