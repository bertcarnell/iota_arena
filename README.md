# iota_arena
A framework for iota algorithms to compete for iota domination

iota is a game consisting of cards and simple rules.  See the games and rules here:  http://www.iotathegame.com/

## PyCharm Community 2017.1 setup

Install coverage (nose is already installed with WinPython
pip install coverage

### Nosetests with code coverage
File -> Settings -> Tools -> External Tools -> + (add a tool)
Name: noseCoverage
Group: External Tools
Description:  code coverage with nose tests
Options: all checked
Show in: all checked
Tool Settings:
Program: C:\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\python.exe
Parameters: -m nose --with-coverage --cover-erase --cover-tests --cover-html --cover-package=$Prompt$ $FilePath$
WorkingDirectory: $ProjectFileDir$

Right click on the test directory, external tools, noseCoverage
Dialog pops up -> enter src to only show coverage for what is run in the src module

To view the coverage results, open the cover directory, right click on index.html and select open in browser.


