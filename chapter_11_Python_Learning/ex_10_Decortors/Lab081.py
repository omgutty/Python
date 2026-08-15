# This program shows the problem decorators solve:
# we must remember to call start() and end() ourselves around every test.
# start() does the setup work before the test.
def start():
    print("Before the running UI TC")
    print("Start the Browser ")

# end() does the cleanup work after the test.
def end():
    print("End the running UI TC")
    print("Quit the Browser ")

# test_ui() only tests; it knows nothing about setup or cleanup.
def test_ui():
    print("I will Test the UI")


# Without a decorator, we must call start(), test_ui(), end() manually.
start()
test_ui()
end()