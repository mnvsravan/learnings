// ============================================================
//                    DIAMOND PROBLEM
// ============================================================
//
// The DIAMOND PROBLEM occurs when a class gets the same method
// through multiple inheritance paths.
//
// Java avoids the problem by forcing the implementing class
// to resolve the ambiguity.
//
//
//
//                       A
//                      / \
//                     B   C
//                      \ /
//                       D
//
// D inherits from BOTH B and C.
//
// B → fun() prints "B"
// C → fun() prints "C"
//
// So Java asks:
//
//     "Which fun() should D use?"
//
// D MUST resolve the conflict by overriding fun().
//
// ============================================================


public class Demo6 {

    public static void main(String[] args) {

        D d = new D();

        // D provides its own implementation of fun().
        //
        // Therefore there is NO ambiguity.

        d.fun();
    }
}


// ============================================================
//                    TOP INTERFACE
// ============================================================

interface A {

    // Abstract method.
    //
    // Automatically:
    //
    // public abstract void fun();

    void fun();
}


// ============================================================
//                    INTERFACE B
// ============================================================
//
// B extends A.
//
// B provides a DEFAULT implementation of fun().
//
// ============================================================

interface B extends A {

    @Override
    default void fun() {

        System.out.println("B");
    }
}


// ============================================================
//                    INTERFACE C
// ============================================================
//
// C ALSO extends A.
//
// C provides its own DEFAULT implementation of fun().
//
// ============================================================

interface C extends A {

    @Override
    default void fun() {

        System.out.println("C");
    }
}


// ============================================================
//                     CLASS D
// ============================================================
//
// D implements BOTH B and C.
//
// Now D receives two possible default implementations:
//
//     B.fun() → "B"
//     C.fun() → "C"
//
// Java cannot automatically choose one.
//
// Therefore D MUST override fun().
//
// ============================================================

class D implements B, C {

    @Override
    public void fun() {

        // D explicitly decides which implementation to use.
        System.out.println("D");
    }
}


// ============================================================
//                       KEY POINTS
// ============================================================
//
// 1. DIAMOND STRUCTURE:
//
//              A
//             / \
//            B   C
//             \ /
//              D
//
//
// 2. B and C both extend A.
//
//
// 3. B and C both provide a default implementation of fun().
//
//
// 4. D implements both B and C.
//
//
// 5. D now has TWO possible fun() implementations:
//
//       B.fun()
//       C.fun()
//
//
// 6. Java does NOT randomly choose one.
//
//    Instead, D MUST override fun().
//
//
// 7. Therefore:
//
//       class D implements B, C {
//
//           @Override
//           public void fun() {
//               System.out.println("D");
//           }
//       }
//
//    resolves the ambiguity.
//
//
// ============================================================
//              WHAT IF D DOES NOT OVERRIDE?
// ============================================================
//
// If we write:
//
//     class D implements B, C {
//     }
//
//
//
// Java gives a COMPILATION ERROR because both B and C
// provide conflicting default implementations of fun().
//
//
// ============================================================
//              CAN D CHOOSE B OR C INSTEAD?
// ============================================================
//
// YES.
//
// D can explicitly call a particular interface's default
// implementation:
//
//     B.super.fun();
//
// or:
//
//     C.super.fun();
//
// Example:
//
//     class D implements B, C {
//
//         @Override
//         public void fun() {
//
//             B.super.fun();
//         }
//     }
//
// Output:
//
//     B
//
//
// ============================================================
//                  FAANG-STYLE EXAMPLE
// ============================================================
//
// Imagine:
//
// interface Logger {
//     default void log() {
//         System.out.println("Generic logging");
//     }
// }
//
// interface FileLogger extends Logger {
//     default void log() {
//         System.out.println("Logging to file");
//     }
// }
//
// interface CloudLogger extends Logger {
//     default void log() {
//         System.out.println("Logging to cloud");
//     }
// }
//
// class Application implements FileLogger, CloudLogger {
//
//     @Override
//     public void log() {
//
//         // Application decides which behaviour it wants.
//         FileLogger.super.log();
//     }
// }
//
// ------------------------------------------------------------
//
// Application
//       ↓
// FileLogger + CloudLogger
//       ↓
// Both have log()
//
// Java forces Application to resolve the conflict.
//
// This prevents unpredictable behaviour.
//
// ============================================================
