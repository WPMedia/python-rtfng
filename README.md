For example usage, see the code in the unit tests in the 'test' directory and
its subdirectories.

To run all tests:

    virtualenv .
    ./bin/python setup.py develop
    ./bin/pip install -r requirements.txt
    ./bin/python -m unittest discover
