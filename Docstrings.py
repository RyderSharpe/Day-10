



def format_name(f_name, l_name):
    # print(f_name.title())
    # print(l_name.title())

    ############ DOCSTRINGS ############
    """ Take a first and last name and format
    it to return the title case version of the name.
    (When you hover over "format_name", you'll see the docstring.)"""

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

format_name()

formated_string = format_name("rYdEr", "SHARPE")
print(formated_string)