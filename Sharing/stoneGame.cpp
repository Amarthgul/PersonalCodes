#include <iostream>
#include <iomanip>
#include <vector>
#include <numeric>
#include <string>
#include <cstdlib>

using namespace std;

// FUNCTION PROTOTYPES GO HERE:
void drawPercentage(const vector<int> &);
void statDisplay(const vector<int> &);
bool isEmpty(const vector<int> &);
void playerOperation(vector<int> &, bool &);

int main()
{
	int numRod;             //number of rods
	vector<int> stoneInRod; // the rods of stones
	bool playerOne = true;  // record who's turn
	
	const char * WINDOWS = "cls";   // use this if you're Windows
	const char * LINUX = "clear";   // use this if you're Linux
	bool refresh = true;    // do you want to refresh the console
	// For a game, don't refresh console is really a pain;
	// `system` is a bit dangerous (_stackoverflow_), but ik it's fine here

	cout << "How many rods are in this game? ";
	while (true) {
		cin >> numRod;
		if (numRod > 0) break;
		cout << "Number of rods must be positive and less than or equal to 20"
			<< endl << "Enter number of rods again : ";
	}

	cout << endl;
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

	cout << endl;
	drawPercentage(stoneInRod);

	cout << endl;
	statDisplay(stoneInRod);

	cout << endl;
	playerOperation(stoneInRod, playerOne);
	while (!isEmpty(stoneInRod)) {
		if (refresh)
			std::system(WINDOWS);
		cout << endl;
		drawPercentage(stoneInRod);
		
		cout << endl;
		statDisplay(stoneInRod);

		cout << endl;
		playerOperation(stoneInRod, playerOne);
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
	int smallestIndex(0), biggestIndex(0), nonZero(0);

	for (int i = 0; i < varVector.size(); i++) {
		if (varVector[i] > varVector[biggestIndex]) biggestIndex = i;
		if (varVector[i] < varVector[smallestIndex]) smallestIndex = i;
		if (varVector[i] != 0) nonZero++;
	}

	cout << "Rod " << smallestIndex + 1 << " has the smallest number of stones with "
		<< varVector[smallestIndex] << " object(s)." << endl;
	cout << "Rod " << biggestIndex + 1 << " has the largest number of stones with "
		<< varVector[biggestIndex] << " object(s)." << endl;

	cout << "The average number of stones per rod (i.e., rods with stones) is "
		<< std::fixed << setprecision(2) 
		<< accumulate(varVector.begin(), varVector.end(), 0) / double(nonZero)
		<<" stones." << endl;
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
