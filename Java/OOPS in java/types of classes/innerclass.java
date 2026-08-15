public class innerclass {

    public static void main(String[] args) {

        Order order = new Order(
            "ORD101",
            "Laptop",
            75000
        );

        Order.Payment payment = order.new Payment("UPI");

        payment.pay(74999);
        payment.showPayment();

        order.showOrder();
    }
}

class Order {

    private String orderId;
    private String product;
    private int price;

    private static int totalOrders = 0;

    Order(String orderId, String product, int price) {

        this.orderId = orderId;
        this.product = product;
        this.price = price;

        totalOrders++;
    }

    class Payment {

        private String method;
        private double amount;
        private String status;

        private static int paymentCount = 0;

        Payment(String method) {   // unlike static we dont need to do like Order order and all to access outter class vcariables this is done default

            this.method = method;
            this.status = "PENDING";

            paymentCount++;
        }

        void pay(double amount) {

            this.amount = amount;

            if (this.amount == Order.this.price) {
                this.status = "SUCCESS";
            } else {
                this.status = "FAILED";
            }
        }

        void showPayment() {

            System.out.println();
            System.out.println("===== PAYMENT =====");

           System.out.println("Order ID : " + orderId);
            System.out.println("Product  : " + product);
            System.out.println("Price    : " + price);

            System.out.println("Amount   : " + this.amount);
            System.out.println("Method   : " + this.method);
            System.out.println("Status   : " + this.status);

            System.out.println(
                "Payments : " + Payment.paymentCount
            );
        }
    }

    void showOrder() {

        System.out.println();
        System.out.println("===== ORDER =====");

        System.out.println("Order ID : " + orderId);
        System.out.println("Product  : " + product);
        System.out.println("Price    : " + price);

        System.out.println(
            "Total Orders : " + totalOrders
        );
    }
}

/*
========================================================
       INNER CLASS vs STATIC NESTED CLASS
========================================================

1. OUTER OBJECT
   -----------------------------------------------------
   Inner Class:
   → Requires an Outer class object.

   Static Nested Class:
   → Does NOT require an Outer class object.


2. CREATING OBJECT
   -----------------------------------------------------
   Inner Class:
   → outer.new Inner()

   Static Nested Class:
   → new Outer.Inner()


3. OUTER CLASS INSTANCE VARIABLES
   -----------------------------------------------------
   Inner Class:
   → Can directly access outer class's
     non-static variables.

   Static Nested Class:
   → Cannot directly access outer class's
     non-static variables.


4. OUTER OBJECT REFERENCE
   -----------------------------------------------------
   Inner Class:
   → Automatically has a reference to its
     outer object.

   Static Nested Class:
   → Has NO automatic outer-object reference.


5. OUTER STATIC VARIABLES
   -----------------------------------------------------
   Both can directly access static variables
   of the outer class.


6. OUTER PRIVATE MEMBERS
   -----------------------------------------------------
   Both can access private members of the
   outer class.

   But:

   Inner Class:
   → Can directly access outer instance members.

   Static Nested Class:
   → Needs an Outer object reference to access
     outer instance members.


7. Outer.this
   -----------------------------------------------------
   Inner Class:
   → Can use Outer.this.

   Static Nested Class:
   → Cannot use Outer.this.


8. DEPENDENCY
   -----------------------------------------------------
   Inner Class:
   → Strongly associated with a particular
     Outer object.

   Static Nested Class:
   → Associated with the Outer class itself,
     not a particular object.


9. MEMORY / REFERENCE
   -----------------------------------------------------
   Inner Class:
   → Internally maintains a reference to the
     Outer class object.

   Static Nested Class:
   → Does not automatically maintain an
     Outer class object reference.


10. INSTANCE CREATION
    ----------------------------------------------------
    Inner Class:
    → Cannot exist independently of an
      Outer object.

    Static Nested Class:
    → Can exist independently of an
      Outer object.


11. USE CASE
    ----------------------------------------------------
    Inner Class:
    → Use when the nested class needs data
      from a particular Outer object.

    Static Nested Class:
    → Use when the nested class is logically
      related to the Outer class but does not
      need a particular Outer object.


12. THIS KEYWORD
    ----------------------------------------------------
    Inner Class:

        this
        ↓
        Inner class object

        Outer.this
        ↓
        Outer class object


    Static Nested Class:

        this
        ↓
        Static nested class object

        Outer.this
        ↓
        NOT AVAILABLE


13. STATIC MEMBERS
    ----------------------------------------------------
    Both Inner Class and Static Nested Class
    can have their own:

    → static variables
    → static methods
    → instance variables
    → instance methods
    → constructors


14. MOST IMPORTANT RULE
    ----------------------------------------------------

    INNER CLASS
          ↓
    Automatically connected to
    an Outer object
          ↓
    Can directly access
    Outer instance variables


    STATIC NESTED CLASS
          ↓
    No automatic Outer object
          ↓
    Cannot directly access
    Outer instance variables


========================================================
              EASY MEMORY TRICK
========================================================

INNER CLASS
    = "I belong to an OBJECT"

STATIC NESTED CLASS
    = "I belong to a CLASS"


========================================================
              ONE-LINE DIFFERENCE
========================================================

Inner Class:
"Give me an Outer OBJECT."

Static Nested Class:
"Give me the Outer CLASS."

========================================================
*/