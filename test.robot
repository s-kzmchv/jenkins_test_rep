*** Settings ***
Documentation       Test example.
Library             ./TestLibrary.py

*** Test Cases ***
Get the theoretical number of steps to an absorbing state
    Get theoretical  0
    Expect answer  8.8

Get the number of steps to an absorbing state by simulation with approximations
    Get im  0
    Expect answer with approximation  8.8  0.4

Compare the theoretical number and simulation result
    Compare
    Expect answer  Success

Start calculation with the wrong start state
    Get theoretical  3
    Expect answer  Wrong start

