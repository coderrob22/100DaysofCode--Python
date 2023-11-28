PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("./Input/Letters/starting_letter.txt") as old_name:
    data = old_name.read()
    
    
    for name in names:
        update_letter = data.replace(PLACEHOLDER, name.strip())

        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", 'w') as complete_letter:
            complete_letter.write(update_letter) 

