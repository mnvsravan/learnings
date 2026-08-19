// ============================================================
//              MULTIPLE INHERITANCE USING INTERFACES
// ============================================================
//
// Java does NOT support multiple inheritance using classes.
//
// ❌ class C extends A, B
//
// But Java DOES support multiple inheritance through interfaces.
//
// ✅ class C implements A, B
//
// A class can implement MULTIPLE interfaces.
//
// ============================================================


public class Demo3 {

    public static void main(String[] args) {

        // Creating a GoogleEmployee object
        GoogleEmployee employee = new GoogleEmployee();

        employee.code();
        employee.manage();
    }
}


// ============================================================
//                    INTERFACE 1
// ============================================================
//
// Interface Developer represents the behaviour of a developer.
//
// An interface defines WHAT a class should do,
// not HOW it should do it.
//
// ============================================================

interface Developer {

    // Automatically:
    // public abstract void code();

    void code();
}


// ============================================================
//                    INTERFACE 2
// ============================================================
//
// Interface Manager represents the behaviour of a manager.
//
// ============================================================

interface Manager {

    void manage();
}


// ============================================================
//              MULTIPLE INHERITANCE
// ============================================================
//
// GoogleEmployee implements BOTH:
//
//     Developer
//     Manager
//
// Therefore GoogleEmployee gets the contract of both interfaces.
//
// This is Java's way of achieving MULTIPLE INHERITANCE.
//
// ============================================================

class GoogleEmployee implements Developer, Manager {

    // Must implement Developer.code()
    //
    // The method in the interface is public,
    // so the implementation MUST also be public.

    @Override
    public void code() {

        System.out.println("Writing production-quality code");
    }


    // Must implement Manager.manage()

    @Override
    public void manage() {

        System.out.println("Managing the engineering team");
    }
}


// ============================================================
//                      KEY POINTS
// ============================================================
//
// 1. Java DOES NOT support:
//
//       class C extends A, B
//
//    because multiple class inheritance can create ambiguity.
//
//
// 2. Java DOES support:
//
//       class C implements A, B
//
//    because interfaces provide contracts.
//
//
// 3. A class can implement ANY NUMBER of interfaces:
//
//       class C implements A, B, C, D
//
//
//
// 4. Each interface can define different behaviours.
//
//       Developer → code()
//       Manager   → manage()
//
//    GoogleEmployee must provide implementations for BOTH.
//
//
// 5. Interface methods are public by default.
//
//    Therefore:
//
//       public void code()      ✅
//
//    but:
//
//       void code()             ❌
//       protected void code()   ❌
//       private void code()     ❌
//
//
// 6. Multiple inheritance through interfaces is useful when
//    one class needs capabilities from multiple roles.
//
//    Example:
//
//       class GoogleEmployee implements Developer, Manager
//
//    The employee can BOTH:
//
//       → develop software
//       → manage a team
//
// ============================================================


// ============================================================
//               FAANG-STYLE REAL-WORLD EXAMPLE
// ============================================================
//
// Think about a company like Google, Amazon, Meta, Apple, etc.
//
// An employee may have multiple responsibilities.
//
// For example:
//
//     SoftwareEngineer
//          ↓
//     Can code
//          +
//     Can review code
//
// We can model these independent capabilities using interfaces.
//
// ============================================================


// interface Coder {
//     void code();
// }
//
// interface CodeReviewer {
//     void reviewCode();
// }
//
// class SoftwareEngineer implements Coder, CodeReviewer {
//
//     @Override
//     public void code() {
//         System.out.println("Writing scalable backend services");
//     }
//
//     @Override
//     public void reviewCode() {
//         System.out.println("Reviewing pull requests");
//     }
// }
//
// ============================================================
//
// ONE CLASS
//     ↓
// implements
//     ↓
// Coder + CodeReviewer
//
// This is MULTIPLE INHERITANCE THROUGH INTERFACES.
//
// ============================================================
