greeting = 'Hello'
name = 'Michael'

print('Concatenating strings with plus sign...\n')
message = greeting + ', ' + name + '. Welcome!'
print('   ', message)

print('\nUsing a str-type "format" class method...\n')
message2 = '{}, {}. Welcome!'.format(greeting, name)
print('   ', message2)

print('\nUsing formatter "f" on Python 3, not available on Python 2...\n')
message3 = f'{greeting}, {name}. Welcome!'
print('   ', message3)

print('\nConverting a string to upper case...\n')
message4 = f'{greeting}, {name.upper()}. Welcome!'
print('   ', message4)

# find class methods and detail description of a method
print('\nInquiring all class methods of a str-type variable "name":', name, '\n', dir(name))
print('\nInquiring a class description, "str.lower()":\n')
help(str.lower)

