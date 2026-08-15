# This program demonstrates escape sequences in strings.
# Escape sequences are special codes inside text that do special things.
# Escape Sequence
# \n -> new line
# \t -> tab
# \b -> backspace (1 char backspace)

# \n inside the string makes a new line.
print("Hello\nWorld")
# \t adds a tab (space) between the words.
print("Hello\tWorld")
# \b removes the character before it (backspace) - Hello\b becomes Hell.
print("Hello\bWorld")