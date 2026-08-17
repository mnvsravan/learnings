// ============================================================
//                         clone()
// ============================================================
//
// clone() is a method of the Object class.
//
// Purpose:
//     Creates a copy of an existing object.
//
// Object class method:
//
//     protected native Object clone()
//             throws CloneNotSupportedException
//
// IMPORTANT:
//     Object.clone() returns Object
//     Object.clone() is protected
//
// Therefore, we normally override clone() and make it public.
//
// ============================================================

public class clone {

    static class Student implements Cloneable {

        String name;

        Student(String name) {
            this.name = name;
        }

        // ====================================================
        // Overriding clone()
        // ====================================================
        //
        // Object.clone() returns Object.
        //
        // Here we change the return type to Student.
        //
        // This is called a COVARIANT RETURN TYPE.
        //
        // Object:
        //     protected Object clone()
        //
        // Student:
        //     public Student clone()
        //
        // We make it public so that main() can call it.
        // ====================================================

        @Override
        public Student clone() throws CloneNotSupportedException {

            // super.clone() calls Object.clone()
            //
            // Object.clone() returns Object,
            // so we cast it to Student.

            return (Student) super.clone();
        }
    }

    public static void main(String[] args)
            throws CloneNotSupportedException {

        Student a = new Student("Rahul");

        // Calling the overridden clone()
        Student b = a.clone();

        System.out.println(b.name);

        // a and b are different objects
        System.out.println(a == b);
    }
}


// ============================================================
// OUTPUT
// ============================================================
//
// Rahul
// false
//
//
// ============================================================
// IMPORTANT POINTS
// ============================================================
//
// 1. clone() is originally present in Object.
//
// 2. Object.clone() returns Object.
//
// 3. Object.clone() is protected.
//
// 4. The class should implement Cloneable.
//
// 5. We override clone() and make it public.
//
// 6. We can change the return type:
//
//       Object clone()
//              ↓
//       Student clone()
//
//    This is called COVARIANT RETURN TYPE.
//
// 7. super.clone() calls Object.clone().
//
// 8. clone() creates a NEW object.
//
//       a → Student object 1 → "Rahul"
//       b → Student object 2 → "Rahul"
//
// 9. Therefore:
//
//       a == b → false
//
// 10. But both objects contain the same data:
//
//       a.name → "Rahul"
//       b.name → "Rahul"
//
// ============================================================