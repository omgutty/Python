# This program shows two decorators: one adds logs, the other measures time.
import time


# This decorator prints a log line before and after the function runs.
def print_logs(func):
    def wrapper():
        print("Start the logs")
        func()
        print("End of the log")
    return wrapper

# This decorator measures how long the function takes to run.
def time_decorator(func):
    def wrapper():
        # Record the time just before the function runs.
        start_time = time.time()
        print(start_time)
        func()
        # Record the time again after it finishes.
        end_time = time.time()
        print(end_time)
        print("Total Time Take by Func -> ", end_time - start_time)
    return wrapper



# Stacked decorators: the bottom one (@print_logs) runs first, then @time_decorator.
# @deco applies the decorator: test_ui_1 = time_decorator(print_logs(test_ui_1))
@time_decorator
@print_logs
def test_ui_1():
    print("Add a function, time taken by this function 1")
    # time.sleep(2) pauses the program for 2 seconds so we can measure the time.
    time.sleep(2)

@time_decorator
@print_logs
def test_ui_2():
    print("Add a function, time taken by this function 2")
    time.sleep(5)



test_ui_1()
test_ui_2()
