public class Demo {

    public static void main(String[] args) {

        int a = 5;
        int b = 0;

        // ============================================================
        // STACK:
        //
        //        main()
        //
        // main() is the first method called by the JVM.
        //
        // try-catch is present here, so main() is capable of handling
        // an exception that reaches it from methodA() or methodB().
        // ============================================================

        try {

            System.out.println("Inside main TRY");

            methodA(a, b);

            // If methodA() returns normally, this statement executes.
            System.out.println("main TRY - After methodA");

        }
        catch (ArithmeticException e) {

            // This executes ONLY if an ArithmeticException reaches main()
            // without being handled by methodA() or methodB().

            System.out.println("main CATCH");

            // Prints the exception information and call stack.
            e.printStackTrace();
        }

        // ============================================================
        // IMPORTANT:
        //
        // This is OUTSIDE the try-catch.
        //
        // If the exception was handled by the catch block, execution
        // continues from here.
        // ============================================================

        System.out.println("main - After TRY-CATCH");
    }


    private static void methodA(int a, int b) {

        // ============================================================
        // STACK:
        //
        //        methodA()   <-- CURRENT
        //        main()
        //
        // methodA() has its OWN try-catch.
        // ============================================================

        try {

            System.out.println("Inside methodA TRY");

            methodB(a, b);

            // This executes ONLY if methodB() finishes normally.
            System.out.println("methodA TRY - After methodB");

        }
        catch (ArithmeticException e) {

            // If methodB() throws ArithmeticException and this catch
            // matches it, the exception is HANDLED HERE.
            //
            // Once this catch handles the exception, the exception
            // does NOT continue propagating to main().
            //
            // This is the most important concept here.

            System.out.println("methodA CATCH");

            e.printStackTrace();
        }

        // ============================================================
        // Since methodA() handled the exception above, execution
        // continues HERE.
        //
        // This statement WILL execute after the catch.
        // ============================================================

        System.out.println("methodA - After TRY-CATCH");
    }


    private static void methodB(int a, int b) {

        // ============================================================
        // STACK:
        //
        //        methodB()   <-- CURRENT
        //        methodA()
        //        main()
        //
        // methodB() also has its OWN try-catch.
        // ============================================================

        try {

            System.out.println("Inside methodB TRY");

            // 5 / 0
            //
            // ArithmeticException occurs HERE.
            int result = a / b;

            // This statement is NEVER executed because the exception
            // happened before it could be reached.

            System.out.println("Result = " + result);

        }
        catch (ArithmeticException e) {

            // ========================================================
            // EXCEPTION IS CAUGHT HERE.
            //
            // The JVM DOES NOT continue executing the remaining
            // statements inside the try block.
            //
            // Instead:
            //
            //      exception
            //          ↓
            //      matching catch
            //          ↓
            //      catch executes
            //
            // Because methodB() handled the exception itself,
            // the exception STOPS HERE.
            //
            // It does NOT propagate to methodA() or main().
            // ========================================================

            System.out.println("methodB CATCH");

            e.printStackTrace();
        }

        // ============================================================
        // This is AFTER the try-catch.
        //
        // Therefore, it WILL execute after the catch finishes.
        // ============================================================

        System.out.println("methodB - After TRY-CATCH");
    }
}
    