fo=open('test.txt','w')
print('Name: ',fo.closed)
print('Is closed :',fo.closed)
print('Opening Mode :',fo.mode )
fo.write('I like python')
fo.write('and beer')
fo.close()

fo=open('test.txt','a')
fo.write('I like python')
fo.write('and beer')
fo.close()