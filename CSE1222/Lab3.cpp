// File: investments.cpp
// Created by: Guoping CHen (chen.8759)
// Created on: 12 Sept, 2018

/* (: my comment here :) */

/* Calculate 2 methods of investment */

#include <iostream>
#include <cmath>
using namespace std;
int main(){
	
	const double EULER(2.71828);
	int initInvest; //x. why int... I may 10.5 bucks for that
	int interestRate; //R
	int numMonth;
	double numYear; //Y
	double finalValue;
	double profit;
	double finalValueCombo; //creat combo variables in case for further useage
	double profitCombo;
	
	
	/* get user input */
	cout << "Enter initial investment (dollars): ";
	cin >> initInvest;
	cout << "Enter interest rate per year (percentage): ";
	cin >> interestRate;
	cout << "Enter number of months: ";
	cin >> numMonth;


	/* Calculation */
	numYear		= numMonth / 12.0;
	//The good old way
	finalValue	= initInvest * pow(1 + (interestRate / 100.0), numYear);
	profit		= finalValue - initInvest;
	// Combo!!!
	finalValueCombo = initInvest * pow(EULER, (interestRate / 100.0) * numYear);
	profitCombo		= finalValueCombo - initInvest;


	/*Output result*/
	cout << endl; //The good old way
	cout << "Value of your investment compounded annually after " << numYear 
		<< " year(s) is " << finalValue << " dollars." << endl;
	cout << "Profit from your investment after " << numYear 
		<< " year(s) is " << profit << " dollars." << endl << endl;
	// Combo!!!
	cout << "Value of your investment continuously compounded after " 
		<< numYear << " year(s) is " << finalValueCombo 
		<< " dollars." << endl;
	cout << "Profit from this investment is " << profitCombo
		<< " dollars." << endl << endl;
	// Compare
	cout << "The difference between both investment types is " 
		<< abs(profit - profitCombo) << " dollars." << endl;

	return (0);
}
