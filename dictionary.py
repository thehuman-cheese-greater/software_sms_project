#python3 level_six/functions_folder/dictionary.py

def login_data_for_user(**user_details):
    return dict(**user_details)

create_dictionary = login_data_for_user(username='Password01')
print(create_dictionary)

# Creating a new dict() for each person.  
create_dictioary = login_data_for_user(username3='Password0122')
print(create_dictioary)





#_________Reset_pdw_____________#
# def data_storage(**user_details):
#     return dict(**user_details)

# create_dictionary = data_storage(username='Password01')
# create_dictionary = data_storage(user='Pass')
# print(create_dictionary)



