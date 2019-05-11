'''
This program takes First name and Last name
then accept any kinds of information for user profile.
'''
# build and print user profile

def build_user_profile (fname, lname, **other_information):
    # Create empty dictionary to store values later on
    profile = {}
    profile['first_name'] = fname
    profile['last_name'] = lname
    for key, value in other_information.items():
        profile[key] = value
    return profile

user_profile = build_user_profile('Ganesh', 'Baral', field = 'Computer', sector = 'business')
# now printing full dictonary based on information supplied

print(user_profile)