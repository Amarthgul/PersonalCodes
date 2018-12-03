/*
File:          polys.cpp
Created by:    Anon
Creation Date: 2 Dec 2018
Synopsis:      ?
*/

#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <cstdlib>

using namespace std;

class Term
{
private:
	int coeff;
	int exp;

public:
	int getCoeff() const;
	int getExp() const;
	void setCoeff(const int coefficient);
	void setExp(const int exponent);

	double eval(const double x) const;
	Term derivative() const;
	Term multiply(const Term & term) const;

	void displayFirst() const;
	void displayNext() const;

};

class Poly
{
private:
	vector<Term> terms;		// Terms are in decreasing order of degree

public:
	// member functions
	Term getTerm(const int index) const;
	int degree() const;		// highest degree
	int termCount() const;	// number of terms

	void addTerm(const int coeff, const int exp);
	void scale(const int fact);

	double eval(const double x) const;		// evaluate polynomial with value x
	Poly derivative() const;				// derivative

	void display(const string & label) const;
	void displayMultiply(const Poly & poly, const string & label) const;

};

void display_banner();
Poly read_poly(const int label);
void display_stats(const Poly & poly, const string & label);
void evaluate_poly(const Poly & poly);
void goodbye_banner();

int main()
{
	Poly poly1, poly2;
	int scale;

	display_banner();

	poly1 = read_poly(1);
	cout << endl;
	display_stats(poly1, "You entered polynomial #1");

	poly2 = read_poly(2);
	cout << endl;
	display_stats(poly2, "You entered polynomial #2");

	cout << "Multiplication terms - " << endl << endl;;
	poly1.displayMultiply(poly2, "Poly #1 * Poly #2");
	poly2.displayMultiply(poly1, "Poly #2 * Poly #1");

	cout << endl;

	evaluate_poly(poly1);
	cout << endl;

	if (poly1.termCount() > 0) {
		cout << "Enter a scale factor to apply to polynomial #1: ";
		cin >> scale;
		poly1.scale(scale);
		display_stats(poly1, "The polynomial after scaling");
	}

	goodbye_banner();

	return 0;
}

// CLASS TERM MEMBER FUNCTIONS
int Term::getCoeff() const
{/* code deleted */
}

int Term::getExp() const
{/* code deleted */
}

void Term::setCoeff(const int coefficient)
{/* code deleted */
}

void Term::setExp(const int exponent)
{/* code deleted */
}

double Term::eval(const double x) const
{/* code deleted */
}

Term Term::derivative() const
{/* code deleted */
} 

Term Term::multiply(const Term & term) const
{/* code deleted */
}

void Term::displayFirst() const
{/* code deleted */
}
void Term::displayNext() const
{/* code deleted */
}

// CLASS POLY MEMBER FUNCTIONS
Term Poly::getTerm(const int index) const
{/* code deleted */
}

int Poly::degree() const
{/* code deleted */
}

int Poly::termCount() const
{/* code deleted */
}

void Poly::addTerm(const int coeff, const int exp)
{/* code deleted */
}

void Poly::scale(const int fact)
{/* code deleted */
}

double Poly::eval(const double x) const
{/* code deleted */
}

Poly Poly::derivative() const
{/* code deleted */
}

void Poly::display(const string & label) const
{/* code deleted */
}

void Poly::displayMultiply(const Poly & poly, const string & label) const
{/* code deleted */
}

// NON-MEMBER FUNCTIONS
void display_banner() {
/* code deleted */
}

Poly read_poly(const int label)
{/* code deleted */
}

void display_stats(const Poly & poly, const string & label)
{/* code deleted */
}

void evaluate_poly(const Poly & poly)
{/* code deleted */
}

void goodbye_banner()
{/* code deleted */
}
