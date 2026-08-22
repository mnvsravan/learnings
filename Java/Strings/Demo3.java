public class Demo3 {
    public static void main(String[] args) {

        // ============================================================
        //                      STRINGBUILDER
        // ============================================================

        /*
         * StringBuilder is MUTABLE.
         *
         * Unlike String, modifications happen on the SAME object.
         *
         * String:
         *     String s = "Hello";
         *     s = s + " World";
         *
         *     → creates another String object
         *
         * StringBuilder:
         *     sb.append(" World");
         *
         *     → modifies the existing StringBuilder object
         *
         * StringBuilder is NOT synchronized / NOT thread-safe.
         * Therefore, it is generally faster than StringBuffer.
         *
         * Use StringBuilder when multiple String modifications
         * are required in normal single-threaded programs.
         */

        StringBuilder sb = new StringBuilder();


        // ============================================================
        //                         append()
        // ============================================================

        /*
         * Adds data to the END of the StringBuilder.
         *
         * append() is overloaded, so it can accept:
         * String, int, char, boolean, double, etc.
         */

        sb.append("Aditya");
        sb.append(" Tandon");
        sb.append(28);
        sb.append('A');
        sb.append(true);

        System.out.println(sb);
        // Aditya Tandon28Atrue


        // ============================================================
        //                         insert()
        // ============================================================

        /*
         * Inserts data at a specified index.
         *
         * insert(index, value)
         */

        StringBuilder sb1 = new StringBuilder("AdityaTandon");

        sb1.insert(6, " Kumar");

        System.out.println(sb1);
        // Aditya KumarTandon


        // ============================================================
        //                         delete()
        // ============================================================

        /*
         * delete(start, end)
         *
         * start → INCLUDED
         * end   → EXCLUDED
         *
         * [start, end)
         */

        StringBuilder sb2 = new StringBuilder("AdityaTandon");

        sb2.delete(6, 12);

        System.out.println(sb2);
        // Aditya


        // ============================================================
        //                      deleteCharAt()
        // ============================================================

        /*
         * Deletes ONE character at the specified index.
         */

        StringBuilder sb3 = new StringBuilder("Aditya");

        sb3.deleteCharAt(2);

        System.out.println(sb3);
        // Adita


        // ============================================================
        //                         replace()
        // ============================================================

        /*
         * replace(start, end, String)
         *
         * Replaces characters from start to end-1.
         */

        StringBuilder sb4 = new StringBuilder("Aditya");

        sb4.replace(1, 4, "XYZ");

        System.out.println(sb4);
        // AXYZa


        // ============================================================
        //                         reverse()
        // ============================================================

        /*
         * Reverses the entire sequence of characters.
         */

        StringBuilder sb5 = new StringBuilder("Aditya");

        sb5.reverse();

        System.out.println(sb5);
        // aytidA


        // ============================================================
        //                         charAt()
        // ============================================================

        /*
         * Returns the character at the specified index.
         *
         * Indexing starts from 0.
         */

        StringBuilder sb6 = new StringBuilder("Aditya");

        System.out.println(sb6.charAt(2));
        // i


        // ============================================================
        //                       setCharAt()
        // ============================================================

        /*
         * Replaces the character at a specified index.
         */

        StringBuilder sb7 = new StringBuilder("Aditya");

        sb7.setCharAt(2, 'X');

        System.out.println(sb7);
        // AdXtya


        // ============================================================
        //                         length()
        // ============================================================

        /*
         * Returns the number of characters currently stored.
         */

        StringBuilder sb8 = new StringBuilder("Aditya");

        System.out.println(sb8.length());
        // 6


        // ============================================================
        //                       capacity()
        // ============================================================

        /*
         * capacity() tells us how much storage is currently available
         * before the StringBuilder needs to resize its internal array.
         *
         * IMPORTANT:
         *
         * length   → actual characters
         * capacity → allocated storage
         */

        StringBuilder sb9 = new StringBuilder();

        System.out.println(sb9.capacity());
        // 16


        /*
         * Default capacity:
         *
         * 16
         *
         * When more capacity is required, Java generally grows it using:
         *
         * newCapacity = oldCapacity * 2 + 2
         *
         * Example:
         *
         * 16 → 34 → 70 → 142 → ...
         */


        // ============================================================
        //                     ensureCapacity()
        // ============================================================

        /*
         * Ensures that the capacity is AT LEAST the specified value.
         *
         * It does NOT necessarily make capacity exactly that value.
         */

        StringBuilder sb10 = new StringBuilder();

        sb10.ensureCapacity(100);

        System.out.println(sb10.capacity());
        // At least 100


        // ============================================================
        //                      trimToSize()
        // ============================================================

        /*
         * Reduces the capacity to the current length.
         *
         * Useful when you no longer expect the StringBuilder
         * to grow and want to reduce unused storage.
         */

        StringBuilder sb11 = new StringBuilder("Hello");

        System.out.println(sb11.capacity());
        // 21

        sb11.trimToSize();

        System.out.println(sb11.capacity());
        // 5


        // ============================================================
        //                       substring()
        // ============================================================

        /*
         * Returns a portion of the StringBuilder as a STRING.
         *
         * IMPORTANT:
         *
         * substring() does NOT return StringBuilder.
         *
         * start → INCLUDED
         * end   → EXCLUDED
         */

        StringBuilder sb12 = new StringBuilder("AdityaTandon");

        String result = sb12.substring(0, 6);

        System.out.println(result);
        // Aditya


        // ============================================================
        //                        indexOf()
        // ============================================================

        /*
         * Returns the index of the FIRST occurrence of a substring.
         *
         * Returns -1 if the substring is not found.
         */

        StringBuilder sb13 = new StringBuilder("AdityaTandon");

        System.out.println(sb13.indexOf("Tandon"));
        // 6

        System.out.println(sb13.indexOf("XYZ"));
        // -1


        // ============================================================
        //                     lastIndexOf()
        // ============================================================

        /*
         * Returns the index of the LAST occurrence.
         */

        StringBuilder sb14 = new StringBuilder("abcabc");

        System.out.println(sb14.lastIndexOf("abc"));
        // 3


        // ============================================================
        //                       toString()
        // ============================================================

        /*
         * Converts StringBuilder → String.
         *
         * This is very commonly used when you finish building
         * a String and need an actual String object.
         */

        StringBuilder sb15 = new StringBuilder();

        sb15.append("Hello");
        sb15.append(" World");

        String str = sb15.toString();

        System.out.println(str);
        // Hello World
    }
}


