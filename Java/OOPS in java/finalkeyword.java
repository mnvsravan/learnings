public class finalkeyword {

    // 1. final instance variable
    final int MAX_SPEED = 120;

    // 2. final static variable (constant)
    static final double PI = 3.14159;

    String name;

    // Constructor
    finalkeyword(String name) {
        this.name = name;
    }

    // 3. final method
    final void displayName() { // like the child or other class can't override this method in the child class if we make it final
        System.out.println("Name: " + name);
    }

    // Normal method
    void displaySpeed() {
        System.out.println("Maximum Speed: " + MAX_SPEED);
    }

    // Static method
    static void displayPI() {
        System.out.println("PI: " + PI);
    }

    public static void main(String[] args) {

        // Creating object
        finalkeyword obj = new finalkeyword("Nitish");

        // Using final instance variable
        System.out.println("Maximum Speed: " + obj.MAX_SPEED);

        // Using final static variable
        System.out.println("PI: " + finalkeyword.PI);

        // Calling final method
        obj.displayName();

        // Calling normal method
        obj.displaySpeed();

        // Calling static method
        finalkeyword.displayPI();


        // ❌ Cannot change final instance variable
        // obj.MAX_SPEED = 200;

        // ❌ Cannot change final static variable
        // finalkeyword.PI = 3.14;
    }
}