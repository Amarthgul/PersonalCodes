/*
File:          isprime.cpp
Created by:    Guoping chen (chen.8759)
Creation Date: 22 Octo, 2018
Synopsis:      find prime number in a given range
*/

#include <iostream>
#include <cmath>

using namespace std;

// FUNCTION PROTOTYPE FOR read_range
void read_range(int &, int &);

// FUNCTION PROTOTYPE FOR is_prime
bool is_prime(int);

// DO NOT MODIFY THE MAIN ROUTINE IN ANY WAY
int main()
{
	int imin(0), imax(0);

	// Read in range
	read_range(imin, imax);

	// Print prime numbers
	cout << "Primes:";
	for (int j = imin; j <= imax; j++) {
		if (is_prime(j))
		{
			cout << "  " << j;
		}
	}
	cout << endl;

	return 0;
}

// DEFINE FUNCTION read_range() HERE:
void read_range(int & iMin, int & iMax) {
	/* Read and verify input 
	iMin: input min;
	iMax: input max (Lol iMax);
	*/
	
	while (true) {
		cout << "Enter minimum and maximum: ";
		cin >> iMin >> iMax;
		if (iMin < 2 || iMax < 2)
			cout << "Error. Minimum and maximum must be at least 2." << endl;
		else if (iMin >= iMax)
			cout << "Error. Minimum must be less than maximum." << endl;
		else
			break;
	}
}

// DEFINE FUNCTION is_prime() HERE:
bool is_prime(int inNum) {
	/* Judge if inNum is prime number */

	bool isPrime = true;
	for (int i = 2; i < inNum; i++) {
		if (inNum % i == 0)
			isPrime = false;
	}
	return isPrime;
}