/*
======================================================================
                    STRING vs STRINGBUILDER
======================================================================

String
------
→ IMMUTABLE
→ Cannot be modified after creation
→ Operations that appear to modify it create/return another String
→ Good when the value does not need repeated modification


StringBuilder
------------
→ MUTABLE
→ Same object can be modified
→ NOT synchronized
→ NOT thread-safe
→ Faster than StringBuffer in normal single-threaded situations
→ Preferred for repeated String modifications


======================================================================
                    STRINGBUFFER vs STRINGBUILDER
======================================================================

StringBuilder
-------------
→ Mutable
→ Not synchronized
→ Not thread-safe
→ Faster
→ Preferred for most normal programs / LeetCode


StringBuffer
------------
→ Mutable
→ Synchronized
→ Thread-safe
→ Usually slower than StringBuilder


IMPORTANT:
The major methods are basically the same:

append()
insert()
delete()
deleteCharAt()
replace()
reverse()
charAt()
setCharAt()
length()
capacity()
ensureCapacity()
trimToSize()
substring()
indexOf()
lastIndexOf()
toString()


So you DO NOT need to learn the methods twice.

Learn them using StringBuilder.

Then remember:

StringBuilder → faster, not synchronized
StringBuffer  → synchronized, thread-safe


======================================================================
                         CAPACITY
======================================================================

StringBuilder sb = new StringBuilder();

Default capacity = 16


If more capacity is required:

new capacity = old capacity * 2 + 2


Example:

16
 ↓
34
 ↓
70
 ↓
142


======================================================================
                    LENGTH vs CAPACITY
======================================================================

length()
→ Number of actual characters


capacity()
→ Amount of storage currently available


Example:

StringBuilder sb = new StringBuilder("Hello");

length   = 5
capacity = 21


Why?

Default capacity = 16

16 + length of "Hello" (5)

= 21


======================================================================
                     ensureCapacity()
======================================================================

sb.ensureCapacity(100);

→ Ensures capacity is at least 100.

It does NOT mean:

capacity == 100


======================================================================
                      trimToSize()
======================================================================

sb.trimToSize();

→ Reduces capacity to current length.


Example:

StringBuilder sb = new StringBuilder("Hello");

Before:

length   = 5
capacity = 21

After:

sb.trimToSize();

length   = 5
capacity = 5


======================================================================
                         MUTABILITY
======================================================================

String:

String s = "Hello";

s.concat(" World");

System.out.println(s);

Output:

Hello


Because String is immutable.


StringBuilder:

StringBuilder sb = new StringBuilder("Hello");

sb.append(" World");

System.out.println(sb);

Output:

Hello World


Because StringBuilder is mutable.


======================================================================
                     PERFORMANCE IDEA
======================================================================

If you repeatedly modify a String:

String result = "";

for (...) {
    result += value;
}

This can create many intermediate String objects.

Prefer:

StringBuilder sb = new StringBuilder();

for (...) {
    sb.append(value);
}

String result = sb.toString();


This is especially useful in:

→ Loops
→ String manipulation
→ Competitive programming
→ LeetCode
→ Large text construction


======================================================================
                         INTERVIEW RULE
======================================================================

Need repeated String modification?
                ↓
          StringBuilder


Need thread-safe mutable String operations?
                ↓
          StringBuffer


Need an immutable String?
                ↓
             String
======================================================================
*/