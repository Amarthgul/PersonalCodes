package helloWorld;
import java.math.*; //import all in .math
import java.util.Scanner;

public class HelloWorld {
	
	public static void main(String[] args) {	
		/* Initializing */
		int x = 0;
		boolean dump = true;
		byte biteMe = 1; //in between -127 ~ 128
		BigInteger bigNum = new BigInteger("1242423231"); //big
		double [] randList = new double [10]; //list
		randList[0] = (double)biteMe; //casting
		final int MARK = 3; //constant 
		
		/* operating */
		Scanner in = new Scanner(System.in);
		System.out.print("Say some int f: "); //same as `cpp cout`
		x = in.nextInt();
		System.out.print("Say some flost f: ");
		randList[0] = in.nextDouble();
		System.out.printf("Int: %5d, float: %.2f", x, randList[0]); //format print

		
		// Dump
		if (dump) {
			x += MARK;
			bigNum = bigNum.multiply(bigNum);
		}
	}

} 
