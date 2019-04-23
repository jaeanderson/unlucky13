# Unlucky13 Sum in Python
The general concept is to sum lists of numbers from a text file (luckynums1.txt, luckynums2.txt, and luckynums3.txt). However, a baker's dozen (the number 13) is considered very, very unlucky for the particular sum.  Therefore, do not count the number 13 and any number immediately following the unlucky 13. It is also noted an empty array returns 0.

For example, in this text file:
```
$ cat luckynums1.txt
1,2,2,1
1,2
1,0,0,1
2,-1
1,0,0,1,2,2
```

# Expected Behavior 
```
$ ./unlucky13.py
usage: unlucky13.py [-h] FILE
unlucky13.py: error: the following arguments are required: FILE
$ ./unlucky13.py -h
sage: unlucky13.py [-h] FILE

Unlucky 13 Sum

positional arguments:
  FILE        Input file

optional arguments:
  -h, --help  show this help message and exit
$ ./unlucky13.py luckynums1.txt
lucky sum: 6
lucky sum: 3
lucky sum: 2
lucky sum: 1
lucky sum: 6
$ ./unlucky13.py luckynums2.txt
lucky sum: 0
lucky sum: 0
lucky sum: 0
$ ./unlucky13.py luckynums3.txt
lucky sum: 3
lucky sum: 6
lucky sum: 4
```

# Test
To execute the test suite, run `make test` or `pytest -v test.py`

# Test Suite
```
$ make test
pytest -v test.py
============================= test session starts ==============================
platform linux -- Python 3.6.2, pytest-3.2.1, py-1.4.34, pluggy-0.4.0 -- /rsgrps/bhurwitz/hurwitzlab/bin/python3
cachedir: .cache
rootdir: /rsgrps/bh_class/jaea/biosys-analytics/assignments/14-open, inifile:
collected 3 items

test.py::test_usage PASSED
test.py::test_bad_input PASSED
test.py::test_runs_ok PASSED

=========================== 3 passed in 2.02 seconds ===========================
```

# Author
Jae R. Anderson jaea@email.arizona.edu
