
favorite_bars = [
    'Lloyds',
    'Manuels',
    'The Imperial'
]

best_item = [
    'Cheap bourbon',  # at Lloyd's
    'The Dogzilla',   # at Manuel's
    'Best staff ever' # The Imperial
]

day_least_crowded = [
    'Tuesday',
    'Wednesday',
]

print(f"At {favorite_bars[0]} they have a good {best_item[0]}")


# Dictionaries are collections of pairs of keys and values
# Keys are strings (99% of the time)
bars = {
    'Lloyds': 'Cheap bourbon',
    'Manuels': 'The Dogzilla',
    'The Imperial': 'Best staff ever!'
}

# Use the [] to look up information by the "key"
bars['Lloyds']
#'Cheap bourbon'
bars['Manuels']

# The .get() method will not raise an Exception if it can't find the key.
bars.get('Book House')
# You can pass the .get() method a second argument. This value will be 
# returned if it can't find the key.
bars.get('Book House', 'stuff')

# How do I write useful dictionaries?
# How do I store multiple values for a single key?
bars = {
    'Lloyds': ['Cheap Bourbon', 'Tuesday']
    },{
    'Manuels': ['The Dogzilla', 'Wednesday']
}
# Values can be lists! (Or numbers, or tuples, or anything)

# How do I store more complicated data for a single key?
# Nest your dictionaries!
bars = {
    'Lloyds': {
        'item': 'Cheap Bourbon',
        'day': 'Tuesday'
    },
    'Manuels': {
        'item': 'The Dogzilla',
        'day': 'Wednesday'
    },
    'The Imperial': {
        'item': 'Philly',
        'day': ['Tuesday', 'Friday']
        # Using a list because the days don't need individual labels
    }
}

places = {
    'US': {
        'Georgia': {
            'Atlanta': {
                'work': 'DigitalCrafts',
                'cats': ['Oakley','Mill']
            },
            'Nashville': {
                'lunch': 'Hattie B'
            },
            'Savannah': {
                'coffee': 'That place that time'
            }
        },
        'Tennessee': {
            'Nashville': {
                'lunch': 'Hattie B'
            }
        }
    },
    'Europe': {
        'Germany': {
            'Berlin': {
                'lunch': 'The Reichstag'
            },
            'Munich': {
                'snack': 'Hofbrauhaus'
            }
        }
    }
}

##### How do I access information in useful dictionaries?
# How do I access nested information?
# Use square brackets side by side (as you would with nested lists).
places['US']['Georgia']['Atlanta']['work']
#  how do i caccess a list in a nested dictionary
places['US']['Georgia']['Atlanta']['cats'][0]


movies = [
    {
        'title':'avengers:end game',
        'release date':'2019'
    },
    {
        'title':'avengers:end game',
        'release date':'2018'
    }

]

movies[1]['release date']

# How do I loop through information in a dictionary?

##### How do I modify a dictionary?
favorites ={}
favorites['cat']= "Oakley"
favorites['ice cream'] ='butter Pecan'
favorites.update(cat = 'Milla')
#  to delete an item
# del favorites['ice cream'][1]
favorites['ice cream']= ''


# How do I store new values to an existing dictionary?
# How do I remove value values from an existing dictionary?
charges = [
    {
        'vender': 'kula',
        'amount': 6.36
    },
    {
        'vender': 'kula',
        'amount': 9.11
    },
    {
        'vender': 'narns and noble',
        'amount': 16.41
    },
    {
        'vender': 'kula',
        'amount': 3.99
    },
    {
        'vender': 'Lloyds',
        'amount': 50
    }
]

for  charges in charges:
    total +=charge[amount]
# total
# round(total,2)
# highest