# This program shows keyword arguments: we name each value we pass.
# Then the order of the arguments does not matter.
def display_information(name, role):
    print(f"Name : {name}, role is {role}")


# Here we say which parameter each value belongs to, using name= and role=.
display_information(name="Pramod2", role="QA2")
display_information(role="QA3", name="Pramod3")