STATES_CAPITALS = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas': 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Indiana' : 'Indianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismarck',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne',
}

# adds the city idaho 
def capital_of_Idaho(STATES_CAPITALS):
    print(STATES_CAPITALS["Idaho"])
# prints all the states in the dict
def states_capitals_string(STATES_CAPITALS):
    for i in STATES_CAPITALS:
        print(i)
# prints all the cities in the dict 
def all_capitals(STATES_CAPITALS):
    for i in STATES_CAPITALS:
        print(STATES_CAPITALS[i])
# prints the items in dict in the above order using the above format
def state_capital(STATES_CAPITALS):
    for i in STATES_CAPITALS:
        print(f'{i} -> {STATES_CAPITALS[i]}', end=' , ')
# prints the items in dict in the above order using the above format in sorted order
def state_capital_sorted(STATES_CAPITALS):
    sorted_states = sorted(STATES_CAPITALS.items())
    for i in sorted_states:
        print(f'{i[0]} -> {i[1]}', end=' , ')
# function that asks the user for input of a city the function scans the dictionary items and returns the value of the key 
# Also there is an if condition that checks for duplicates and if there is a duplicate prints an error 
def reverse(STATES_CAPITALS):
    city=input('enter the city:')
    counter=0
    for key,value in STATES_CAPITALS.items():
        if value == city:
            counter+=1
            state=key
    if counter > 1:
        print('Error - more than one state with the same capital')
    elif counter==1:
                print(f'The state of {city} is',state)

# 
capital_of_Idaho(STATES_CAPITALS)
print()
states_capitals_string(STATES_CAPITALS)
print()
all_capitals(STATES_CAPITALS)
print()
state_capital(STATES_CAPITALS)
print()
state_capital_sorted(STATES_CAPITALS)
print()
reverse(STATES_CAPITALS)
