// File: fallMars.cpp
// Created by: Guoping CHen (chen.8759)
// Created on: 9 Sept, 2018

/* my comment here */

/* valculate projectile horizontal distance*/

#include <iostream>
using namespace std;
int main(){
	
	/* Place my solution here */
	const double G = 9.81;
	double initVelocity;
	double horizonDist;

	//get user input
	cout << "Enter the initial velocity (meter/second): ";
	cin >> initVelocity;

	//calculate
	horizonDist = (initVelocity * initVelocity) / G;

	//output result
	cout << "Horizontal distance travelled is ";
	cout << horizonDist << " meters." << endl;;

	return(0);
}
