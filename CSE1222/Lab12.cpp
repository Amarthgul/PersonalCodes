/*
  File:           triangles.cpp
  Created by:     Guoping Chen (chen.8759)
  Creation Date:  25 Nov 2018 (I gotta be honest)
  Synopsis:       calculate and display the attributes of 
                  a right triangle
*/

#include <iostream>
#include <cmath>

using namespace std;

class Point
{
private:
	double px;
	double py;

public:
	void setX(const double x);
	void setY(const double y);
	double getX() const;
	double getY() const;
};

class Triangle
{
private:
	Point blPoint;
	double length, height;

public:
	// member functions
	void setBottomLeftX(const double x);
	void setBottomLeftY(const double y);
	void setLength(const double inLength);
	void setHeight(const double inHeight);

	Point getBottomLeft() const;
	Point getBottomRight() const;
	Point getTopLeft() const;
	double getLength() const;
	double getHeight() const;

	double perimeter() const;
	double hypotenuse() const;
	void scaleLength(const double sx);
	void scaleHeight(const double sy);
	void display() const;
};

// FUNCTION PROTOTYPES GO HERE:
void read_triangle(Triangle & tri);

int main()
{
	// Define local variables
	Triangle tri;
	double sx, sy;

	//Prompt the user for triangle information and fill Class Triangle object, tri,
	//with this information
	read_triangle(tri);

	// Display triangle information
	tri.display();

	// Prompt and read scale factors to change length and height
	cout << "Enter scale factor in x direction: ";
	cin >> sx;

	cout << "Enter scale factor in y direction: ";
	cin >> sy;

	// Apply scale factors
	tri.scaleLength(sx);
	tri.scaleHeight(sy);

	// Display triangle information
	tri.display();

	return 0;
}

// FUNCTION DEFINITIONS GO HERE:

// CLASS MEMBER FUNCTION DEFINITINOS GO HERE:

void Point::setX(const double x)
{
	px = x;
}

void Point::setY(const double y)
{
	py = y;
}

double Point::getX() const
{
	return (px);
}

double Point::getY() const
{
	return (py);
}

void Triangle::setBottomLeftX(const double x)
{/*  Set Bottom Left X;
     x: Bottom Left X  */
	blPoint.setX(x);
}

void Triangle::setBottomLeftY(const double y)
{/*  Set Bottom Left Y;
     y: Bottom Left Y  */
	blPoint.setY(y);
}

void Triangle::setLength(const double inLength)
{/*  Set Length;
     x: length  */
	length = inLength;
}

void Triangle::setHeight(const double inHeight)
{/*  Set Height;
     x: height  */
	height = inHeight;
}

Point Triangle::getBottomLeft() const
{/*   Get Bottom Left Point Coordinates; */
	return blPoint;
}

Point Triangle::getBottomRight() const
{/*   Get Bottom Right Point Coordinates; */
	Point brp; // Bottom Right Point
	brp.setX(blPoint.getX() + length);
	brp.setY(blPoint.getY());
	return brp;
}

Point Triangle::getTopLeft() const
{/*   Get Top Left Point Coordinates; */
	Point tlp; // Top Left Point
	tlp.setX(blPoint.getX());
	tlp.setY(blPoint.getY() + height);
	return tlp;
}

double Triangle::getLength() const
{ /*   Get Length; */
	return length;
}

double Triangle::getHeight() const
{/*    Get Height; */
	return height;
}

double Triangle::hypotenuse() const
{/*   Get hypotenuse; */
	return sqrt(length * length + height * height);
}

double Triangle::perimeter() const
{/*    Get perimeter; */
	return hypotenuse() + height + length;
}

void Triangle::scaleLength(const double scalefact)
{/*  Scale Length;
	 scalefact: Scale Factor */
	setLength(getLength() * scalefact);
}

void Triangle::scaleHeight(const double scalefact)
{/*  Scale Height;
	 scalefact: Scale Factor */
	setHeight(getHeight() * scalefact);
}

void Triangle::display() const
{/*  Display attributes; */
	cout << endl << std::string(40, '-') << endl;
	cout << "Lower Left Vertex ("<< getBottomLeft().getX() <<", " <<
	  getBottomLeft().getY() << ")" << endl;
	cout << "Top Left Vertex (" << getTopLeft().getX() << ", " <<
	  getTopLeft().getY() << ")" << endl;
	cout << "Bottom Right Vertex (" << getBottomRight().getX() << ", " <<
  	  getBottomRight().getY() << ")" << endl;
	cout << "Hypotenuse = " << hypotenuse() << endl;
	cout << "Perimeter = " << perimeter() << endl;
	cout << std::string(40, '-') << endl << endl;
}

void read_triangle(Triangle & tri)
{/*  Read Triangle; 
	 tri: target triangle */
	double temp;
	cout << "Enter bottom left x coordinate: ";
	cin >> temp;
	tri.setBottomLeftX(temp);
	cout << "Enter bottom left y coordinate: ";
	cin >> temp;
	tri.setBottomLeftY(temp);
	cout << "Enter length: ";
	cin >> temp;
	tri.setLength(temp);
	cout << "Enter height: ";
	cin >> temp;
	tri.setHeight(temp);
}
