#tester file for the project
from nose.tools import *
import MAIN

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!")
