/*
File:          query.cpp
Created by:    Guoping Chen (Chen.8759)
Creation Date: 20 Sept, 2018
Synopsis: Determine the relationship of a point
          And 3 circles
*/

#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	// Variable declarations
	double circleData[3][3]; 
		// the ist index is circle, the second indicates x, y and radius
	double pointCord[2];
		// indicates x and y coordiantes 
	double distance[3];
		//Records the distance of the points with circles' pivot 
	bool   inCircle[3] = {false, false, false};
		// indicates whether that point is in the circle


	// Prompt and read center and radius for each circle
	for (int Index = 0; Index < 3; Index ++) {
		cout << "Enter x and y coordinates of circle C" 
			<< Index + 1 << " (2 values): ";
		cin >> circleData[Index][0] >> circleData[Index][1];
		cout << "Enter radius of circle C" << Index + 1<< ": ";
		cin >> circleData[Index][2];
	}
	

	// Prompt and read in query point
	cout << "Enter x and y coordinates of query point (2 values): ";
	cin >> pointCord[0] >> pointCord[1];


	// Determine location of query point relative to the circles
	for (int Index = 0; Index < 3; Index++) {
		distance[Index] = pow(pointCord[0] - circleData[Index][0], 2) +
			pow(pointCord[1] - circleData[Index][1], 2);
		distance[Index] = sqrt(distance[Index]);

		inCircle[Index] = (distance[Index] <= circleData[Index][2]);
			//whether contains in the circle
	}
	/* // Check
	for (int Index = 0; Index < 3; Index++) {
		cout << "for C1: ";
		cout << circleData[Index][0] << " " << circleData[Index][1] << " " <<circleData[Index][2];
		cout << "   In the circle? " << inCircle[Index] << endl;
	}*/

	
	// Final output
	if (!inCircle[0] && !inCircle[1] && !inCircle[2]) {
		cout << "No circle contains point (";
	} 
	else if ( inCircle[0] && !inCircle[1] && !inCircle[2]) {
		cout << "Circle C1 contains point (";
	}
	else if (!inCircle[0] &&  inCircle[1] && !inCircle[2]) {
		cout << "Circle C2 contains point (";
	}
	else if (!inCircle[0] && !inCircle[1] &&  inCircle[2]) {
		cout << "Circle C3 contains point (";
	}
	else if (!inCircle[0] &&  inCircle[1] &&  inCircle[2]) {
		cout << "Circles C2 and C3 contain point (";
	}
	else if ( inCircle[0] && !inCircle[1] &&  inCircle[2]) {
		cout << "Circles C1 and C3 contain point (";
	}
	else if ( inCircle[0] &&  inCircle[1] && !inCircle[2]) {
		cout << "Circles C1 and C2 contain point (";
	}
	else { cout << "Circles C1, C2, and C3 contain point ("; }

	cout << pointCord[0] << "," << pointCord[1] << ")" << endl;

	return 0;
}

/*
I spent a lot time trying to find the shortest way to code that
Yet the final output part is still bulky 

The indexing is really a pain :C
*/
