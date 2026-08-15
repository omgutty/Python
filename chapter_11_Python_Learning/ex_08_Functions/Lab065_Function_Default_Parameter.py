# This program shows default parameters: if we pass no value, the default is used.
# Here "QA" is the default value, used when no name is given.
def greet_with_default_param(name="QA"):
    print("Hi,", name)


greet_with_default_param("Pramod")
greet_with_default_param("Amit")
# No argument passed, so the default value "QA" is used.
greet_with_default_param()