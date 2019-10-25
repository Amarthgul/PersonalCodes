/*
File:  vector2D.cpp
Created by:  Anon
Creation Date:
Synopsis: ??
*/

#include <iostream>
#include <string>
#include <iomanip>
#include <cmath>

using namespace std;

const double EPSILON(1e-12);

// function prototypes

// code deleted

// *** DO NOT CHANGE ANY CODE IN THE MAIN FUNCTION.
int main()
{
	double u1, v1;	// coordinates of first vector
	double u2, v2;	// coordinates of second vector
	double u3, v3;
	double scalar;

	read_vector("Enter first vector (2 floats): ", u1, v1);
	read_vector("Enter second vector (2 floats): ", u2, v2);

	cout << "Enter scalar multiplier: ";
	cin >> scalar;
	cout << endl;

	write_vector("First vector: ", u1, v1);
	write_vector("Second vector: ", u2, v2);

	cout << endl;

	vector_add(u1, v1, u2, v2, u3, v3);
	write_vector("Vector add: ", u3, v3);

	vector_subtract(u1, v1, u2, v2, u3, v3);
	write_vector("Vector subtract: ", u3, v3);

	scalar_mult(u1, v1, scalar, u3, v3);
	write_vector("Scalar multiplier: ", u3, v3);

	cout << endl;

	write_vector("First vector: ", u1, v1);
	write_vector("Second vector: ", u2, v2);
	perpendicular(u1, v1, u2, v2);

	return(0);
}

// code deleted
