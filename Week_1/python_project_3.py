user_input = input("Please enter a sentence to analylze : ")

list_input = user_input.split(" ")
word_count = 0
longest_word = " "
list_so_far = []
totaal_characters = 0
for word in list_input :
    word_count += 1
    longest_word = word if len(word) > len(longest_word) else longest_word

    totaal_characters += len(word) # This gives totaal character excluding spaces
    if word not in list_so_far:
        list_so_far.append(word) # Add unieq words in this list
    

print(f"There {'is' if word_count == 1 else 'are'} totaal {word_count} {'word' if word_count == 1 else 'words'} in the given sentence")
print(f"{'The longest word is':<20}: {longest_word}") # 
print(f"{'Total unieq words':<20}: {len(list_so_far)}") # 
print(f"{'Total characters':<20}: {totaal_characters}") # 

