/*
File:          freq.cpp
Created by:    Anon
Creation Date: 12 Nov, 2018
Synopsis:      Useless
*/

#include <iostream>
#include <iomanip>
#include <string>
#include <vector>

using namespace std;

/*
   YOU SERIOUSLY NEED THAT MANY FUNCTIONS?
*/

// FUNCTION PROTOTYPES GO HERE:
void init_vectors(vector<char> & vowels, vector<int> & frequencies);
string read_text(const string & prompt);
bool is_alphabetic(const char character);
void create_list(const string & str_text, vector<char> & vec_text);
bool is_member(const vector<char> & list, char character);
int find_index(const vector<char> & list, char character);
int compute_vowel_freqs(const vector<char> & text, const vector<char> & vowels, vector<int> & freqs);
void display_characters(const vector<char> & characters, const int colwidth);
void display_freqs(const vector<int> & freqs, const int colwidth);

int main()
{
	// Define local variables and constants
	vector<char> vowels;
	vector<int> freqs;
	string input;
	vector<char> text;
	int consonants(0);

	const int COLUMNWIDTH = 2;

	// Initialize the list of vowels and vowel frequencies.
	// Call function init_vectors with variables vowels and freqs

	// Prompt the user for the input text by calling function read_text
	
	// Copy the characters (ignoring non-alphabetic characters) in the input string to the vector of characters in variable text
	// Call function create_list to do this

	// Compute the frequencies of vowels and consonants from the input text containing only alphabetic letters
	// Call function compute_vowel_freqs to do this

	// Display the vowels and their frequencies
	// Call functions display_characters and display_freqs

	// Display the number of consonants. No function calls here.
	
	return 0;
}

// FUNCTION DEFINITIONS GO HERE:

