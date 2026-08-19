// ============================================================
//        DEFAULT, STATIC AND PRIVATE METHODS IN INTERFACE
// ============================================================
//
// Java 8  → default methods + static methods
// Java 9  → private methods
//
// These features were added to make interfaces more powerful
// and easier to maintain in large applications.
//
// ============================================================


public class Demo5 {

    public static void main(String[] args) {

        // Vehicle is the reference type.
        // Car is the actual object.
        //
        // This is UPCASTING + RUNTIME POLYMORPHISM.

        Vehicle v = new Car();

        // Car does NOT override drive().
        //
        // Therefore Java uses the DEFAULT implementation
        // provided by the Vehicle interface.

        v.drive();


        // ========================================================
        // STATIC INTERFACE METHOD
        // ========================================================

        // Static methods belong to the INTERFACE itself.
        //
        // Therefore call them using the interface name:
        //
        // Vehicle.brake();

        Vehicle.brake();


        // ❌ NOT allowed:
        //
        // v.brake();
        //
        // Static interface methods cannot be called through
        // an implementing class's object/reference.
    }
}


// ============================================================
//                         INTERFACE
// ============================================================

interface Vehicle {


    // ==========================================================
    //                    DEFAULT METHOD
    // ==========================================================
    //
    // Java 8 introduced default methods.
    //
    // A default method:
    //
    //     → has a body
    //     → is automatically public
    //     → can be inherited by implementing classes
    //     → can optionally be overridden
    //
    // Car gets this method automatically because Car implements
    // Vehicle.
    //
    // ==========================================================

    default void drive() {

        System.out.println("Vehicle is driving");

        // Calling the private helper method.
        //
        // Private interface methods can be called from
        // other methods inside the SAME interface.

        accelerate();
    }


    // ==========================================================
    //                    STATIC METHOD
    // ==========================================================
    //
    // Java 8 introduced static methods in interfaces.
    //
    // Static methods belong to the INTERFACE itself.
    //
    // Therefore:
    //
    //     Vehicle.brake();      ✅
    //
    // NOT:
    //
    //     v.brake();            ❌
    //
    // Static interface methods are NOT inherited by
    // implementing classes.
    //
    // ==========================================================

    static void brake() {

        System.out.println("Vehicle is applying brake");
    }


    // ==========================================================
    //                    PRIVATE METHOD
    // ==========================================================
    //
    // Java 9 introduced private methods in interfaces.
    //
    // A private interface method:
    //
    //     → has a body
    //     → is only accessible INSIDE the interface
    //     → cannot be accessed by implementing classes
    //     → is useful for code reuse between default/static methods
    //
    // ==========================================================

    private void accelerate() {

        System.out.println("Vehicle is Accelerating");
    }
}


// ============================================================
//                       IMPLEMENTING CLASS
// ============================================================

class Car implements Vehicle {

    // Car does NOT need to implement drive()
    // because Vehicle already provides a DEFAULT implementation.
    //
    // Therefore this is perfectly valid:
    //
    // class Car implements Vehicle {
    //
    // }
    //
    //
    // Car can also OVERRIDE drive() if it wants its own behaviour:
    //
    // @Override
    // public void drive() {
    //     System.out.println("Car is driving");
    // }
}


// ============================================================
//                       KEY POINTS
// ============================================================
//
// 1. DEFAULT METHOD
//
//    Introduced in Java 8.
//
//    Example:
//
//       default void drive() { ... }
//
//    → Has a body.
//    → Can be inherited.
//    → Can be overridden.
//
//
// ------------------------------------------------------------
//
// 2. STATIC METHOD
//
//    Introduced in Java 8.
//
//    Example:
//
//       static void brake() { ... }
//
//    Call using:
//
//       Vehicle.brake();        ✅
//
//    NOT:
//
//       v.brake();              ❌
//
//    Static interface methods belong to the interface itself.
//
//
// ------------------------------------------------------------
//
// 3. PRIVATE METHOD
//
//    Introduced in Java 9.
//
//    Example:
//
//       private void accelerate() { ... }
//
//    → Only accessible inside Vehicle.
//    → Cannot be accessed from Car.
//    → Useful as a helper method.
//
//
// ------------------------------------------------------------
//
// 4. IMPORTANT DIFFERENCE
//
//    DEFAULT:
//
//       v.drive();
//
//       ↓
//
//       Can be inherited by Car.
//
//
//    STATIC:
//
//       Vehicle.brake();
//
//       ↓
//
//       Belongs to Vehicle.
//       NOT inherited by Car.
//
//
//    PRIVATE:
//
//       accelerate();
//
//       ↓
//
//       Only accessible inside Vehicle.
//
//
// ============================================================
//                  FAANG-STYLE USE CASE
// ============================================================
//
// Imagine a large payment system:
//
// interface Payment {
//
//     default void pay() {
//         validate();
//         System.out.println("Processing payment");
//     }
//
//     private void validate() {
//         System.out.println("Validating payment");
//     }
//
//     static void refund() {
//         System.out.println("Processing refund");
//     }
// }
//
// class CreditCard implements Payment {
//     // Can use default pay()
// }
//
// class UPI implements Payment {
//     // Can use default pay()
// }
//
// ------------------------------------------------------------
//
// DEFAULT → shared implementation
//
// STATIC  → utility operation belonging to interface
//
// PRIVATE → internal helper code used by interface methods
//
// This allows large interfaces to contain reusable logic
// without forcing every implementing class to rewrite it.
//
// ============================================================
