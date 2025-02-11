def update_dict(data, subj):
    if subj in data:
        data[subj] = [mark + 5 for mark in data[subj]]

#original_dict = {'English': [83, 74, 90], 'Biology': [86, 89, 92], 'Math': [74, 84, 91]}
#update_dict(original_dict, 'Biology')
#print(original_dict)