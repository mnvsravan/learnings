public class Demo2 {

    public static void main(String[] args) {

        // ============================================================
        //             ACCESSING INTERFACE VARIABLES
        // ============================================================

        // Interface variables can be accessed directly using
        // the interface name.
        //
        // MathConstant.PI_VALUE
        //
        // No object is required.

        System.out.println(MathConstant.PI_VALUE);


        // We can also access it through a class that implements
        // the interface, although using the interface name is
        // preferred:
        //
        // Random r = new Random();
        // System.out.println(r.PI_VALUE);
    }
}


// ============================================================
//                    VARIABLES IN INTERFACE
// ============================================================

interface MathConstant {

    // IMPORTANT:
    // Every variable declared inside an interface is
    // automatically:
    //
    //     public
    //     static
    //     final
    //
    // So:
    //
    // double PI_VALUE = 3.14;
    //
    // is actually:
    //
    // public static final double PI_VALUE = 3.14;


    double PI_VALUE = 3.14;

    int VALUE = 10;


    // ============================================================
    // Because variables are FINAL:
    //
    // PI_VALUE = 3.14159;   // ❌ ERROR
    //
    // VALUE = 20;           // ❌ ERROR
    //
    // Once assigned, their values CANNOT be changed.
    // ============================================================


    // Interface methods are public abstract by default
    // (unless they are default, static, or private methods).
    //
    // void fun();
}


// ============================================================
//                  IMPLEMENTING THE INTERFACE
// ============================================================

class Random implements MathConstant {

    // Random automatically gets access to the constants
    // PI_VALUE and VALUE because it implements MathConstant.
    //
    // But these variables still belong to the INTERFACE.
    //
    // They are NOT instance variables of Random.


    // If fun() were declared in the interface:
    //
    // @Override
    // public void fun() {
    //     System.out.println(PI_VALUE);
    // }
}


// ============================================================
//                       KEY POINTS
// ============================================================
//
// INTERFACE VARIABLES ARE:
//
//     public + static + final
//
// Example:
//
//     int VALUE = 10;
//
// actually means:
//
//     public static final int VALUE = 10;
//
// ------------------------------------------------------------
//
// WHY static?
//
// Because the variable belongs to the interface itself,
// not to individual objects.
//
// Access using:
//
//     MathConstant.VALUE
//
// ------------------------------------------------------------
//
// WHY final?
//
// Because interface variables are constants.
// Their value cannot be changed.
//
//     MathConstant.VALUE = 20;   // ❌ ERROR
//
// ------------------------------------------------------------
//
// WHY public?
//
// Interface members are public by default.
//
// ------------------------------------------------------------
//
// IMPORTANT:
//
// You don't need to create an object:
//
//     MathConstant m = new Random();  // unnecessary
//
// Simply:
//
//     System.out.println(MathConstant.PI_VALUE);
//
// ============================================================
