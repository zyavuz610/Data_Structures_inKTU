# cf1.1

print('Welcome to the GPA calculator.')
print('Please enter all your letter grades, one per line.')
print('Enter a blank line to designate the end.')
# map from letter grade to point value
points = {'AA':4.0, 'BA':3.5, 'BB':3.0, 'CB':2.5, 'CC':2.0, 'DC':1.5, 
          'DD':1.0, 'FD':0.5, 'FF':0.0}
num_courses     = 0
total_points    = 0
done = False
while not done:
  grade = input()                          # read line from user
  if grade == '':                          # empty line was entered
    done = True
  elif grade not in points:                # unrecognized grade entered
    print("Unknown grade '{0}' being ignored".format(grade))
  else:
    num_courses += 1
    total_points += points[grade]
if num_courses > 0:                        # avoid division by zero
  print('Your GPA is {0:.3}'.format(total_points / num_courses))
