// File: fallMars.cpp
// Created by: Guoping CHen (chen.8759)
// Created on: 9 Sept, 2018

/* my comment here */

/* Kidding, that file calculates the velocity and distance 
   based on time given */

#include <iostream>
using namespace std;
int main(){
	
	/* Place your solution here */
	const double G = 3.73;
	double t;
	double velocity;
	double distance;

	//get user input
	cout << "Enter the time: ";
	cin >> t;

	//compute
	velocity = G * t;
	distance = (1 / 2.0) * velocity * t;

	//output result
	cout << "After " << t << " seconds, ";
	cout << "the velocity on mars is " << velocity << " meters per second." << endl;
	cout << "After " << t << " seconds, ";
	cout << "the falling distance on mars is " << distance << " meters." << endl;
	
	return(0);
}
