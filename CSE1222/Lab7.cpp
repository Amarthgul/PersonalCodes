/*
File:          rootTable.cpp
Created by:    Guoping Chen (Chen.8759)
Creation Date: 12 Oct, 2018
Synopsis:      print a table of root
*/

#include <iostream>
#include <cmath>
#include <iomanip>
#include <string>
using namespace std;

int main()
{
	/* variable declaration */
	int numRoot;     // number of roots, user input
	int increment;   // value increment, user input
	int precision;   // precision, user input
	int columnWidth; // later calculated based on user input


	/* Get user input, didn't do the checking since not required :P */
	cout << "Enter number of roots: ";
	cin >> numRoot;
	cout << "Enter value increment (integer): ";
	cin >> increment;
	cout << "Enter precision: ";
	cin >> precision;


	/* calculation and display */
	columnWidth = (precision > 2)? (precision + 5) : 7;
	cout << "Value"; 
	for (int i = 2; i <= numRoot + 1; i++) {
		cout << setw(columnWidth) << std::right << "x^1/" + to_string(i);
	} /*by casting the int into a string
	    no need to worry about the number of digits.
		using `std::` to be more clear (I think...)  */
	cout << endl;
	for (int value = increment; value <= 100; value += increment) {
		cout << setw(5) << std::right << value;
		for (int i = 2; i <= numRoot + 1; i++) {
			cout << std::fixed << setprecision(precision);
			cout << setw(columnWidth) << std::right << pow(value, 1.0 / i);
		}
		cout << endl;
	}


	return 0;
}

/* I thought lab7 would be about function std::thinking */
