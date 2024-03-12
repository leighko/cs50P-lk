"""
implement a program that prompts the user for names, one per line, until 
the user inputs control-d. Assume that the user will input at least one 
name. Then bid adieu to those names, separating two names with one and, 
three names with two commas and one and, and n names with n - 1 commas 
and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
"""

import inflect

p = inflect.engine()

prompt = "Name: "
   
def main():
    name_input = ask_and_store_name(prompt)
    name_output = convert_names_to_string(name_input)
    print(f"\nAdieu, adieu, to {name_output}")

        
def ask_and_store_name(name: str) -> list:
    no_name_input = True
    name_list = []
    while no_name_input:
        try:
            user_input = input(name)
            name_list.append(user_input)
        except EOFError:
            return name_list


def convert_names_to_string(n_list: list) -> str:
    for n in n_list:
        names = p.join(n_list)
        return names


if __name__ == "__main__":
    main()


# !!!! should i pass name_list into the next function here?
# !!!! or should i pass it in in the main function?

# def ask_and_store_nameme(name: str) -> str:
#     no_name_input = True
#     name_list = []
    
#     while no_name_input:
#         try:
#             user_input = input(name)
#             name_list.append(user_input)
#         except EOFError:
#             for n in name_list:
#                 name_str = p.join(name_list)
#             return name_str