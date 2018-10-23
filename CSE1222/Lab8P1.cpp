/*
File:          polarcoord.cpp
Created by:    Guoping Chen (chen.8759)
Creation Date: 22 Octo, 2018
Synopsis:      Given radius and polar angle, 
               calculate Cartesian coordinates.
*/

#include <iostream>
#include <cmath>

using namespace std;

// FUNCTION PROTOTYPE FOR degrees2radians
double degrees2radians(double);

// FUNCTION PROTOTYPE FOR compute_coord
void compute_coord(double, double, double &, double &);

// DO NOT MODIFY THE MAIN ROUTINE IN ANY WAY
int main()
{
	double angle_degrees(0.0), angle_radians(0.0), radius(0.0);
	double coord_x(0.0), coord_y(0.0);

	// Read in polar coordinates
	cout << "Enter radius: ";
	cin >> radius;

	cout << "Enter polar angle (degrees): ";
	cin >> angle_degrees;

	// Convert degrees to radians
	angle_radians = degrees2radians(angle_degrees);

	// Compute Cartesian (x,y) coordinates
	compute_coord(radius, angle_radians, coord_x, coord_y);

	// Output Cartesian coordinates
	cout << "Cartesian coordinates: ";
	cout << "(" << coord_x << "," << coord_y << ")" << endl;

	return 0;
}

// DEFINE FUNCTION degrees2radians here:
double degrees2radians(double degree) {
	/* Convert degree to radians.
	degree: degree (what else could I explain);
	*/

	return degree * 3.14159265358979323846 / 180;
}

// DEFINE FUNCTION compute_coord here:
void compute_coord(double radius, double angleRadians,
	double & coordX, double & coordY) {
	/* Compute coordiantes based on radius and angle radians 
	radius: the polar radius of the point;
	angleRadians: the polar angle in radians of the point;
	coordX: the x-coordinate of the point;
	coordY: the y-coordinate of the point;
	*/

	coordX = radius * cos(angleRadians);
	coordY = radius * sin(angleRadians);
}

