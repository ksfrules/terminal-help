"""
let's help each other
the best game of 2024 - TERMINAL
https://t.me/terminal_CIS
contacts: https://t.me/ksfrules
"""

number_of_words = int(input("input number of words: "))
words = []
for i in range(number_of_words):
  words.append(input("input the word: "))
for word in words:
  print(word)
full_list = []
for i in range(len(words) - 1):
  for j in range(i + 1, len(words)):
    counter = 0
    word_i = ''
    word_j = ''
    for k in range(len(words[i])):
     if words[i][k] == words[j][k]:
        counter += 1
        word_i += words[i][k].capitalize()
        word_j += words[j][k].capitalize()
     else:
       word_i += words[i][k]
       word_j += words[j][k]
    letter_counter_list = [word_i, word_j]
    letter_counter_list.append(counter)
    full_list.append(letter_counter_list)
    
sorted_full_list = sorted(full_list, key=lambda x: x[2], reverse=True)
for letter_counter in sorted_full_list:
  print(letter_counter)  
