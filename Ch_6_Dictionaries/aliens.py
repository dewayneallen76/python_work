# Sometimes you'll want to store multiple dictionaries in a list, or a list of items as a value
# in a dictionary. This is called nesting. 

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# A more realistic example would involve more than three aliens with code that automatically generates
# each alien. In the following example, we use range() to create a fleet of 30 aliens
alien_fleet = []

# Make 30 green aliens:
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    alien_fleet.append(new_alien)
# Show the first 5 aliens
for alien in alien_fleet[:5]:
    print(alien)
print('...')
# Show how many aliens have been created
print(f"Total number of aliens: {len(alien_fleet)}")