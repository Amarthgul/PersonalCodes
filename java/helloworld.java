/* This program is created to help people with other programming experiences
 * (c++, python, etc.) to get familiar with java ASAP  
*/

package helloWorld; // include helloWorld.java and helloWorldPlus.java
// or to say all classes under helloWorld package 
import java.math.*; //import all classes in java.math
import java.util.Scanner; //impoer a single class
import java.util.Random; //used in method `basicBranchAndLoops` to generate random number
import javax.swing.JOptionPane; //used in `callingGUIforIO` 

public class HelloWorld {
	
	public static int recorder = 0; // Class attributes
	protected static int insider; // can only be accessed by code in this package 
	
	public static void basicDatatype() {
		boolean typeBool = true;   // boolean datatype
		Boolean classBool = false; // boolean class
		int anInteger = 0; //basic integer
		long aLong = 123456789; // large number
		byte aByte = (byte)anInteger;  //byte, range -128~127; (DATATYPE) is a way to cast
		// Variable aByte would be 0
		double aDouble = 3.14;  // basic float
		char aChara = '1';  // basic char
		String aStr = Long.toString(aLong); // string class cast a double to Sting
		// Variable aStr would be "123456789"
		final int CONST = Integer.parseInt(aStr); // `final` is the java keyword for constant;
		// Variable CONST would be 123456789
		double [] uncertainList = new double [10]; //java array
		double [] certainList = {0.0, 0.1, 0.2, 0.3, 0.5}; // cannot be used as return value
		double [] comboList = new double [] {0.0, 0.1, 0.2, 0.3, 0.5}; // can be used as return value
		BigInteger bigNum = new BigInteger("1242423231");    //larger number
		BigDecimal bigDec = new BigDecimal("3.14159265354"); //large float
		
		System.out.println("Finished");
	}
	
	public static void basicConsoleIO() {
		Scanner in = new Scanner(System.in); // declare a scanner for user input	
		System.out.print("This is static method `print`, "); // same as `cpp cout`
		System.out.print("followed with another `print`. \n Enter an integer: "); // no auto-newline
		int input = in.nextInt(); //read from scanner
		//Also declaration can be done aside from function/method top
		/* other scanner methods:
		 *    float:          SCANNER.nextFloat();
		 *    double:         SCANNER.nextDouble();
		 *    String:         SCANNER.next();     // reads next word, stops at space
                              SCANNER.nextLine(); // reads next line, stops at \n
              etc.
		*/
		/* Confirm whethwe user input is certain input:
		 *    int:            SCANNER.hasNextInt()
		 *    float:          SCANNER.hasNextFloat()
		 *    String:         SCANNER.hasNextLine()
		 *    double:         SCANNER.hasNextDouble()
		 *    byte:           SCANNER.hasNextByte()
		 *    etc.
		 * */
		System.out.printf("You entered %5d.\n", input); // format output
		in.close(); // Scanner should be closed after using
		System.out.println("Okay"); // next `println` will be in a newline
		System.out.println("All over"); // short cut: `sysout` then press Ctrl+Space
	}
	
	public static void callingGUIforIO() {
		String input = JOptionPane.showInputDialog("Enter name:"); //GUI interface
		System.out.print("Omae Wa Mou Shindeiru! " + input + "!"); // concatenate Strings
		// Still output in console 
	}

	public static int basicBranchAndLoops(int iterator) { // argument `iterator` passed by value
		Random rand = new Random(); // a random instance 
		int n = rand.nextInt(50);   // generate a number between 0~49
		while(n < 100) { // `do {...} while(...);` also applies
			System.out.println(n);
			n = n > 60 ? n + 5 : n * 2; // conditional snetence
		}
		
		for(int i = 1; i <= iterator; i++) { //same `for` as c and c++
			if (n > 101 && n < 1000) { /* operator `&&` and `||`,
			Still obeys the Short Circuit rule */
				n *= i;
				System.out.println(n);
			}
			else continue; // `continue` and `break` 
		}
		
		String [] names = {"Miyamoto Musashi", "Onna no Shinkan", "Junko"};
		for(String name : names) { // iterate name through names
			System.out.println(name);
		}
		
		return 0;
	}

 	public static void main(String[] args) {	
		HelloWorld.basicBranchAndLoops(5);
	}
}



