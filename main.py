RECIPIENT = '[RECIPIENT]'
SENDER = '[SENDER]'
sender_name = input('Provide sender name please: ')


# Open and store letter
with open('./input/letters/starting_letter.docx') as file:
    letter = file.read()


# Open file, readlineS and store names
with open('./input/names/invited_names.txt') as file:
    names = [name.strip() for name in file.readlines()]
# print(names)


# Input names in file
for name in names:
    if RECIPIENT in letter:
        with open(f'./output/ready_to_send/letter_for_{name}.docx', mode='w') as file:
            update_letter = letter.replace(RECIPIENT, name.title()).replace(SENDER, sender_name)
            file.write(update_letter)