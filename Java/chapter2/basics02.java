import java.util.Scanner;
public class basics02 {
public static void main(String[] args){
// if else and all are like c only even the else if and all, same with relational and logical
Scanner input= new Scanner(System.in);
int num;
System.out.print("Enter number: ");
num= input.nextInt();
if(num>0){
    System.out.println("Number is positive");
}
else if(num<0){
    System.out.println("Number is negative");
}
else{
    System.out.println("Number is zero");

}
// question 2
int num1,num2,num3;
System.out.print("Enter number 1: ");
num1= input.nextInt();
System.out.print("Enter number 2: ");
num2= input.nextInt();
System.out.print("Enter number 3: ");
num3= input.nextInt();
if(num1>num2 && num1>num3){
    System.out.println("Number 1 is greatest");
}
else if(num2>num1 && num2>num3){
    System.out.println("Number 2 is greatest");
}
else{
    System.out.println("Number 3 is greatest");
}
 //3
 //switch case in java is also same as c, but in java we can use string in switch case as well
 String day;
 System.out.print("Enter day: ");
    day= input.nextLine();
    switch(day){
        case "Monday":
            System.out.println("Today is day 1");
            break;
        case "Tuesday":
            System.out.println("Today is day 2");
            break;
        case "Wednesday":
            System.out.println("Today is day 3");
            break;
        case "Thursday":
            System.out.println("Today is day 4");
            break;
        case "Friday":
            System.out.println("Today is day 5");
            break;
        case "Saturday":
            System.out.println("Today is day 6");
            break;
        case "Sunday":
            System.out.println("Today is day 7");
            break;
        default:
            System.out.println("Invalid day");
    }







}
}
