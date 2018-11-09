/*
File:          pickstones.cpp
Created by:    Guoping Chen
Creation Date: 8 Nov, 2018
Synopsis:      Play a complex game
*/

/* I tried first to follow the comment instruction,
   but what came out was incredibly ugly with toms of bugs.
   So I gave up and started using another implentation, 
   as what you are about to see
*/

#include <iostream>
#include <iomanip>
#include <vector>
#include <numeric>
#include <string>

using namespace std;


// FUNCTION PROTOTYPES GO HERE:
void drawPercentage(const vector<int> &);
void statDisplay(const vector<int> &);
bool isEmpty(const vector<int> &);
void playerOperation(vector<int> &, bool &);

int main()
{
	// Define variables and constants here
	int numRod;
	vector<int> stoneInRod;
	bool playerOne = true;
	bool refresh = true;

	// Algorithm:

	// Prompt and read number of rods
	cout << "How many rods are in this game? ";
	while (true) {
		cin >> numRod;
		if (numRod > 0) break;
		cout << "Number of rods must be positive and less than or equal to 20"
			<< endl << "Enter number of rods again : ";
	}

	// Prompt and read the number of objects in each rod
	for (int i = 0; i < numRod; i++) {
		int temp;
		while (true) {
			cout << "How many stones are on rod " << i + 1 << ": ";
			cin >> temp;
			if ((temp > 0) && (temp <= 10)) break;
			cout << "Sorry, the number of stones must be positive and less than or equal to 10." << endl;
		}
		stoneInRod.push_back(temp);
	}

	// Draw the rods with percentages
	cout << endl;
	drawPercentage(stoneInRod);

	// Display statistics
	cout << endl;
	statDisplay(stoneInRod);

	// WHILE some rod is NOT empty DO
	playerOperation(stoneInRod, playerOne);
	while (!isEmpty(stoneInRod)) {
		if (refresh)
			std::system("cls");
		// Prompt and read the next player's move
		// Remove the specified number of objects from the specified rod
		// IF all the heaps are empty, THEN
		// Print a message congratulating the winning player.
		// ELSE
		// Redraw the rods with percentages
		cout << endl;
		drawPercentage(stoneInRod);
		// Display statistics
		cout << endl;
		statDisplay(stoneInRod);

		// Change to the other player
		cout << endl;
		playerOperation(stoneInRod, playerOne);

		// END IF
		// END WHILE
	}

	cout << endl << "Congratulations! Player " 
		<< (playerOne ? 2 : 1) << " wins." << endl;

	return 0;
}

// FUNCTION DEFINITIONS GO HERE:
void drawPercentage(const vector<int> & varVector) {
	/* Draw the rods with percentages;
	varVector: vector to draw;
	*/
	for (int i = 0; i < varVector.size(); i++) {
		cout << "Rod " << i + 1 << ": ";
		cout << std::left << setw(16) << string(varVector[i], '*');
		cout << "(" << std::fixed << setprecision(3)
			<< varVector[i] * 100.0 / accumulate(varVector.begin(), varVector.end(), 0)
			<< "%)" << endl;
	}
}

void statDisplay(const vector<int> & varVector) {
	/* Display statistics;
	varVector: vector to display;
	*/
	int smallestIndex(0), biggestIndex(0);

	for (int i = 0; i < varVector.size(); i++) {
		if (varVector[i] > varVector[biggestIndex]) biggestIndex = i;
		if (varVector[i] < varVector[smallestIndex]) smallestIndex = i;
	}

	cout << "Rod " << smallestIndex + 1 << " has the smallest number of stones with "
		<< varVector[smallestIndex] << " object(s)." << endl;
	cout << "Rod " << biggestIndex + 1 << " has the largest number of stones with "
		<< varVector[biggestIndex] << " object(s)." << endl;
}

bool isEmpty(const vector<int> & varVector) {
	for (int i = 0; i < varVector.size(); i++)
		if (varVector[i] != 0)
			return false;
	return true;
}

void playerOperation(vector<int> & varVector, bool & isPlayerOne) {

	int numRodToOp;
	int numStoneToRm;

	while (true) {
		cout << "Player (" << (isPlayerOne ? 1 : 2) << ") : Which rod would you like to play? ";
		cin >> numRodToOp;
		if (varVector[numRodToOp - 1] == 0) {
			cout << "Rod " << numRodToOp << " has zero stones. Please select a different rod." << endl;
			continue;
		}
		if ((numRodToOp > 0) && (numRodToOp <= varVector.size())) break;
		cout << "Invalid rod number. Please try again." << endl;
	}

	while (true) {
		cout << "Enter number of stones to remove (" << varVector[numRodToOp - 1]
			<< " or less) from rod " << numRodToOp << ": ";
		cin >> numStoneToRm;
		if (numStoneToRm <= 0)
			cout << "Number of stones you can remove must be positive. Try again." << endl;
		else if (numStoneToRm > varVector[numRodToOp - 1])
			cout << "Can only remove up to " << varVector[numRodToOp - 1] 
			<< " object(s). Please try again." << endl;
		else break;
	}

	varVector[numRodToOp - 1] -= numStoneToRm;
	isPlayerOne = !isPlayerOne;
}
