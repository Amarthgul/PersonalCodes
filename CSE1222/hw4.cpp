/*
File:          vector2D.cpp
Created by:    Guoping Chen (chen.8759)
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

// ENTER FUNCTION PROTOTYPE FOR read_vector HERE.
void read_vector(const string & prompt, double & x, double & y);
// ENTER FUNCTION PROTOTYPE FOR vector_length HERE.
double vector_length(double x, double y);
// ENTER FUNCTION PROTOTYPE FOR write_vector HERE.
void write_vector(const string & prompt, double x, double y);
// ENTER FUNCTION PROTOTYPE FOR vector_add HERE.
void vector_add(double x1, double y1, double x2, double y2, double & x3, double & y3);
// ENTER FUNCTION PROTOTYPE FOR vector_subtract HERE.
void vector_subtract(double x1, double y1, double x2, double y2, double & x3, double & y3);
// ENTER FUNCTION PROTOTYPE FOR scalar_mult HERE.
void scalar_mult(double x1, double y1, double s, double & x2, double & y2);
// ENTER FUNCTION PROTOTYPE FOR normalize HERE.
void normalize(double & x, double & y);
// ENTER FUNCTION PROTOTYPE FOR perpendicular HERE.
void perpendicular(double x1, double y1, double x2, double y2);
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

// DEFINE FUNCTION read_vector HERE.
void read_vector(const string & prompt, double & x, double & y) {
	// read user input
	cout << prompt;
	cin >> x >> y;
}
// DEFINE FUNCTION vector_length HERE.
double vector_length(double x, double y) {
	// compuate the length of the vector
	return sqrt(x * x + y * y);
}
// DEFINE FUNCTION write_vector HERE.
void write_vector(const string & prompt, double x, double y) {
	// display a 2D vector and it's length
	cout << prompt << "(" << x << ", " << y << ") has length "
		<< vector_length(x, y) << endl;
}
// DEFINE FUNCTION vector_add HERE.
void vector_add(double x1, double y1, double x2, double y2, double & x3, double & y3) {
	// add 2 2D vectors and results in a new 2D vector
	x3 = x1 + x2;
	y3 = y1 + y2;
}
// DEFINE FUNCTION vector_subtract HERE.
void vector_subtract(double x1, double y1, double x2, double y2, double & x3, double & y3) {
	// subtract 2 2D vectors and results in a new 2D vector
	x3 = x1 - x2;
	y3 = y1 - y2;
}
// DEFINE FUNCTION scalar_mult HERE.
void scalar_mult(double x1, double y1, double s, double & x2, double & y2) {
	// apply scalar multiplication to a 2D vector and results in a new 2D vector
	x2 = s * x1;
	y2 = s * y1;
}
// DEFINE FUNCTION normalize HERE.
void normalize(double & x, double & y) {
	// normalize a 2D vector
	double length = vector_length(x, y);
	x = (abs(length) >= EPSILON) ? (x / length) : 0;
	y = (abs(length) >= EPSILON) ? (y / length) : 0;
}
// DEFINE FUNCTION perpendicular HERE.
void perpendicular(double x1, double y1, double x2, double y2) {
	// judging if 2 2D vectors are perpendicular
	double prpX1, prpY1, prpX2, prpY2;

	normalize(x1, y1);
	normalize(x2, y2);
	prpX1 = -y1; prpY1 = x1;
	prpX2 = -prpX1; prpY2 = -prpY1;

	cout << "Vectors are ";
	if (((abs(prpX1 - x2) <= EPSILON) && (abs(prpY1 - y2) <= EPSILON)) ||
		((abs(prpX2 - x2) <= EPSILON) && (abs(prpY2 - y2) <= EPSILON)))
		cout << "PERPENDICULAR";
	else
		cout << "NOT PERPENDICULAR";
}
