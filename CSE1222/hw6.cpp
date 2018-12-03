/*
File:          polys.cpp
Created by:    Guoping Chen (chen.8759)
Creation Date: 2 Dec 2018
Synopsis:      A game about polynomial that nobody would actually play
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
{/* returns the coecoefficient */
	return coeff;
}

int Term::getExp() const
{/* returns the exponent  */
	return exp;
}

void Term::setCoeff(const int coefficient)
{/* set the coefficient  */
	coeff = coefficient;
}

void Term::setExp(const int exponent)
{/* set the exponent */
	exp = exponent;
}

double Term::eval(const double x) const
{ /* returns the evaluation of the term given an input valuex;
	x: user input; */
	return getCoeff() * pow(x, getExp());
}

Term Term::derivative() const
{/* returns a new term that is the derivative of the term thefunction is called on */
	Term daenerysTargaryen; // resulting term; Mother of Terms
	daenerysTargaryen.setCoeff(getCoeff() * getExp());
	daenerysTargaryen.setExp(getExp() == 0? 0 : getExp() - 1);
	return daenerysTargaryen;
} // I have to find way to make the comments not useless, sorry to troll the var name

Term Term::multiply(const Term & term) const
{/* returns a new term that is the multiplication of terms;
	term: THE term; */
	Term archon; // resulting term; Merged by 2 Dark Templar or High Templar
	archon.setCoeff(term.getCoeff() * getCoeff());
	archon.setExp(term.getExp() + getExp());
	return archon ;
}

void Term::displayFirst() const
{/* displays a term to the screen formatted as the  rstterm in a polynomial */
	cout << coeff;
	if (exp != 0) cout << "x";
	if (exp > 1) cout << "^" << exp;
}
void Term::displayNext() const
{/* displays a term to the screen formatted as a termafter the  rst term in a polynomial; */
	if (coeff < 0) cout << " - ";
	else cout << " + ";
	cout << abs(coeff);
	if (exp != 0) cout << "x";
	if (exp > 1) cout << "^" << exp;
}

// CLASS POLY MEMBER FUNCTIONS
Term Poly::getTerm(const int index) const
{/* returns the term in the instancel
	index: index */
	return terms[index];
}

int Poly::degree() const
{/* returns the largest exponent in the list; */
	return terms[0].getExp();
}

int Poly::termCount() const
{/* returns the number of terms in the polynomial; */
	int unicorn; // counter; dancing on rainbow
	for (unicorn = 0; terms[unicorn].getExp() != 0; unicorn++);
	return unicorn + 1;
}

void Poly::addTerm(const int coeff, const int exp)
{/* adds a term to the listterms */
	Term tracer; //term to add; The cavalry’s here!
	tracer.setCoeff(coeff);
	tracer.setExp(exp);
	terms.push_back(tracer);
}

void Poly::scale(const int fact)
{/* changes the polynomial by multiplying each term with a scalefactor;
	fact: factor to multiply; */
	for (int i = 0; i < termCount(); i++)
		terms[i].setCoeff(terms[i].getCoeff() * fact);
}// exp is not affected by multiplying, why the hw6 req asks to use `setExp()`?

double Poly::eval(const double x) const
{/* evaluates the polynomial given an input value for variablex;
	x: given input; */
	double recorder(0); // record sum
	for (int i = 0; i < termCount(); i++)
		recorder += (terms[i].getCoeff() * pow(x, terms[i].getExp()));
	return recorder;
}

Poly Poly::derivative() const
{/* returns a polynomial that is the derivative of the polyonmialit is called on */
	Poly theBornKing; //resulting Poly; Legend of Sword
	for (int i = 0; i < termCount(); i++)
		theBornKing.addTerm(terms[i].derivative().getCoeff(),
			terms[i].derivative().getExp());
	return theBornKing;
}

void Poly::display(const string & label) const
{/* prints a label and then prints the polynomial to the screen;
	label: label to print; */
	cout << label;
	terms[0].displayFirst();
	//for (int i = 1; i < termCount(); i++)		cout << terms[i].getCoeff() << " " << terms[i].getExp() << " , ";
	for (int i = 1; i < termCount(); i++)
		if(terms[i].getCoeff() != 0)
			terms[i].displayNext(); 
}

void Poly::displayMultiply(const Poly & poly, const string & label) const
{/* prints a label and then printsthe terms needed to calculate a multiplication of the polynomial;
	poly: polynomial to multiply;
	label: label to print; */
	Poly archons; //resulting Ploy; that, my friend, is many `archon` 
	for (int i = 0; i < termCount(); i++)
		for (int j = 0; j < poly.termCount(); j++)
			archons.addTerm(terms[i].multiply(poly.getTerm(j)).getCoeff(), 
				terms[i].multiply(poly.getTerm(j)).getExp());
	archons.display(label + " : ");
	cout << endl;
}

// NON-MEMBER FUNCTIONS
void display_banner() {
/* prints the welcome banner. */
	cout << "Welcome to fun with polynomials!" << endl;
	cout << "You will enter two polynomials." << endl;
	cout << "Please follow all instructions below." << endl << endl;
}

Poly read_poly(const int label)
{/* prompts and then reads a polynomial from the user one termper line;
	label: which poly to record; */

	bool iDontGiveAShitMode = true; //Whether to quit when encountering invalid input
	Poly weasley; // the main polynomial; cause Weasley Is Our King
	int temp[2], indicator(0); //temp for record, indicator for indexing

	cout << "Enter poly #" << label << ":" << endl;
	while (true) {
		cin >> temp[0] >> temp[1];
		if (!temp[0]) continue;
		if (indicator >= 1 && weasley.getTerm(indicator - 1).getExp() < temp[1]) {
			if (iDontGiveAShitMode) {
				cerr << "Invalid Term. Bye!" << endl;
				exit(1);
			}
			else {
				cout << "That's not right, darling~ \nTry again: " << endl;
				continue;
			}
		}
		weasley.addTerm(temp[0], temp[1]);
		if (!temp[1]) break;
		indicator++;
	}
	return weasley;
}

void display_stats(const Poly & poly, const string & label)
{/* displays information for a polynomial;
	poly: polynomial to display;
	label: label to display; */
	poly.display("You entered polynomial " + label + ": ");
	cout << endl << "The polynomial has degree " << poly.degree() << endl;
	cout << "The polynomial has " << poly.termCount() << " term(s)." << endl;
	cout << "The derivative is: ";
	poly.derivative().display("");
	cout << endl << endl;
}

void evaluate_poly(const Poly & poly)
{/* prompts the user to enter how many values to evaluate;
	poly: polynomial to be evaluated; */
	int time;
	double value;

	cout << "How many times would you like to evaluate polynomial #1? ";
	while (true) {
		cin >> time;
		if (time >= 0) break;
		cout << " Try again. Enter a number greater than or equal to zero: ";
	}
	
	for (int i = 0; i < time; i++) {
		cout << "Enter value to evaluate: ";
		cin >> value;
		cout << "    When x = " << value << " the polynomial evaluates to "
			<< poly.eval(value) << endl;
	}
}

void goodbye_banner()
{/* prints a goodbye message */
	cout << "Thank you for playing!" << endl;
}

// I can only imagine how pain it would be to read 20 codes like this...
// Thank you :D
