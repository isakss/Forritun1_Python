def get_emails():
    email_list = []
    email_input = input("Email address: ")
    
    while email_input != "q":
        email_list.append(email_input)
        email_input = input("Email address: ")
    return email_list

def get_names_and_domains(list_object):
    tuple_list = []
    for element in list_object:
        tuple_list.append(tuple(element.split("@")))
    return tuple_list
# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)