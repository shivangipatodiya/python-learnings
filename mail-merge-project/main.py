#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", mode='r') as list_of_names:
    for name in list_of_names:
        new_letter_filepath = "./Output/ReadyToSend/letter_for_" + name.strip()
        with open("./Input/Letters/starting_letter.txt", mode='r') as letter_format:
            content = letter_format.read()
            with open(new_letter_filepath, mode='w') as final_letter:
                new_content = content.replace("[name]", name.strip())
                final_letter.write(new_content)
