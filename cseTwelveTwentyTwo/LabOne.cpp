  cout << "Enter a character: ";
	cin >> character;
	cout << "Enter value for double value x: ";
	cin >> x;
	cout << "Enter value for integer value y: ";
	cin >> y;
	cout << "Enter value for integer value z: ";
	cin >> z;

	cout << endl << "Your character is " << character << endl;
	cout << "Your value for x is " << x << endl;
	cout << "Your value for y is " << y << endl;
	cout << "Your value for z is " << z << endl << endl;

	cout << "The reciprocal of x is " << 1 / x << endl; //x is double type
	cout << "x/z is " << x / z << endl; //x is double type
	cout << "x + y + z is " << x + y + z << endl << endl; //x is double type

	cout << "The reciprocal of y is " << 1.0 / y << endl; //implicit conversion
	cout << "The reciprocal of z is " << 1.0 / z << endl; 
	cout << "y/z is " << y / z << endl; //apperantly integer devide
	cout << "y modulus z is " << y % z << endl;
