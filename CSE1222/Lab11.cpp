/*
File:          freq.cpp
Created by:    Guoping Chen (chen.8759)
Creation Date: 12 Nov, 2018
Synopsis:      Using a bunch of completely unnecessary functions
               to do a simple vowel count;
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
	init_vectors(vowels, freqs);

	// Prompt the user for the input text by calling function read_text	
	input = read_text("Enter your text: ");

	// Copy the characters (ignoring non-alphabetic characters) in the input string to the vector of characters in variable text
	// Call function create_list to do this
	create_list(input, text);

	// Compute the frequencies of vowels and consonants from the input text containing only alphabetic letters
	// Call function compute_vowel_freqs to do this
	consonants = compute_vowel_freqs(text, vowels, freqs);

	// Display the vowels and their frequencies
	// Call functions display_characters and display_freqs
	display_characters(vowels, COLUMNWIDTH);
	cout << endl;
	display_freqs(freqs, COLUMNWIDTH);
	cout << endl;

	// Display the number of consonants. No function calls here.
	cout << "There are " << consonants << " consonants." << endl;

	return 0;
}

// FUNCTION DEFINITIONS GO HERE:
void init_vectors(vector<char> & vowels, vector<int> & frequencies) {
/* initialize two input vectors;
	parameter is literal, really no need to explain;
*/
	char temp[] = { 'a', 'e', 'i', 'o', 'u', 'y' };
	for (int i = 0; i < 6; i++) {
		vowels.push_back(temp[i]);
		frequencies.push_back(0);
	}
}

string read_text(const string & prompt) {
/* prompts the user for some text and returns the entered text as a string;
   prompt: prompt;
*/
	string temp;
	cout << prompt;
	getline(cin, temp);
	return temp;
}

bool is_alphabetic(const char character) {
/* returns trueif a character is an alphabetic character
   character: 
*/
	return ((character > 64 && character < 91) || (character > 96 && character < 123)) 
		? true : false;
}

void create_list(const string & str_text, vector<char> & vec_text) {
/* copies only the alphabetic characters from str_text to vec_text;
str_text: like was told;
vec_text: like was told;
*/
	for (int i = 0; i < str_text.size(); i++) {
		if (is_alphabetic(str_text[i]))
			vec_text.push_back(str_text[i]);
	}
}

bool is_member(const vector<char> & list, char character) {
/*returns trueif a character appears in a given vector of characters;
  list: the given vector;
  character: the character;
*/
	for (int i = 0; i < list.size(); i++) {
		if (character == list[i])
			return true;
	}
	return false;
}
int find_index(const vector<char> & list, char character) {
/* returns the index location where the input character appear.
   That function is a BAD idea;
   list: the given vector;
   character: the character;
*/
	for (int i = 0; i < list.size(); i++) {
		if (character == list[i])
			return i;
	}
	return -1;
}
int compute_vowel_freqs(const vector<char> & text, const vector<char> & vowels, vector<int> & freqs) {
/* computes the frequency of each of the six vowels and returns the number of consonants found in the input text;
   text: input text;
   vowels: vector of vowels;
   freqs: frequency;
*/
	int consonants(0);
	for (int i = 0; i < text.size(); i++) {
		if (is_member(vowels, tolower(text[i])))
			freqs[find_index(vowels, text[i])] += 1;
		else
			consonants++;
	}
	return consonants;
}

void display_characters(const vector<char> & characters, const int colwidth) {
/* display characters;
   characters: characters;
   colwidth: column width;
*/
	for (int i = 0; i < characters.size(); i++) 
		cout << ((i > 0) ? "," : " ") << setw(colwidth + 1) << characters[i];
	
		
}
void display_freqs(const vector<int> & freqs, const int colwidth) {
/* display frequency;
   freqs: frequency;
   colwidth: column width;
*/
	for (int i = 0; i < freqs.size(); i++)
		cout << ((i > 0) ? "," : " ") << setw(colwidth + 1) << freqs[i];
}
