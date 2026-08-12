
public class autoboxing_pogos {
    public static void main(String[] args) {
    //  Wrapper classes are classes in Java that convert primitive data types into objects.
    // we convert cuz we can use the their methods and properties. and its advanced features like collection framework, generics, etc.
    // auto-boxing is the automatic conversion that the Java compiler makes between the primitive types and their corresponding object wrapper classes. For example, converting an int to an Integer, a double to a Double, and so on.
int x =10;
Integer y = x; // Auto-boxing 
// this is like Integer y = Integer.valueOf(x); // Auto-boxing we dont do like Integer y = new Integer(x); // Auto-boxing but this is not recommended as it creates a new object every time and we can use the valueOf method which is more efficient and it uses caching for values between -128 to 127.
// notice that we use Integer. something ie this is a static method cuz we are calling it on the class itself not on an object of the class.
Integer z = 20; 
int a= z; // Unboxing
// this is like int a = z.intValue(); // Unboxing
// notice that we use z. something ie this is a instance method cuz we are calling it on an object of the class.

// THIS IS A BASIC OERVIEW HOW IT THE INTEGER CLASS WORKS IN JAVA.

// public final class Integer {

//     private final int value;

//     // Constructor
//     public Integer(int value) {
//         this.value = value;
//     }

//     // Returns the primitive int
//     public int intValue() {
//         return value;  GETTER
//     }

//     // Creates/Gives an Integer object
//     public static Integer valueOf(int x) {
//         return new Integer(x);   kind of setter
//     }

//     // Compares two Integer objects
//     public boolean equals(Integer y) {
//         return this.value == y.value;
//     }
// }
// ------------------------------------------------------------
        Integer k = 200;
        Integer m = 200;
        // a == b --> If a and b points to same reference

         System.out.println(k == m); // false cuz these are two different objects in memory. and they are not cached as they are outside the range of -128 to 127.
         // if we use values in between -128 to 127 then they will be cached and they will point to the same reference and the output will be true.
// ------------------------------------------------------------



// POJO = Plain Old Java Object

// It simply means a normal Java class used to store data.
// its of two types :
// like a class with only fields and getters and setters.
// another type is a class with fields, getters, setters and constructors.
    }
}