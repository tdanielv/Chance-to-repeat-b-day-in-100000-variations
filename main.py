import datetime
import random

def birthdays(num_of_birthdays):
    birth_days = []
    for i in range(num_of_birthdays):
        birth_days.append(datetime.date(2001,1,1)+datetime.timedelta(random.randint(0, 364)))
    return birth_days

def get_match(birthdays):
    match = []
    if len(birthdays) == len(set(birthdays)):
        return None
    for i, birth in enumerate(birthdays):
        for i2, birth2 in enumerate(birthdays[i + 1:]):
            if birth == birth2:
                match.append(birth)

    return match

print('Birthday Paradox, by Al Sweigart al@inventwithpython.com \n The Birthday Paradox shows us that in a group of N people, the odds\nthat two of them have matching birthdays is surprisingly large.\nThis program does a Monte Carlo simulation (that is, repeated random \n simulations) to explore this concept. \nIts not actually a paradox, its just a surprising result.)')

bdays = int(input('How much birthdays do u want check?'))
birth_days = birthdays(bdays)
matches = get_match(birth_days)
m = 0

print('Here are',bdays,'birthdays:' )
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for i in range(bdays):
    if i != bdays-1:
        print(birth_days[i].day, MONTHS[birth_days[i].month-1], end=',')
    else:
        print(birth_days[i].day, MONTHS[birth_days[i].month - 1], end='.')
print('\n')

if matches is not None:
    for i in matches:
        m += 1
    print(m, 'of them are the same')
else:
    print('No repeat')


print('Generating', bdays,' birthdays 100_000 times to check')
s = 0
for i in range(100000):
    if i % 10000 == 0:
        print(i, 'times')
    birth_days = birthdays(bdays)
    if get_match(birth_days) != None:
        s += 1
print('100_000 well done')
probability = round(s / 100000 * 100, 2)
print('Out of 100,000 simulations of', bdays, 'people, there was a matching birthday in that group', s, 'times. This means')
print('that', bdays, 'people have a', probability, '% chance of having a matching birthday in their group. That\'s probably more than you would think!')
