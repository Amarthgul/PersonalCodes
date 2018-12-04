/*
File:          temps.cpp
Created by:    Guoping Chen (chen.8759)
Creation Date: 3 Dec 2018
Synopsis:      Record time onto a file
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
{/* Get Hour; */
	return hour;
}

int MilTime::getMin() const
{/* Get Minutes; */
	return minutes;
}

void MilTime::setHour(const int h)
{/* Set hour; */
	hour = h;
}

void MilTime::setMin(const int m)
{/* Set minutes; */
	minutes = m;
}

void MilTime::write_out(ofstream & fout)
{/* Writes the military time; */
/* Assumption unsafe, the solution has no minutes protection at all,
   You can have more than 60 min in 1 military-time-hour...*/
	bool autoCorrection = true;
	int mod;
	if (autoCorrection) {
		mod = getMin() / 60;
		setHour(getHour() + mod);
		setMin(getMin() - 60 * mod);
	}
	fout << ((getHour() < 10) ? "0" : "") << getHour() 
		<< ":" << ((getMin() < 10)? "0" : "") << getMin();
}

double Fahrenheit::getTemp() const
{/* Get temperature; */
	return degree;
}

MilTime Fahrenheit::getTime() const
{/* Get time; */
	return time;
}

double Fahrenheit::getCelsius() const
{/* Get Celsius degree; */
	return (degree - 32) * (5.0 / 9);
}

void Fahrenheit::setTemp(const double temp)
{/* Set temperature; */
	degree = temp;
}

void Fahrenheit::setTime(const int h, const int m)
{/* Set time; */
	time.setHour(h);
	time.setMin(m);
}

string read_filename(const string prompt)
{/* Read file name;
	prompt: prompt; */
	string kimiNoNaWa; //file name (actually a good movie)
	cout << prompt;
	cin >> kimiNoNaWa;
	return kimiNoNaWa;
}

int read_num_samples(const string prompt)
{/* Read number of samples;
	prompt: prompt; */
	int piper; // number of samples;
	cout << prompt;
	cin >> piper;
	return piper;
}

Fahrenheit read_sample()
{/* Read samples */
	double temp[2]; //record varibales
	Fahrenheit thisIsAFahrenheitInstance; // the instance 
	cout << "Enter degrees(Fahrenheit): ";
	cin >> temp[0];
	thisIsAFahrenheitInstance.setTemp(temp[0]);

	cout << "Enter hours (Military time): ";
	cin >> temp[0];
	cout << "Enter minutes (Military time):";
	cin >> temp[1];
	thisIsAFahrenheitInstance.setTime(int(temp[0]), int(temp[1]));

	return thisIsAFahrenheitInstance;
}

void write_to_file(const string filename, const vector<Fahrenheit> & samples)
{/* write to file;
	filename: file name;
	samples: sample instances;*/
	ofstream fart;
	fart.open(filename, ios::out);
	if (!fart.is_open()) {
		cerr << "You wouldn't have guessed what just happened, " << std::string('w', 200) 
			<< " the file couldn't be opened!" << endl;
		exit(1);
	}

	fart << endl;
	fart << std::string(73, '-') << endl;
	for (int i = 0; i < samples.size(); i++) {
		fart << "Sample #" << i + 1 << ": " << samples[i].getTemp() 
			<< " degrees F (or " << samples[i].getCelsius() 
			<< " degrees C ) at ";
		samples[i].getTime().write_out(fart);
		fart << endl;
	}
	fart << std::string(73, '-') << endl;

	fart << "The average temp is " << average_temp(samples) << " degrees F" << endl;
	fart << "The coldest temp is " << coldest_temp(samples) << " degrees F" << endl;
	fart << "The last sample was taken at time ";
	last_sample(samples).write_out(fart);
	fart << endl;
}

double average_temp(const vector<Fahrenheit> samples)
{/* Average Temprature; 
	samples: sample instances; */
	double sum(0); //sum
	for (int i = 0; i < samples.size(); i++) {
		sum += samples[i].getTemp();
	}
	return sum / samples.size();
}

double coldest_temp(const vector<Fahrenheit> samples)
{/* Coldest Temprature; 
	samples: sample instances; */
	double elsa = samples[0].getTemp(); //coldest temprature
	for (int i = 0; i < samples.size(); i++) {
		if (samples[i].getTemp() < elsa)
			elsa = samples[i].getTemp();
	}
	return elsa;
}

MilTime last_sample(const vector<Fahrenheit> samples)
{/* Last sample time; 
	samples: sample instances; */
	return samples[samples.size() - 1].getTime();
}
