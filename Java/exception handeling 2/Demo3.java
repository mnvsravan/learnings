public class Demo3 {
    public static void main(String[] args) {
        try {
            //System.out.println( 5 / 0); // new ArithmeticException("/ by zero");
            String s = null;
            s.length();

            Object obj = "Hello";
            Integer i = (Integer) obj; // new ClassCastException()
        }
        // we can use multiple catch blocks and something like this
        catch(ArithmeticException | NullPointerException e) { // this is never recommended
            System.out.println(e.getMessage());
        }
        catch(RuntimeException e) {
            
        }
        catch(Exception e) {
            System.out.println("Some generice Exception");
        }
    }
}
// Java Exception Handling Hierarchy
//
// Object
//   |
//   v
// Throwable
//   |
//   +-------------------+
//   |                   |
//   v                   v
// Error              Exception
//   |                   |
//   |                   +-----------------------+
//   |                   |                       |
//   v                   v                       v
// StackOverflowError  RuntimeException     Checked Exceptions
// OutOfMemoryError        |                       |
//                         |                       +-- IOException
//                         +-- ArithmeticException +-- SQLException
//                         +-- NullPointerException
//                         +-- ArrayIndexOutOfBoundsException
//                         +-- NumberFormatException
//
// -------------------------------------------------------
//
// Error:
// - Serious problems
// - Usually not handled by the programmer
//
// Exception:
// - Problems that can usually be handled
//
// RuntimeException:
// - Unchecked exception
// - Compiler does NOT force us to handle it
//
// Checked Exception:
// - Compiler checks them
// - Must be handled using try-catch OR declared using throws
//
// -------------------------------------------------------
//
// Example:
//
// int a = 10 / 0;
// -> ArithmeticException
//
// String s = null;
// s.length();
// -> NullPointerException
//
// FileReader f = new FileReader("abc.txt");
// -> FileNotFoundException (Checked Exception)