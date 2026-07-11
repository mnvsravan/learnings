import java.util.Scanner;
public class question {
    public static void main(String[] args) {
        String name;
        System.out.print("Enter your name: ");
        Scanner input = new Scanner(System.in);
        name = input.nextLine();
        int age;
        System.out.print("Hello " + name + "! , Enter your age: ");
        age=input.nextInt();
        System.out.println("Hello " + name + "! , You are " + age + " years old"+" and welcome to Java!!!");

    }
}

