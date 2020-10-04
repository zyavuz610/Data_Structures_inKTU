# 1. whitespace is important in Python, code indention is made by whitespace
# 2. new_line character is the end of statement
# 3. # chararacter is for comment 
# 4. if a line continues to next line, \ char is used
# 5. if an opening delimiter has not yet been closed, such as the { character in deﬁning value map
# 6. case sensitive

print('Welcome to the GPA calculator.')
print('Please enter all your letter grades, one per line.')
print('Enter a blank line to designate the end.')
# map from letter grade to point value
points = {'AA', 'BA', 'BB', 'CB', 'CC', 'DC', 'DD', 'FD', 'FF'}
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
    if grade == 'AA':
        total_points += 4.0
    elif grade == 'BA':
        total_points += 3.5
    elif grade == 'BB':
        total_points += 3.0
    elif grade == 'CB':
        total_points += 2.5
    elif grade == 'CC':
        total_points += 2.0
    elif grade == 'DC':
        total_points += 1.5
    elif grade == 'DD':
        total_points += 1.0
    elif grade == 'FD':
        total_points += 0.5
    else:
        total_points += 0.0
if num_courses > 0:                        # avoid division by zero
  print('Your GPA is {0:.3}'.format(total_points / num_courses))
