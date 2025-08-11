#Arithmetic Progression while

term = int(input('Enter the term:\n'))
ratio = int(input('Enter the ratio:\n'))

counter = 1

progression = term

term_count = 9

more_terms = 9
total = 0

print(f'Term: {term}, Ratio: {ratio}\n')

print(f'{term}'+'=' f'{term}')



while more_terms != 0:
	total += more_terms
	while counter <= total:
		print(f'{term} + {ratio}'+'=' f'{term+ratio}')
		term=term+ratio
		counter+=1
		progression=progression+term

	more_terms=int(input('how many more terms do you want to show?\n'))


print(f'The sum of the terms is: {progression}')
	
	
	
	
	
	
	
	