/*
File:          alt_harmonic.cpp
Created by:    Guoping Chen (Chen.8759)
Creation Date: 9 Oct, 2018
Synopsis:      calculate harmonic number
*/

#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	/* variable declaration */
	int userNum;
	double harmonic(0);


	/* get and verify user input */
	cout << "Enter n: ";
	cin >> userNum;
	while (userNum <= 1) {
		cout << "Value n must be 1 or greater. Try again: ";
		cin >> userNum;
	}


	/* calculation */
	for (int k = 1; k <= userNum; k++) {
		harmonic += pow(-1, k + 1) / k;
	}


	/* display result */
	cout << "The alternating series converges to " << harmonic << endl;

	return 0;
}
