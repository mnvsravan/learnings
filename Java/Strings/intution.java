

public class intution {
    public static void main(String[] args) {

        // =========================================================
        // 1. STRING LITERAL
        // =========================================================

        String s1 = "Hello";
        String s2 = "Hello";

        // "Hello" is a STRING LITERAL.
        //
        // String literals are stored in the STRING POOL.
        //
        // When s2 = "Hello" is created, Java checks the String Pool.
        // "Hello" already exists, so Java REUSES the same object.
        //
        // Memory:
        //
        //        String Pool
        //        +---------+
        // s1 --->| "Hello"  |
        // s2 --->|          |
        //        +---------+
        //
        // Therefore, s1 and s2 point to the SAME object.

        System.out.println(s1 == s2);    // true

        // == compares REFERENCES for objects.
        // Here both references point to the same object.


        // =========================================================
        // 2. STRING CREATED USING new
        // =========================================================

        String s3 = new String("Aditya");
        String s4 = new String("Aditya");

        // new String() explicitly creates a NEW String object.
        //
        // Even though both contain "Aditya", two different objects
        // are created.
        //
        // Conceptually:
        //
        //        Heap
        //
        // s3 ---> [ "Aditya" ]
        //
        // s4 ---> [ "Aditya" ]
        //
        // These are TWO DIFFERENT OBJECTS.
        //
        // Therefore, s3 and s4 have different references.

        System.out.println(s3 == s4);    // false

        // == checks whether s3 and s4 refer to the SAME object.
        // They don't, so the result is false.


        // =========================================================
        // 3. == VS equals() cuz this can be overided
        // =========================================================

        // == 
        // For objects → compares REFERENCES.
        // It asks:
        // "Are these two references pointing to the same object?"
        //
        // equals()
        // For String → compares CONTENT.
        // It asks:
        // "Do these two Strings contain the same characters?"

        System.out.println(s3.equals(s4)); // true

        // s3 and s4 are different objects,
        // BUT both contain "Aditya".
        // Therefore equals() returns true.


        // =========================================================
        // 4. VERY IMPORTANT INTERVIEW EXAMPLE
        // =========================================================

        String a = "Hello";
        String b = new String("Hello");

        // a points to the String Pool object.
        //
        // b points to a NEW object created in the Heap.
        //
        // Therefore:
        //
        // a == b          → false
        // a.equals(b)     → true

        System.out.println(a == b);       // false
        System.out.println(a.equals(b));  // true


        // =========================================================
        // 5. STRING IMMUTABILITY
        // =========================================================

        String x = "Hello";

        x.concat(" World");

        // String is IMMUTABLE.
        //
        // concat() does NOT modify the existing "Hello" object.
        // Instead, it creates a NEW String.
        //
        // Since we didn't store the returned String,
        // x still points to "Hello".

        System.out.println(x); // Hello


        // To actually change what x refers to:

        x = x.concat(" World");

        // Now x points to the NEW String "Hello World".

        System.out.println(x); // Hello World


        // =========================================================
        // 6. COMPILE-TIME STRING CONCATENATION
        // =========================================================

        String p = "Hel" + "lo";
        String q = "Hello";

        // Both "Hel" and "lo" are String literals.
        //
        // The compiler can evaluate:
        //
        // "Hel" + "lo"
        //      ↓
        //   "Hello"
        //
        // Therefore p and q point to the same pooled object.

        System.out.println(p == q); // true


        // =========================================================
        // 7. RUNTIME CONCATENATION
        // =========================================================

        String first = "Hel";
        String second = "lo";

        String r = first + second;
        String t = "Hello";

        // first and second are variables.
        // Their concatenation happens at RUNTIME.
        //
        // Therefore r is generally a newly created String,
        // rather than simply referring to the pooled "Hello".

        System.out.println(r == t);       // false
        System.out.println(r.equals(t));  // true


        // =========================================================
        // 8. intern()
        // =========================================================

        String u = new String("Java");
        String v = "Java";

        // u → new String object
        // v → String Pool object
        //
        // Therefore:
        //
        // u == v → false

        System.out.println(u == v); // false

        // intern() returns the pooled/canonical String
        // corresponding to the same content.

        System.out.println(u.intern() == v); // true


        // =========================================================
        // 9. WHY IS String IMMUTABLE?
        // =========================================================

        // String immutability provides several benefits:
        //
        // 1. String Pool can safely share objects.
        //
        // 2. Improves security because String values cannot
        //    unexpectedly change.
        //
        // 3. Strings are thread-safe because their state
        //    cannot be modified.
        //
        // 4. Strings are commonly used as HashMap/HashSet keys.
        //    Their hash value remains stable because their content
        //    cannot change.


        // =========================================================
        // 10. MOST IMPORTANT INTERVIEW RULES
        // =========================================================

        // String literal
        //       ↓
        // String Pool
        //
        // new String()
        //       ↓
        // New object
        //
        // == 
        //       ↓
        // Compares references
        //
        // equals()
        //       ↓
        // Compares String contents
        //
        // String
        //       ↓
        // Immutable
        //
        // intern()
        //       ↓
        // Returns pooled String representation
    }
}

