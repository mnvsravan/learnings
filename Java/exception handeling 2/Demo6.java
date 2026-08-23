/*
 * ============================================================
 *                  THROW vs THROWS
 * ============================================================
 *
 * 1. throw
 * ------------------------------------------------------------
 * throw is used to ACTUALLY throw an exception.
 *
 * Syntax:
 *
 *     throw new Exception("message");
 *
 * FANNG LEVEL:
 * Think of "throw" as an ACTION.
 *
 *     throw → "Something went wrong RIGHT NOW!"
 *
 *
 * 2. throws
 * ------------------------------------------------------------
 * throws is used in a METHOD DECLARATION to tell the caller
 * that the method MAY throw an exception.
 *
 * Syntax:
 *
 *     void test() throws Exception
 *
 * FANNG LEVEL:
 * Think of "throws" as a WARNING/DECLARATION.
 *
 *     throws → "Caller, be prepared. I may throw this!"
 *
 *
 * ============================================================
 *              THROW vs THROWS — SIDE BY SIDE
 * ============================================================
 *
 * throw
 *   ↓
 * Used INSIDE method body
 *   ↓
 * Actually throws exception
 *   ↓
 * Followed by an exception OBJECT
 *
 * Example:
 *
 *     throw new Exception("Invalid age");
 *
 *
 * throws
 *   ↓
 * Used in METHOD DECLARATION
 *   ↓
 * Declares possible exceptions
 *   ↓
 * Followed by exception CLASS NAME
 *
 * Example:
 *
 *     void checkAge() throws Exception
 *
 *
 * ============================================================
 *                    DIFFERENT EXAMPLES
 * ============================================================
 *
 *
 * Example 1: throw
 *
 *     if (age < 0) {
 *         throw new IllegalArgumentException("Invalid age");
 *     }
 *
 * Here:
 *     throw = ACTUALLY throws the exception
 *
 *
 *
 * Example 2: throws
 *
 *     static void readFile() throws IOException {
 *         FileReader file = new FileReader("data.txt");
 *     }
 *
 * Here:
 *     throws = DECLARES that IOException may occur
 *
 *
 * ============================================================
 *              THROW + THROWS IN ONE PROGRAM
 * ============================================================
 */

public class Demo6 {

    public static void main(String[] args) {

        try {

            // FANNG NOTE:
            // main() calls checkAge().
            //
            // checkAge() has "throws InvalidAgeException",
            // so the caller (main) must handle it using
            // try-catch OR declare it using throws.
            checkAge(-5);

        }
        catch (InvalidAgeException e) {

            // FANNG NOTE:
            // The exception thrown inside checkAge()
            // reaches this catch block.
            System.out.println(e.getMessage());
            System.out.println("You litrally entered"+e.getAge());
        }
    }


    // =========================================================
    // throws → DECLARATION
    // =========================================================

    // FANNG NOTE:
    // "throws" tells the CALLER:
    //
    // "This method MAY throw InvalidAgeException."
    //
    // It does NOT actually throw the exception here.
    static void checkAge(int age)
            throws InvalidAgeException {

        if (age < 0) {

            // =================================================
            // throw → ACTUAL ACTION
            // =================================================

            // FANNG NOTE:
            // "throw" ACTUALLY throws the exception object.
            //
            // new InvalidAgeException(...)
            //        ↓
            // creates an exception object
            //
            // throw
            //        ↓
            // sends that object to the caller
            throw new InvalidAgeException(
                    "Age cannot be negative",age);
        }

        System.out.println("Valid age");
    }
}


/*
 * ============================================================
 *                  CUSTOM EXCEPTION
 * ============================================================
 */

class InvalidAgeException extends Exception {
    private int age;

    public InvalidAgeException(String message,int age) {

        // FANNG NOTE:
        // Passes the message to the parent Exception class.
        //
        // Therefore:
        //
        // e.getMessage()
        //       ↓
        // returns "Age cannot be negative"
        super(message);
        this.age=age;
    }
    public int getAge(){
        return this.age;

    }
}


/*
 * ============================================================
 *                  PROGRAM FLOW
 * ============================================================
 *
 * main()
 *   |
 *   | checkAge(-5)
 *   ↓
 *
 * checkAge()
 *   |
 *   | "throws InvalidAgeException"
 *   |       ↓
 *   | Declares possible exception
 *   |
 *   | age < 0
 *   ↓
 *
 * throw new InvalidAgeException(...)
 *   |
 *   | ACTUALLY throws exception
 *   ↓
 *
 * catch (InvalidAgeException e)
 *   |
 *   ↓
 *
 * Exception handled
 *
 *
 * ============================================================
 *                 MOST IMPORTANT DIFFERENCE
 * ============================================================
 *
 * throw
 *   → ACTION
 *   → Actually throws an exception
 *   → Used inside method body
 *   → Followed by exception OBJECT
 *
 * throws
 *   → DECLARATION
 *   → Tells caller about possible exception
 *   → Used in method declaration
 *   → Followed by exception CLASS NAME
 *
 *
 * ============================================================
 *                 EASY MEMORY TRICK
 * ============================================================
 *
 * throw  → "THROW IT!"
 *
 * throws → "WARNING: I MAY THROW IT!"
 *
 */
