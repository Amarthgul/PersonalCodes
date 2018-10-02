/*
File:          oval.cpp
Created by:    Guoping Chen (Chen.8759)
Creation Date: 2 Oct, 2018
Synopsis:
*/

#include <iostream>
#include <iomanip>
#include <cstdlib>
using namespace std;

int main()
{
	int rowLength; //the number of '*'s in the middle row
	int rowNum; //he number of rows above and below the middle row

	/* prompt and read in*/
	cout << "Enter size of the middle rowLength: ";
	while (true) {
		cin >> rowLength;
		if (rowLength >= 3)
			break;
		cout << "Size of the middlerow must be at least three." << endl;
		cout << "Enter size of the middle row again: ";
	}

	cout << "Enter number of rows :";
	while (true) {
		cin >> rowNum;
		if (rowLength - 2 * rowNum >= 2)
			break;
		cout << "Invalid number of rows." << endl;
		cout << "Enter number of rows again :";
	}
	cout << endl;


	/* Display the oval */
	for (int i = rowNum; i > 0; i--) {
		for (int j = 0; j < i; j++)
			cout << " ";
		for (int j = 0; j < rowLength - 2 * i; j++)
			cout << "*";
		for (int j = 0; j < i; j++)
			cout << " ";
		cout << endl;
	}
	cout << setfill('*') << setw(rowLength) << "*" << endl;
	for (int i = 1; i < rowNum+1; i++) {
		for (int j = 0; j < i; j++)
			cout << " ";
		for (int j = 0; j < rowLength - 2 * i; j++)
			cout << "*";
		for (int j = 0; j < i; j++)
			cout << " ";
		cout << endl;
	}
}

//Shouldn't this be more efficient with recursion
