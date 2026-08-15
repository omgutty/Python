# This program shows a decorator that prints messages before and after a test.
# The wrapper function holds the extra steps around the original function.
def before_after_ui_test(func):
     def wrapper():
          print("Before the TC code execute!")
          # Call the original test function.
          func()
          print("After the TC Done")
     return wrapper()


# @before_after_ui_test applies the decorator: test_ui = before_after_ui_test(test_ui)
@before_after_ui_test
def test_ui():
     print("Hi, I am testing a UI Test")