/*
File:          temps.cpp
Created by:    Anon
Creation Date: 3 Dec 2018
Synopsis:      WTF 
*/

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

class MilTime
{
private:
	int hour;
	int minutes;

public:
	int getHour() const;
	int getMin() const;
	void setHour(const int h);
	void setMin(const int m);

	void write_out(ofstream & fout);
};

class Fahrenheit
{
private:
	double degree;
	MilTime time;

public:
	// member functions
	double getTemp() const;
	MilTime getTime() const;
	double getCelsius() const;

	void setTemp(const double temp);
	void setTime(const int h, const int m);
};

// FUNCTION PROTOTYPES GO HERE:
string read_filename(const string prompt);
int read_num_samples(const string prompt);
Fahrenheit read_sample();
void write_to_file(const string filename, const vector<Fahrenheit> & samples);
double average_temp(const vector<Fahrenheit> samples);
double coldest_temp(const vector<Fahrenheit> samples);
MilTime last_sample(const vector<Fahrenheit> samples);

int main()
{

	// Define local variables
	string fname;   	 	// Output file name
	int n;				// Number of temperature samples
	vector<Fahrenheit> temps;	// Temperature samples

								// Prompt for the name of the output file to write
	fname = read_filename("Enter the output file name: ");

	// Prompt for the number of temperature samples
	n = read_num_samples("Enter the number of samples: ");

	// Read temperature samples from user
	for (int i = 0; i < n; i++) {
		cout << endl;
		temps.push_back(read_sample());
	}

	// Write the sample information to the outputfile
	write_to_file(fname, temps);
	cout << endl;

	return 0;
}

// FUNCTION DEFINITIONS GO HERE:

// CLASS MEMBER FUNCTION DEFINITINOS GO HERE:

int MilTime::getHour() const
{/* code deleted */
}

int MilTime::getMin() const
{/* code deleted */
}

void MilTime::setHour(const int h)
{/* code deleted */
}

void MilTime::setMin(const int m)
{/* code deleted */
}

void MilTime::write_out(ofstream & fout)
{/* code deleted */
}

double Fahrenheit::getTemp() const
{/* Get temperature; */
	return degree;
}

MilTime Fahrenheit::getTime() const
{/* code deleted */
}

double Fahrenheit::getCelsius() const
{/* code deleted */
}

void Fahrenheit::setTemp(const double temp)
{/* code deleted */
}

void Fahrenheit::setTime(const int h, const int m)
{/* code deleted */
}

string read_filename(const string prompt)
{/* code deleted */
}

int read_num_samples(const string prompt)
{/* code deleted */
}

Fahrenheit read_sample()
{/* code deleted */
}

void write_to_file(const string filename, const vector<Fahrenheit> & samples)
{/* code deleted */
}

double average_temp(const vector<Fahrenheit> samples)
{/* code deleted */
}

double coldest_temp(const vector<Fahrenheit> samples)
{/* code deleted */
}

MilTime last_sample(const vector<Fahrenheit> samples)
{/* code deleted */
}
