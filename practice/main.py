
'''Read'''
file = open('my_file.txt')
contents = file.read()
print(contents)
file.close()


# or


with open('my_file.txt') as file:
    contents = file.read()
    print(contents)


'''Write'''
with open('my_file.txt', mode='w') as file:
    file.write('New content written...blah blah blah. ')

'''Append'''
with open('my_file.txt', mode='a') as file:
    file.write('Append to end of text')

'''Create file'''
with open('new_file.txt', mode='w') as file:
    file.write('New file created. ')