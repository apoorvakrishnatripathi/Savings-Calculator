PROJECT TITLE:-

SmartInvest: Stock Interest & Savings Calculator

Overview of the Project :-

A Python-based console program called SmartInvest assists users in figuring out their investment returns.
There are two modes that it supports:

Custom Investment Mode: The user computes simple or compound interest by entering their own interest rate.

Stock-Based Investment Mode: The user chooses from a predetermined list of 20 stocks, each with a unique interest and return rate.

Additionally, depending on the user's preference, the program computes simple interest, compound interest, or both.

In order to guarantee that only users who are older than 17 can utilise the investment calculator, it also incorporates age validation.

 Features:-

 Validation of age (18+ required)

 Two ways to invest

Personalised savings calculator

Calculator for stock-based investments:-

-> 20 stocks with predetermined interest and return rates

-> Calculating simple interest

-> Calculating compound interest

> The ability to compare CI and SI

-> An interactive, clear console interface

 Tools and Technologies Used:

Python 3.x

Input and output from a console or terminal

How to Install and Run the Project:

Get the savings calculator in investemenet.py, a Python file. 

# Investment savings calculator

Verify that Python 3 is installed.
Verify by running:

Python --version

Launch a command prompt or terminal.

Go to the script's saved folder, for instance
CD Downloads
Launch the application
"Savings calculater in investemenet.py" in Python
To enter, adhere to the on-screen directions:

Name :
Age :
Amount:
Preference for interests:
Stoc0k selection (if stock mode is being used)

Instructions for Testing :-

Test the following scenarios to make sure everything functions properly:
1. Test of Age Restrictions

If your age is less than 18, the program should prevent you from accessing it.

Enter 18 years of age or older → The program should proceed.
 I 2. Test of Mode Selection

The custom investment calculator should open when you enter 1.
The stock-based calculator should open when you enter 2.

3. Easy Interest Test

Input
Amount: $10,000
5% interest
Three years
Select SI → The program should compute correctly:
SI is equal to (P × R × T)/100.

4. Test of Compound Interest

Select CI and confirm:

CI is equal to P × (1 + R/100)^T.

5. Test of Stock Selection

Choose a stock number, such as "3" (Nestle India).

Verify that the program is using the appropriate interest value from the tuple.

6. Test for Invalid Input

Try: Non-number inputs
Invalid mode :

Wrong stock number

Program should show error messages.
Basic arithmetic and exponentiation

Data structures (tuple for stock list & interest list)
Non-number inputs

Invalid mode

Wrong stock number
Program should show error messages.
Basic arithmetic and exponentiation

Data structures (tuple for stock list & interest list)
