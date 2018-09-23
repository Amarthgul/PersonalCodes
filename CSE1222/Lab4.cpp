/*
File:          compare.cpp
Created by:    Guoping Chen (Chen.8759)
Creation Date: 22 Sept, 2018
Synopsis: Compare the position of 2 points
*/

#include <iostream>
#include <string>
using namespace std;

int main()
{
	// Variable declarations
	double ptOneCoord[] = { .0, .0 }; //x1 y1, coordinates of point one
	double ptTwoCoord[] = { .0, .0 }; //x2 y2, coordinates of point two
	string horizontal = "right ";     // relation horizontally
	string vertical = "above ";       //relation vertically
	string connection = "and ";       //whether needs an "and"

	// Prompt and read points coordinates
	cout << "Enter coordinates of the first point (2 values): ";
	cin >> ptOneCoord[0] >> ptOneCoord[1];
	cout << "Enter coordinates of the second point (2 values): ";
	cin >> ptTwoCoord[0] >> ptTwoCoord[1];


	/* when comparing coordinates,
	   I decided to use 4 `if else` to reduce code duplicate.
	   By separate x and y
	   I also don't have to write a loooooong if expression
	*/
	if (fabs(ptTwoCoord[0] - ptOneCoord[0]) < 0.0001) {
		vertical = "";
	}
	else if (ptTwoCoord[0] - ptOneCoord[0] < -0.0001) {
		vertical = "below ";
	}
	if (fabs(ptTwoCoord[1] - ptOneCoord[1]) < 0.0001) {
		horizontal = "";
	}
	else if (ptTwoCoord[1] - ptOneCoord[1] < -0.0001) {
		horizontal = "left ";
	}

	if ((horizontal.size() == 0) || (vertical.size() == 0)){
		connection = "";
	}


	// Final output
	if ((horizontal.size() == 0) && (vertical.size() == 0)) {
		cout << "Point (" << ptTwoCoord[0] << "," << ptTwoCoord[1] 
			<< ") equals point (" << ptOneCoord[0] << "," << ptOneCoord[1] 
			<< ")" << endl;
	}
	else {
		cout << "Point (" << ptTwoCoord[0] << "," << ptTwoCoord[1] 
			<< ") is " << vertical << connection << horizontal 
			<< "of point (" << ptOneCoord[0] << ", " << ptOneCoord[1]
			<< ")" << endl;
	}


	return 0;
}
/*
I assume I am supposed to use loop?
But how?

Also, without a dict type
(I just learned c++ has dict, but I don't quite understand how it works)
writing this is really a pain
*/
