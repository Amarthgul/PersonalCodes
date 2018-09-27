/*
File:          scrabble.cpp
Created by:    Guoping Chen (Chen.8759)
Creation Date: 27 Sept, 2018
Synopsis: count occurrences of certain letters 
*/

#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main()
{
	// Variable declarations
	int numA(0);
	int numG(0);
	int numM(0);
	int numF(0);
	int numK(0);
	int numJ(0);
	string userInput;

	cout << "Enter text :" << endl;
	while (true) { // avoid code duplication
		cin >> userInput;

		int i(0); //iterator
		while (i < userInput.size()) {
			if (userInput.at(i) == '.' || userInput.at(i) == '!') { 
				//end condition
				cout << "\nNumber of a's (worth 1 point each) : " << numA << endl;
				cout << "Number of g's (worth 2 points each) : " << numG << endl;
				cout << "Number of m's (worth 3 points each) : " << numM << endl;
				cout << "Number of f's (worth 4 points each) : " << numF << endl;
				cout << "Number of k's (worth 5 points each) : " << numK << endl;
				cout << "Number of j's (worth 8 points each) : " << numJ << endl << endl;
				cout << "Total score: "
					<< numA + numG * 2 + numM * 3 + numF * 4 + numK * 5 + numJ * 8;
				//the solution demo given does not have an endline

				return 0; //exit here instead of at the bottom of `main()`
			}
			else if (userInput.at(i) == 'a' || userInput.at(i) == 'A')
				numA ++;
			else if (userInput.at(i) == 'g' || userInput.at(i) == 'G')
				numG ++;
			else if (userInput.at(i) == 'm' || userInput.at(i) == 'M')
				numM ++;
			else if (userInput.at(i) == 'f' || userInput.at(i) == 'F')
				numF ++;
			else if (userInput.at(i) == 'k' || userInput.at(i) == 'K')
				numK ++;
			else if (userInput.at(i) == 'j' || userInput.at(i) == 'J')
				numJ ++;

			i ++; 
		}
	}
}
