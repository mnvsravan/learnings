public class staticclass {

    public static void main(String[] args) {

        // Create an Order
        Order order = new Order("ORD101", "Laptop", 75000);

        // Create Builder object
        Order.Builder builder = new Order.Builder(order);

        // Builder modifies its static data
        Order.Builder.setQuantity(2);
        Order.Builder.setPriority("HIGH");

        // Static method
        Order.Builder.printBuilderCount();

        // Instance method
        builder.printOrder();

        // Outer class accessing Builder
        order.showBuilderDetails();
        System.out.println(order.getTotalOrders());
    }
}


// =====================================================
// OUTER CLASS
// =====================================================

class Order {

    // Instance variables
    private String orderId;
    private String product;
    private int price;


    // Static variable
    private static int totalOrders = 0;


    // Constructor of Order
    Order(String orderId, String product, int price) {

        this.orderId = orderId;
        this.product = product;
        this.price = price;

        totalOrders++;
    }


    // Instance method
    void displayOrder() {

        System.out.println("Order ID : " + orderId);
        System.out.println("Product  : " + product);
        System.out.println("Price    : " + price);
    }


    // Static method
    static int getTotalOrders() {

        return totalOrders;
    }


    // =================================================
    // STATIC NESTED CLASS
    // =================================================

    static class Builder {

        // Reference to Outer class object
        private Order order;


        // Static variables
        private static int quantity;
        private static String priority;

        private static int builderCount = 0;


        // Constructor
        Builder(Order order) {

            this.order = order;

            builderCount++;
        }


        // Static method
        static void setQuantity(int quantity) {

            Builder.quantity = quantity;
        }


        // Static method
        static void setPriority(String priority) {

            Builder.priority = priority;
        }


        // Instance method
        void printOrder() {

            System.out.println();
            System.out.println("===== ORDER =====");

            // Accessing outer class
            // non-static variables through Order object

            System.out.println("Order ID : " + order.orderId);
            System.out.println("Product  : " + order.product);
            System.out.println("Price    : " + order.price);

            System.out.println("Quantity : " + quantity);
            System.out.println("Priority : " + priority);
        }


        // Static method
        static void printBuilderCount() {

            System.out.println(
                "Builders created : " + builderCount
            );
        }


        // Static method
        static int getBuilderCount() {

            return builderCount;
        }
    }


    // =================================================
    // OUTER CLASS ACCESSING BUILDER
    // WITHOUT CREATING OBJECT
    // =================================================

    void showBuilderDetails() {

        System.out.println();
        System.out.println("===== OUTER ACCESS =====");

        // No Builder object created

        System.out.println(
            "Quantity : " + Builder.quantity
        );

        System.out.println(
            "Priority : " + Builder.priority
        );

        System.out.println(
            "Builder Count : " + Builder.builderCount
        );
    }
}

/*
========================================================
        STATIC NESTED CLASS - IMPORTANT PROPERTIES
========================================================

1. A static nested class is a class declared inside another
   class using the 'static' keyword.

2. It belongs to the OUTER CLASS, not to an object of the
   outer class.

3. We can create it without creating an object of the
   outer class.

4. Syntax:
   Outer.Inner obj = new Outer.Inner();

5. A static nested class can have:
   - Instance variables
   - Static variables
   - Instance methods
   - Static methods
   - Constructors
   - Static blocks
   - Instance blocks
   - Other nested classes

6. It can directly access STATIC members of the outer class.

7. It CANNOT directly access NON-STATIC members of the
   outer class.

8. To access a non-static variable of the outer class,
   it needs a reference to an outer-class object.

9. A static nested class does NOT have an automatic
   reference to the outer-class object.

10. It can access private members of the outer class.

11. The outer class can also access private members of
    the static nested class.

12. A static nested class can have its own static variables.

13. A static nested class can have its own instance variables.

14. A static nested class can have constructors.

15. Its constructor executes only when a nested-class
    object is created.

16. Static methods of the nested class can be called
    using the nested class name without creating an object.

17. Instance methods of the nested class require a
    nested-class object.

18. It can implement interfaces.

19. It can extend another class.

20. It can contain another nested class.

21. It can have access modifiers such as:
    - public
    - private
    - protected
    - default

22. It cannot use Outer.this because it does not have an
    automatic outer-object reference.

23. Main advantage:
    It groups a helper/related class inside the outer class
    without creating an unnecessary outer-object reference.

24. Common use cases:
    - Builder Pattern
    - Helper classes
    - Factory classes
    - Request/Response DTOs
    - Utility classes
    - Encapsulation of implementation details

========================================================
                    KEY RULE
========================================================

Static nested class
        |
        |---- Outer static member
        |          → Direct access
        |
        |---- Outer non-static member
                   → Need Outer object reference

========================================================
*/