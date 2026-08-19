// ============================================================
//              JAVA RESOLUTION PRIORITY RULE
// ============================================================
//
// When a class inherits the SAME method from:
//
//     1. A superclass
//     2. An interface's default method
//
// Java gives PRIORITY to the CLASS method.
//
//
//
// GENERAL PRIORITY:
//
//     CLASS METHOD
//          ↓
//     INTERFACE DEFAULT METHOD
//
// A class method wins over an interface default method.
//
// ============================================================


public class Demo7 {

    public static void main(String[] args) {

        C c = new C();

        c.fun();

        // Output:
        // Inside C class
    }
}


// ============================================================
//                    INTERFACE A
// ============================================================
//
// A provides a DEFAULT implementation of fun().
//
// ============================================================

interface A {

    default void fun() {

        System.out.println("Inside A interface");
    }
}


// ============================================================
//                     CLASS B
// ============================================================
//
// B provides a normal class method fun().
//
// ============================================================

class B {

    public void fun() {

        System.out.println("Inside B class");
    }
}


// ============================================================
//                     CLASS C
// ============================================================
//
// C:
//
//     extends B
//     implements A
//
// Therefore C receives:
//
//     B.fun()  → class method
//     A.fun()  → default interface method
//
// Both have the SAME method signature.
//
//
//
// Java's resolution rule says:
//
//     CLASS METHOD > INTERFACE DEFAULT METHOD
//
// So B.fun() gets priority over A.fun().
//
// ============================================================

class C extends B implements A {

    @Override
    public void fun() {

        System.out.println("Inside C class");

        // u can even do-->
        super.fun();
        A.super.fun();
    }
}


// ============================================================
//                       KEY POINTS
// ============================================================
//
// 1. JAVA GIVES PRIORITY TO CLASS METHODS.
//
//
//       class method
//            ↑
//          wins
//            ↑
//       interface default method
//
//
// 2. Here:
//
//       B.fun()
//       A.fun()
//
//    both have fun().
//
//
//
// 3. B is a CLASS, while A is an INTERFACE.
//
//    Therefore:
//
//       B.fun() wins over A.fun().
//
//
//
// 4. C overrides fun() itself.
//
//    Therefore C.fun() gets the HIGHEST EFFECTIVE PRIORITY.
//
//
//       C.fun()
//          ↓
//       B.fun()
//          ↓
//       A.default fun()
//
//    The actual method called is:
//
//       C.fun()
//
//
// ============================================================
//          WHAT IF C DOES NOT OVERRIDE fun()?
// ============================================================
//
// We can write:
//
//     class C extends B implements A {
//
//     }
//
//
//
// This is still VALID.
//
// Why?
//
// Because B already provides a concrete class method:
//
//     B.fun()
//
// The class method wins over A's default method.
//
//
//
// So:
//
//     C c = new C();
//     c.fun();
//
// Output:
//
//     Inside B class
//
// ============================================================
//                 VERY IMPORTANT RULE
// ============================================================
//
// Remember:
//
//     CLASS > INTERFACE
//
// If a superclass has a method and an interface has a
// default method with the same signature:
//
//     superclass method WINS.
//
//
//
// This rule helps Java avoid ambiguity when combining
// class inheritance with interface inheritance.
//
// ============================================================
//                  FAANG-STYLE EXAMPLE
// ============================================================
//
// interface Payment {
//
//     default void process() {
//         System.out.println("Generic payment");
//     }
// }
//
// class CreditCardPayment {
//
//     public void process() {
//         System.out.println("Credit card payment");
//     }
// }
//
// class AmazonPayment extends CreditCardPayment
//                         implements Payment {
//
//     // CreditCardPayment.process()
//     // wins over Payment.process()
// }
//
// ------------------------------------------------------------
//
// This rule is useful in large systems where interfaces
// provide default behaviour, but an existing superclass
// already defines a concrete implementation.
//
// ============================================================