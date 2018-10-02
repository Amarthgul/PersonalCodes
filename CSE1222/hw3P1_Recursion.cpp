/*
File:          ovalRecursionVersion.cpp
Created by:    Guoping Chen (Chen.8759)
Creation Date: 2 Oct, 2018
Synopsis:      print Oval shape using recursion
*/

#include <iostream>
using namespace std;

void printStarSgl(int rowLength, int rowNum){
	cout << string(rowNum, ' ') << string(rowLength - 2 * rowNum, '*')
		 << string(rowNum, ' ') << endl;
}
void printStarRec(int rowLength, int rowNum){
	printStarSgl(rowLength, rowNum);
	if (rowNum != 0) {
		printStarRec(rowLength, rowNum - 1);
		printStarSgl(rowLength, rowNum);
	}
}

int main()
{
	int rowLength; //the number of '*'s in the middle row
	int rowNum; //he number of rows above and below the middle row

	/* prompt and read in*/
	cout << "Enter size of the middle rowLength: ";
	while (true) {
		cin >> rowLength;
		if (rowLength >= 3) break;
		cout << "Size of the middlerow must be at least three." << endl;
		cout << "Enter size of the middle row again: ";
	}

	cout << "Enter number of rows :";
	while (true) {
		cin >> rowNum;
		if (rowLength - 2 * rowNum >= 2) break;
		cout << "Invalid number of rows." << endl;
		cout << "Enter number of rows again :";
	}
	cout << endl;

	printStarRec(rowLength, rowNum);
}
//Shorter than using for loop
