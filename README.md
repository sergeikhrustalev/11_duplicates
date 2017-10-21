# Anti-Duplicator

Script duplicates.py recursively searches duplicate files in specified directory

# Requirements

Script require python3.5+

# How to use
```bash
$ python duplicates.py testdir
.DS_Store - 6148 bites found on the following path:
	testdir/.DS_Store
	testdir/d1/.DS_Store
	testdir/d3/.DS_Store
	testdir/d2/.DS_Store
1.txt - 0 bites found on the following path:
	testdir/1.txt
	testdir/d2/1.txt
2.txt - 27 bites found on the following path:
	testdir/2.txt
	testdir/d3/2.txt
	testdir/d2/2.txt
pycharm-community-2017.2.3.dmg - 193274572 bites found on the following path:
	testdir/d2/pycharm-community-2017.2.3.dmg
	testdir/d2/distrib/pycharm-community-2017.2.3.dmg
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
