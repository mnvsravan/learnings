import java.util.Scanner;
public class basics01 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in); // Swaping
        int num1,num2,temp;
        System.out.print("Enter number 1: ");
        num1 = input.nextInt();
        System.out.print("Enter number 2: ");
        num2 = input.nextInt();
        temp = num1;
        num1 = num2;
        num2 = temp;
        System.out.println("After swapping: Number 1 = " + num1 + ", Number 2 = " + num2);
        
        // arthemetic operations
        int a,b;
        System.out.print("Enter first number: ");
        a = input.nextInt();
        System.out.print("Enter second number: ");
        b = input.nextInt();
        System.out.println("Addition: " + (a + b)); // same with /,*,% etc

        // Just like C we can use +=,-=,*=,/=,%= operators in Java as well and ++i i++ and all;
        
    }
}
    

