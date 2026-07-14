import java.util.Scanner;
public class bitwise {
    public static void main(String[] args){
// The bitwise operators are same as C
int num1,num2;
Scanner input=new Scanner(System.in);
num1=input.nextInt();
num2=input.nextInt();

System.out.println(num1 & num2);
System.out.println(num1 | num2);
System.out.println(num1 ^ num2);
System.out.println(~num2);
System.out.println(num2 >> 3);
System.out.println(num1<<3);

// How to check if a number is even or odd
// if its even then last digit is 0 if odd then its 1 , so if we do & with 1 then we get last digit
int number=input.nextInt();
if((number&1)!=0){
    System.out.println("its odd");
}
else{
    System.out.println("its even");
}







    }
}
