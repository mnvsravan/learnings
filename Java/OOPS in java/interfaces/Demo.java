// ============================================================
//                    INTERFACE EXAMPLE
// ============================================================

public class Demo {

    public static void main(String[] args) {

        // Payment is the INTERFACE type (reference type)
        // DebitCard is the actual OBJECT created.
        //
        // This is UPCASTING:
        // Payment p = new DebitCard();
        //
        // The reference is of type Payment,
        // but the actual object is DebitCard.

        Payment p = new DebitCard();

        // Calls DebitCard's pay() method.
        // This is RUNTIME POLYMORPHISM / DYNAMIC METHOD DISPATCH.
        p.pay();
    }
}


// ============================================================
//                         INTERFACE
// ============================================================

interface Payment {

    // Methods inside an interface are:
    //     public + abstract
    // by default.
    //
    // So this:
    //     void pay();
    //
    // is actually treated as:
    //     public abstract void pay();
    //
    // We normally don't write public abstract because
    // Java provides them automatically.

    void pay();
}


// ============================================================
//                    CREDIT CARD CLASS
// ============================================================

class CreditCard implements Payment {

    // CreditCard MUST implement pay()
    // because Payment contains an abstract method pay().
    //
    // IMPORTANT:
    // The interface method is PUBLIC.
    // Therefore, the overriding method CANNOT have
    // weaker access.
    //
    // So this is CORRECT:
    //     public void pay()
    //
    // But this is WRONG:
    //     void pay()
    //
    // because package-private/default access is weaker
    // than public.

    @Override
    public void pay() {

        System.out.println("Paying via credit card");
    }
}


// ============================================================
//                    DEBIT CARD CLASS
// ============================================================

class DebitCard implements Payment {

    // Again, Payment.pay() is public.
    // Therefore the overriding method must also be public.

    @Override
    public void pay() {

        System.out.println("Paying via debit card");
    }
}


// ============================================================
//                       KEY POINTS
// ============================================================
//
// 1. An interface is used to define a CONTRACT.
//
// 2. Interface methods are public and abstract by default
//    (unless they are default/static/private methods).
//
// 3. A class uses "implements" to implement an interface.
//
// 4. A class implementing an interface must provide
//    implementations for its abstract methods.
//
// 5. An interface method is public, so the overriding method
//    must also be public.
//
// 6. You CANNOT reduce visibility while overriding:
//
//       public  -> public       ✅
//       public  -> protected    ❌
//       public  -> default      ❌
//       public  -> private      ❌
//
// 7. This:
//
//       Payment p = new DebitCard();
//
//    demonstrates polymorphism.
//
// 8. p.pay() executes DebitCard's pay() because the actual
//    object is a DebitCard.
//
// ============================================================