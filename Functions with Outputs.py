# # Functions with Outputs
#
# def format_name(f_name, l_name):
#     capitalized_f_name = f_name.capitalize()
#     capitalized_l_name = l_name.capitalize()
#
#     full_name = capitalized_f_name + " " + capitalized_l_name
#
#     print("Full name:", full_name)
#
# # Get user input
# user_f_name = input("What is your first name? ")
# user_l_name = input("What is your last name? ")
#
# # Call the function with user input
# format_name(user_f_name, user_l_name)

############### CLASS VERSION ################
def format_name(f_name, l_name):
    # print(f_name.title())
    # print(l_name.title())

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("rYdEr", "SHARPE")
print(formated_string)
