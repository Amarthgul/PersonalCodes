package helloWorld;
import java.math.*;

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

		
		// Dump
		if (dump) {
			x += MARK;
			bigNum = bigNum.multiply(bigNum);
			
		}
	}

} 
