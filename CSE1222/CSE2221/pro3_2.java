import components.simplereader.SimpleReader;
import components.simplereader.SimpleReader1L;
import components.simplewriter.SimpleWriter;
import components.simplewriter.SimpleWriter1L;
import components.utilities.FormatChecker;

public class ABCDGuesser2 {

	/**
	 * Repeatedly asks the user for a positive real number until the user enters
	 * one. Returns the positive real number.
	 * 
	 * @param in
	 *            the input stream
	 * @param out
	 *            the output stream
	 * @return a positive real number entered by the user
	 */
	private static double getPositiveDouble(SimpleReader in, SimpleWriter out) {
		String userInput = "Crap";
		double result = 0;
		while(true) { // code duplication is worse than using break or continue
			out.print("Enter your number: ");
			userInput = in.nextLine();
			if (FormatChecker.canParseDouble(userInput)) {
				result = Double.parseDouble(userInput);
				if (result >= 0)
					return result; //There's only 1 return, thus not multiple return lol 
				else
					out.print("Invalid! Need positive number! ");
			}
			else
				out.print("Invalid! Need number! ");
		}
	}
	  
	/**
	 * Repeatedly asks the user for a positive real number not equal to 1.0
	 * until the user enters one. Returns the positive real number.
	 * 
	 * @param in
	 *            the input stream
	 * @param out
	 *            the output stream
	 * @return a positive real number not equal to 1.0 entered by the user
	 */
	private static double getPositiveDoubleNotOne(SimpleReader in, SimpleWriter out) {
		String userInput = "Crap";
		final double THRESHOLD = 0.00001;
		double result = 0;
		while(true) { 
			out.print("Enter your number: ");
			userInput = in.nextLine();
			if (FormatChecker.canParseDouble(userInput)) {
				result = Double.parseDouble(userInput);
				if (result > 0 && Math.abs(result - 1) > THRESHOLD)
					return result; 
				else
					out.print("Invalid! Need non-one positive number! ");
			}
			else
				out.print("Invalid! Need number! ");
		}
	}
	
	public static void main(String[] args) {
		
		SimpleReader in = new SimpleReader1L();
        SimpleWriter out = new SimpleWriter1L();
        
		double mu;
		double [] wxyz = new double[4];
		int iterator = 0;
		double [] chrm = {-5, -4, -3, -2, -1, -1/2.0, -1/3.0, -1/4.0, 0, 1/4.0, 1/3.0, 1/2.0, 1, 2, 3, 4, 5};
		double [] abcd = new double[4];
		double least = 0;

		mu = getPositiveDouble(in, out);
		while (iterator < wxyz.length) {
			wxyz[iterator] = getPositiveDoubleNotOne(in, out);
			iterator ++;
		}

		for (double a : chrm) {
			double partW = Math.pow(wxyz[0], a);
			for (double b : chrm) {
				double partX = Math.pow(wxyz[1], b);
				for (double c : chrm) {
					double partY = Math.pow(wxyz[2], c);
					for (double d : chrm) {
						double partZ = Math.pow(wxyz[3], d);
						double siml =  partW * partX * partY * partZ;
						if (Math.abs(siml - mu) < Math.abs(least - mu)) {
							least = siml;
							abcd[0] =  a; 
							abcd[1] =  b;
							abcd[2] =  c; 
							abcd[3] =  d;
						}
					}
				}
			}
		}
		
		iterator = 0;
		while (iterator < abcd.length) {
			System.out.print(abcd[iterator] + "  ");
			iterator ++;
		}System.out.println(" ");
		
		System.out.println(least);
		System.out.println((mu - least) / mu);

	}

}
