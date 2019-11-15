

#  Nested Dictionaries
ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies','tennis'],
    'friends':[
        {
        'name':'Jasmine',
        'email':'jasmine@yahoo.com',
        'interests':['photography','tennis']
        },
        {
            'name': 'Jan',
            'email' : 'jan@hotmail.com',
            'interest' : ['movies','tv']
        }
    ]
}
#  print ramit email
print(ramit['email'])
#  print ramit first interest
print(ramit['interests'][0])
#  print jasmine email
print(ramit['friends'][0]['email'])
# print jan second interest
print(ramit['friends'][1]['interest'][1])