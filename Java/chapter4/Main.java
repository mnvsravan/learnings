import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int size;
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the size of the array: ");
        size = input.nextInt();

        int[] arr = new int[size];
        // int[] arr={....} also fine

        for (int i = 0; i < size; i++) {
            System.out.print("Enter element " + (i + 1) + ": ");
            arr[i] = input.nextInt();
        }

        System.out.println("Array elements are:");
        for (int i = 0; i < size; i++) {
            System.out.println(arr[i]);
        }




        // 2D
        int[][] ar = {
    {1, 2, 3, 4},
    {54, 54, 23}
}; // or int[][]arr = new int[2][4] 
for(int i=0;i<ar.length;i++){
    for(int j=0;j<ar[i].length;j++){
        System.out.println(ar[i][j]);
    }
}






// simple question
 int rows;
        int cols;
        
        System.out.println("Enter rows: ");
        rows=input.nextInt();
         System.out.println("Enter cols: ");
        cols=input.nextInt();
        int[][] brr= new int[rows][cols];
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
           System.out.println("Enter value: ");
            brr[i][j]=input.nextInt();
            }
        }
         System.out.println("Printing array: ");
          for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
            System.out.println(brr[i][j]);
            
            }
        }



        
    }
}