# This program demonstrates single vs double quotes and raw strings.
# Both 'C' and "C" create the same string - there is no difference.
c = 'C'
c1 = "C"
print(c)
print(c1)

# dir = 'C:\pramod\n.txt'
# The r before the string makes it RAW, so \n is NOT treated as a new line.
dir = r"C:\pramod\n.txt" # raw - it will print as it is (ignore the escape seq.)
print(dir)