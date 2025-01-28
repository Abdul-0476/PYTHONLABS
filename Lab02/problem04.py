#def compare_strings(string1, string2):
#
 #   sorted1 = sorted(string1)
  #  sorted2 = sorted(string2)


   # if len(sorted1) != len(sorted2):
    #    return False

    #for i in range(len(sorted1)):
     #   if sorted1[i] != sorted2[i]:
      #      return False

    #return 'yes'

#print(compare_strings('abcd', 'cdab'))  # Output: True
#print(compare_strings('abcd', 'abtc'))  # Output: False
#print(compare_strings('AABC', 'ABC'))   # Output: False


def have_same_characters(str1, str2):

    if len(str1) != len(str2):
        return False

    char_count = {}

    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    return all(count == 0 for count in char_count.values())


string_1 = 'abcd'
string_2 = 'cdab'
print(have_same_characters(string_1, string_2))  # Output: True

string_1 = 'abcd'
string_2 = 'abtc'
print(have_same_characters(string_1, string_2))  # Output: False

string_1 = 'AABC'
string_2 = 'ABC'
print(have_same_characters(string_1, string_2))  # Output: False