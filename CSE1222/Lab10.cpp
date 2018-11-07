/*
File:          split.cpp
Created by:    Guoping chen (chen.8759)
Creation Date: 29 Octo, 2018
Synopsis:      read and find the minimum value then subtract in a given array
*/

#include <iostream>
#include <cmath>
#include <cstdlib>

using namespace std;

int count(int *, const int, int &, int &);
void split(const int *, int *, int *, const int, const int, const int);
void print_list(const int *, const int);

int main()
{
	int numElements;   // number of elements
	int * labTenArray = new int; // pointer array
	int * labTenEven = new int;  // subarray of even numbers
	int * labTenOdd = new int;   // subarray of odd numbers
	int numEven(0);       // number of even number
	int numOdd(0);        // number of odd number
	int numZero(0);       // number of zero

	cout << "Enter number of elements: ";
	cin >> numElements;

	cout << "Enter list:" << endl;
	for (int i = 0; i < numElements; i++) {
		cin >> labTenArray[i];
	}

	numZero = count(labTenArray, numElements, numEven, numOdd);

    print_list(labTenArray, numElements);
	split(labTenArray, labTenEven, labTenOdd, numElements, numEven, numOdd);

	cout << "Even elements:" << endl;
	print_list(labTenEven, numEven);

	cout << "Even elements:" << endl;
	print_list(labTenOdd, numOdd);

	cout << "There were " << numZero << " zeros in the list." << endl;

	delete labTenArray;
	delete labTenEven;
	delete labTenOdd;

	return 0;
}


int count(int * userArray, const int numElements, int & numEven, int & numOdd) {
	int numZero; // number of zero

	for (int i = 0; i < numElements; i++) {
		if (userArray[i] == 0)
			numZero++;
		else if (userArray[i] % 2)
			numOdd++;
		else
			numEven++;
	}

	return numZero;
}


void split(const int * motherArray, int * childEven, int * childOdd,
		  const int lengthMother, const int lengthEven, const int lengthOdd) {

			  cout << lengthMother << endl;
	int oddTracker(0), evenTracker(0);
	for (int i = 0; i < lengthMother; i++) {
		cout << i << " currently in : " << motherArray[i] << " ";
		if (motherArray[i] % 2) { // odd
			childOdd[oddTracker] = motherArray[i];
			cout << "it's odd" << endl;
			oddTracker++;
		}
		else { //even
			childEven[evenTracker] = motherArray[i];
			cout << "it's even" << endl;
			evenTracker++;
		}
	}

	cout << evenTracker << " " << lengthEven << endl;
	cout << oddTracker << " " << lengthOdd << endl;

	if ((evenTracker != lengthEven) || (oddTracker != lengthOdd)) {
		cerr << "Error Message" << endl;
		exit(1);
	}
}

void print_list(const int * inputArray, const int arraySize) {
	/* print array elements;
	inputArray: input array;
	arrayLength: length of the input array;
	*/
	for (int i = 0; i < arraySize; i++) {
		cout << " " << inputArray[i];
	}
	cout << endl;
}
