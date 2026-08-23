public class Demo4 {

    public static void main(String[] args) {

        int age = -5;

        if (age < 0) {

            // throw = actually throws an exception
            throw new IllegalArgumentException("Age cannot be negative");
        }

        System.out.println("Valid age");
    }
}