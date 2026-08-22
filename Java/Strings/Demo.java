public class Demo {
    public static void main(String[] args) {

        // ============================================================
        //                    STRING CONSTRUCTORS
        // ============================================================

        // Creates an EMPTY String object.
        // Value = ""
        String s1 = new String();


        // Creates a String object containing "Hello".
        // NOTE:
        // Using new String("Hello") explicitly creates a new String object.
        // Usually NOT recommended when you simply need "Hello".
        String s2 = new String("Hello");


        // String literal.
        // "Aditya" is stored in the String Pool.
        // This is the preferred way to create a String.
        String s3 = "Aditya";


        // Creates a NEW String object using the value of s3.
        // s4.equals(s3) → true
        // s4 == s3       → false
        //
        // Usually unnecessary unless you specifically need a separate object.
        String s4 = new String(s3);


        // ============================================================
        //                    CHAR ARRAY → STRING
        // ============================================================

        char[] arr = {
            'A', 'd', 'i', 't', 'y', 'a',
            ' ', 'T', 'a', 'n', 'd', 'o', 'n'
        };

        // Converts the ENTIRE char[] into a String.
        String s5 = new String(arr);

        // IMPORTANT:
        // String is immutable.
        // Changing the original array does NOT change the String.
        //
        // arr[0] = 'B';
        // s5 is still "Aditya Tandon"


        // ============================================================
        //              CHAR ARRAY SUBSET → STRING
        // ============================================================

        // new String(array, offset, count)
        //
        // offset = starting index
        // count  = number of characters
        //
        // arr = A d i t y a ...
        //       0 1 2 3 4 5
        //
        // Starting at index 0, take 6 characters:
        // "Aditya"
        String s6 = new String(arr, 0, 6);


        // ============================================================
        //                    BYTE ARRAY → STRING
        // ============================================================

        byte[] arr2 = {97, 98, 99};

        // ASCII:
        // 97 → 'a'
        // 98 → 'b'
        // 99 → 'c'
        //
        // Start at index 0
        // Take 2 bytes
        //
        // Result → "ab"
        String s7 = new String(arr2, 0, 2);


        // ============================================================
        //              STRINGBUFFER → STRING
        // ============================================================

        StringBuffer sb = new StringBuffer("Hello");

        // Converts StringBuffer → String
        String s8 = new String(sb);

        System.out.println(s8); // Hello
    }
}