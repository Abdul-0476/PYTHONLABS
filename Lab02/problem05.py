def remove_words1(string_list, remove_list):
    updated_list = [] # this will contain all of sentences after removing the wrong words for example this will contain ['Blue' , '','Purple', 'Red', 'Black'] and after we finish we return it

    for sentence in string_list: # This for loop will return the sentences in string_list e.g. blue color , Red# call this for-loop loop1

        splitted_word=sentence.split() # we split the word by the spaces  so blue color will become ['blue' , color] , and Red# will be ['Red#']

        list_of_updated_word=[] # this list will contain the word that are only valid in order to recreate a list that for example contain ['blue'] then we will use join to reconstruct the string.

        for w in splitted_word: # this for loop will go through the words that are spliited by space e g ['blue' , 'color'] , ['Red#'] call this for-loop loop2

             flag= False # this flag will tell us if the current word is valid or not

             for rword in remove_list:  # this for loop will go over all the porhibited words call this for-loop loop3

                 if rword in w: # check if the porhibited word exists in the current word

                     flag=True # if the porhibited word exists in the current word set the flag to True

                     break # stop looping over the other porhibited words since one porhibited word is sufficient

             if flag==False : # if we leave the loop3 and the flag is still false then add this word to a valid list which is called new string

                 list_of_updated_word.append(w) # for example now this list will contain ['blue'] on the first iteration of loop 2. the second iteration of loop 2 will detect the word color.

        updated_string = " ".join(list_of_updated_word)

        updated_list.append(updated_string)
    return updated_list
string_list = ['Blue color', 'Red#', 'Purple', 'Red %', 'Black']
remove_list = ['%', 'color', '#']

print(remove_words1(string_list,remove_list))