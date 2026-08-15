public class ananymousclass {

    public static void main(String[] args) {

        Payment payment = new Payment() {

            private double amount = 75000;

            @Override
            void pay() {

                System.out.println(
                    "Paid ₹" + amount + " using UPI"
                );
            }

            @Override
            void refund() {

                System.out.println(
                    "Refunding ₹" + amount
                );
            }
        };

        payment.pay();
        payment.refund();
// we must use the methods which are there in class only so only @override stuff gets executed
// but we can create methods among in ananymouse class it self and call it in the overide

// EG:
Payment m = new Payment() {

    private double money = 1000000;

    @Override
    void pay() {

        greet();   // ✅
        System.out.println("Paid amount of " + money);
    }

    void greet() {

        System.out.println("HELLO BRO");
    }

    void bye() {

        System.out.println("BYE BRO");
    }

    @Override
    void refund() {

        System.out.println(
            "Refunded " + (money - 10000)
        );

        bye();     // ✅
    }
};
         m.pay();
        m.refund();
    }
}


abstract  class Payment {

    abstract void pay();

    abstract void refund();
}

/*
========================================================
                ANONYMOUS CLASS
========================================================

1. An anonymous class is a class without a name.

2. It is declared and instantiated at the same time.

3. It is mainly used when we need a class implementation
   only once.

4. Syntax:

   Parent obj = new Parent() {

       // class body

   };


5. An anonymous class can:
   - Extend a class
   - Implement an interface
   - Override methods
   - Have instance variables
   - Have instance methods
   - Have instance initialization blocks

6. An anonymous class CANNOT have a constructor because
   it does not have a class name.

7. It can access variables from the surrounding scope.

8. Local variables accessed from an anonymous class
   must be final or effectively final.

9. Every time we write:

       new Parent() { ... }

   we are creating a new anonymous class implementation.

10. Multiple anonymous classes can extend the same parent
    class but have completely different implementations.

11. Anonymous classes are useful for:
    - One-time implementations
    - Event handling
    - Callbacks
    - Runnable / Threads
    - GUI programming
    - Legacy Java APIs

12. Anonymous class vs Normal class:

    Normal class:
        class Payment extends Transaction {
            ...
        }

    Anonymous class:
        Payment p = new Payment() {
            ...
        };


13. Anonymous class vs Lambda:

    Anonymous class:
    → Can have multiple methods and instance variables.

    Lambda:
    → Mainly used for functional interfaces
      having one abstract method.

14. Anonymous class does NOT require a separate .java file.

15. Anonymous class can access private/protected/public
    members according to normal Java access rules.

========================================================
                KEY IDEA
========================================================

Anonymous class means:

    "I need a class implementation here,
     but I don't need to give that class a name."

========================================================
*/