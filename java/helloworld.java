/* This program is created to help people with other programming experiences
 * (c++, python, etc.) get familiar with java quickly  
*/

package helloWorld;
import java.math.*; //import all classes in java.math
import java.util.Scanner; //impoer a single class
import java.util.Random;

import javax.swing.JOptionPane;

public class HelloWorld {
	
	public static void main(String[] args) {	
		HelloWorld.basicBranchAndLoops();
	}
	
	public static void basicDatatype() {
		boolean typeBool = true;   // boolean datatype
		Boolean classBool = false; // boolean class
		int anInteger = 0; //basic integer
		byte aByte = 127;  //byte, range -128~127
		double aFloat = 3.14;  // basic float
		char aChara = 'A';  // basic char
		String aStr = "Miyamoto Musashi"; // string class, no need to import library
		final int CONST = 3; // `final` is the java keyword for constant
		double [] randList = new double [10]; //java array
		BigInteger bigNum = new BigInteger("1242423231");    //large number
		BigDecimal bigDec = new BigDecimal("3.14159265354"); //large float
		
	}
	
	public static void basicConsoleIO() {
		Scanner in = new Scanner(System.in); // declare a scanner for user input	
		System.out.print("This is static method `print`, "); // same as `cpp cout`
		System.out.print("followed with another `print`. \n Enter an integer: "); // no auto-newline
		int input = in.nextInt(); //read from scanner
		//Also declaration can be done aside from function/method top
		/* other scanner methods:
		 *    float:          SCANNER.nextDouble();
		 *    String:         SCANNER.next();
		*/
		System.out.printf("You entered %5d.\n", input); // format output
		in.close(); // Scanner should be closed after using
		System.out.println("Okay"); // next `println` will be in a newline
		System.out.println("All over");
	}
	
	public static void callingGUIforIO() {
		String input = JOptionPane.showInputDialog("Enter name:"); //GUI interface
		System.out.print("Omae Wa Mou Shindeiru! " + input + "!"); // concatenate Strings
		// Still output in console 
	}

	public static int basicBranchAndLoops() {
		Random rand = new Random(); // a random instance 
		int n = rand.nextInt(50);   // generate a number between 0~49
		while(n < 100) {
			System.out.println(n);
			n = n > 60 ? n + 5 : n * 2; // conditional snetence
		}
		
		for(int i = 0; i < 5; i++) { //same `for` as c and c++
			if (n > 110 && n < 1000) { /* operator `&&` and `||`,
			Still obeys the Short Circuit rule */
				n *= i;
			}
			else continue; // `continue` and `break` 
		}
		return n;
	}
} 



