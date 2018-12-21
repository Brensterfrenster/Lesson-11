print('-'*80)
print()
name = input('Student Name: ')

grade = input('Grade: ')
grade = int(grade)

narrative = input('Narrative: ')
narrative = input('Skye, your final grade in AP Computer Science is 94%.')
if grade >= 65:
	print('You have excelled in all components of the class!')
	print('I wish you continued success in the next semester of AP Computer Science!')
else:
	print('This largely a result of missing projects and homework assignments.')
	print('Unfortunately, because this grade is less than a 65, you will have to complete an MBA assignemnt next semester.')