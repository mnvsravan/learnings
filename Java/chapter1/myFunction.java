import java.util.Scanner;
public class myFunction {
    public static void main(String[] args) {
        int number = 5;
        System.out.println("The number is: " + number);
        float decimal = 5.5f; // we use f to indicate that it is a float
        System.out.println("The decimal number is: " + decimal); // EVEN IF ONE OPERATOR IS STRING WE CAN USE CONCATENATION
        double precision = 5.555555555555555; // we use double for higher precision
        System.out.println("The double precision number is: " + precision);
        boolean isTrue = true; // boolean can be true or false
        System.out.println("The boolean value is: " + isTrue);
        char letter = 'A'; // char is used for single characters
        System.out.println("The character is: " + letter);
        String text = "Hello, World!"; // String is used for text
        System.out.println("The string is: " + text);

        // Taking user input
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = input.nextLine(); // we use nextLine() if input is a string or characters
        System.out.print("Enter your age: ");
        int age = input.nextInt(); // we use nextInt() if input is integer , similary for nextFloat() and nextDouble() for float and double respectively
        System.out.println("Hello, " + name + "! You are " + age + " years old.");
    }
}
