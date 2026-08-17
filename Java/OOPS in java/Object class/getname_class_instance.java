
public class getname_class_instance {

    static class Animal {
    }

    static class Dog extends Animal {
    }

    public static void main(String[] args) {

        Animal a = new Dog();
        Animal b = new Animal();

        
        System.out.println(a.getClass());

        
        System.out.println(a.getClass().getName());

        
        System.out.println(a.getClass().getSimpleName());

        
        System.out.println(a instanceof Dog);
        System.out.println(a instanceof Animal);
        System.out.println(b instanceof Dog);
        System.out.println(b instanceof Animal);
    }
}

// 1. getClass()
// ------------------------------------------------------------
// Returns the Class object representing the runtime class
// of the current object.
//
//     obj.getClass()
//
// Example:
//     Student s = new Student();
//
//     System.out.println(s.getClass());
//
// Output:
//     class Student
//
//
//
// 2. getClass().getName()
// ------------------------------------------------------------
// Returns the FULL name of the class as a String.
//
//     obj.getClass().getName()
//
// Example:
//     Student s = new Student();
//
//     System.out.println(s.getClass().getName());
//
// Output:
//     Student
//
// If the class is inside another class/package,
// it may return the full qualified name.
//
// Example:
//     com.example.Student
//
//
//
// 3. getClass().getSimpleName()
// ------------------------------------------------------------
// Returns ONLY the simple class name.
//
//     obj.getClass().getSimpleName()
//
// Example:
//     Student s = new Student();
//
//     System.out.println(s.getClass().getSimpleName());
//
// Output:
//     Student
//
// Difference:
//
//     getName()         → full class name
//     getSimpleName()   → simple class name
//
//
// ============================================================
//
// 4. instanceof
// ------------------------------------------------------------
// IMPORTANT: instanceof is NOT a method.
// It is a Java operator.
//
// It checks whether an object belongs to a particular class
// or is an instance of a class/interface.
//
// Syntax:
//
//     object instanceof ClassName
//
// Returns:
//     true  → object is an instance of that class
//     false → object is not an instance
//
// Example:
//
//     Student s = new Student("Rahul");
//
//     System.out.println(s instanceof Student);
//
// Output:
//     true
//
//
// Example:
//
//     Student s = new Student("Rahul");
//
//     System.out.println(s instanceof String);
//
// Output:
//     false



// you cannot override getClass() and also instance of .

// getClass() is declared in Object as:

// public final native Class<?> getClass();