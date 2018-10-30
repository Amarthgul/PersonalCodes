/*
File:          array.cpp
Created by:    Guoping chen (chen.8759)
Creation Date: 29 Octo, 2018
Synopsis:      read and find the minimum value then subtract in a given array
*/

#include <iostream>
#include <cmath>

using namespace std;

void read_list(int * , int & , const int );
void print_array(const int * , const int );
int find_min(const int * , const int );
void array_subtract(int * , const int , const int );

int main()
{
	int const LAB9_SPECIAL_DIGIT = 25;     //I guess every program has he's special digit
	int thisIsAnArray[LAB9_SPECIAL_DIGIT]; //user input array
	int numElements; // number of elements
	int smallest;    //the smallest element

	read_list(thisIsAnArray, numElements, LAB9_SPECIAL_DIGIT);
	if (thisIsAnArray[0] == 0) {
		cout << endl << "The list is empty" << endl;
		return 0;
	}

	cout << "Before list: (" << numElements << " numbers): " << endl;
	print_array(thisIsAnArray, numElements);

	smallest = find_min(thisIsAnArray, numElements);
	cout << endl << "The mininum value = " << smallest << "\n\n";

	array_subtract(thisIsAnArray, numElements, smallest);

	cout << "After list: (" << numElements << " numbers): " << endl;
	print_array(thisIsAnArray, numElements);

	return 0;
}


void read_list(int * inputArray, int & numElements, const int maxSize) {
	/* read usrt input array */
	/* inputArray:   array holding integers
	   numElements:  number of elements stored in the array
	   maxSize:      maximum size of the array
	*/
	int temp;
	cout << "Enter positive numbers (ints) terminated by 0 " << endl;
	for (int i = 0; i < maxSize; i++) {
		cin >> temp;
		if (temp > 0)
			inputArray[i] = temp;
		else if (temp == 0) {
			inputArray[i] = temp;
			numElements = i;
			break;
		}
		else
			i--;
	}
}

void print_array(const int * inputArray, const int numElements) {
	/* print array */
	/* inputArray:   array holding integers
	   numElements:  number of elements stored in the array
	*/
	for (int i = 0; i < numElements; i++) {
		cout << inputArray[i];
		if (i == numElements - 1)
			cout << "." << endl;
		else
			cout << ", ";
	}
}

int find_min(const int * inputArray, const int numElements) {
	/* find the minimum value in the array */
	/* inputArray:   array holding integers
	   numElements:  number of elements stored in the array
	*/
	int smallest = inputArray[0];
	for (int i = 0; i < numElements; i++) {
		if (inputArray[i] < smallest)
			smallest = inputArray[i];
	}

	return smallest;
}

void array_subtract(int * inputArray, const int numElements, const int numToSubtract) {
	/* subtracts numToSubtract to every element of the array */
	/* inputArray:    array holding integers
	   numElements:   number of elements stored in the array
	   numToSubtract: number to substract to every element of the array
	*/
	for (int i = 0; i < numElements; i++) {
		inputArray[i] -= numToSubtract;
	}
}
