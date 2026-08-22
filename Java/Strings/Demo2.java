public class Demo2 {
    public static void main(String[] args) {

        String s1 = "Aditya";
        String s2 = "abc";


        // ============================================================
        // LENGTH / EMPTINESS
        // ============================================================

        System.out.println(s1.length());          // 6
        System.out.println(s1.isEmpty());         // false
        System.out.println(s1.isBlank());         // false
        System.out.println("   ".isBlank());      // true


        // ============================================================
        // CHARACTER ACCESS
        // ============================================================

        System.out.println(s1.charAt(2));         // i

        char[] arr = s1.toCharArray();

        for (char c : arr) {
            System.out.print(c + " ");
        }
        // A d i t y a

        System.out.println();


        // ============================================================
        // COMPARISON
        // ============================================================

        System.out.println(s1.equals(s2));        // false
        System.out.println("ADITYA".equalsIgnoreCase("aditya")); // true

        System.out.println("Apple".compareTo("Banana"));  // negative
        System.out.println("Banana".compareTo("Apple"));  // positive
        System.out.println("Apple".compareTo("Apple"));   // 0


        // ============================================================
        // SEARCHING
        // ============================================================

        System.out.println(s1.contains("ity"));       // true

        System.out.println(s1.indexOf("ity"));        // 2

        System.out.println("Aditya Aditya".lastIndexOf("Aditya")); // 7

        System.out.println(s1.startsWith("Ad"));      // true

        System.out.println(s1.endsWith("ya"));        // true


        // ============================================================
        // SUBSTRING
        // ============================================================

        System.out.println(s1.substring(1));          // ditya

        System.out.println(s1.substring(1, 4));       // dit


        // ============================================================
        // CASE CONVERSION
        // ============================================================

        System.out.println(s1.toUpperCase());         // ADITYA

        System.out.println(s1.toLowerCase());         // aditya


        // ============================================================
        // WHITESPACE
        // ============================================================

        System.out.println("   Hello   ".trim());     // Hello

        System.out.println("   Hello   ".strip());    // Hello


        // ============================================================
        // REPEAT
        // ============================================================

        System.out.println(s1.repeat(3));
        // AdityaAdityaAditya


        // ============================================================
        // REPLACE
        // ============================================================

        System.out.println(s1.replace("ity", "abc"));
        // Adabca

        System.out.println(s1.replaceAll("Ad", "Ab"));
        // Abitya


        // ============================================================
        // SPLIT
        // ============================================================

        String s3 = "Aditya-Rohit-Rohan";

        String[] names = s3.split("-");

        for (String name : names) {
            System.out.println(name);
        }

        /*
        Aditya
        Rohit
        Rohan
        */


        // ============================================================
        // JOIN
        // ============================================================

        System.out.println(String.join("-", "a", "b", "c"));
        // a-b-c


        // ============================================================
        // VALUE OF
        // ============================================================

        String s4 = String.valueOf(10);

        System.out.println(s4);
        // 10


        // ============================================================
        // GET BYTES
        // ============================================================

        byte[] bytes = s1.getBytes();

        for (byte b : bytes) {
            System.out.print(b + " ");
        }

        // 65 100 105 116 121 97

        System.out.println();


        // ============================================================
        // INTERN
        // ============================================================

        String s5 = new String("Hello");

        String s6 = s5.intern();

        System.out.println(s5 == s6);        // false


        // ============================================================
        // FORMAT
        // ============================================================

        String name = "Aditya";
        int age = 28;

        System.out.println(
            String.format("Hello %s, your age is %d", name, age)
        );

        // Hello Aditya, your age is 28
    }
}