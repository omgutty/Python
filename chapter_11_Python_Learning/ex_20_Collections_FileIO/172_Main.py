# 172_Main.py
# Topic: if __name__ == '__main__' - the entry point pattern
#
# When a file runs DIRECTLY, Python sets __name__ to '__main__' and
# main() runs. When the same file is IMPORTED elsewhere, __name__ is
# the module name and main() does NOT run. This lets a file be both
# a reusable module AND a runnable script.

def main():
    print("Hello World!")

if __name__ == '__main__':
    main()   # runs only when this file is executed directly