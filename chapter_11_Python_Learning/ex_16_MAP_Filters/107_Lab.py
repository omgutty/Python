# 107_Lab.py
# Topic: filter() with a lambda - real-world test result filtering
#
# filter(lambda x: x == "PASS", test_results) walks the list and
# keeps only the items equal to "PASS". Great for QA: filter out
# only the passing tests from a list of results.

test_results = ["PASS", "FAIL", "PASS", "SKIP", "FAIL"]

pass_give = list(filter(lambda x: x == "PASS", test_results))
print(pass_give)   # ['PASS', 'PASS']