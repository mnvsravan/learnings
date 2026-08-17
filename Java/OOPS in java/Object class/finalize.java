// ============================================================
//                       finalize()
// ============================================================
//
// finalize() was a method of the Object class.
//
// Purpose:
//     It was intended to be called by the Garbage Collector
//     before an object was removed from memory.
//
// Object class method:
//
//     protected void finalize()
//             throws Throwable
//
// IMPORTANT:
//     finalize() is DEPRECATED.
//     It should NOT be used in modern Java.
//
// ============================================================

public class finalize {

    static class Student {

        String name;

        Student(String name) {
            this.name = name;
        }

        @Override
        protected void finalize() throws Throwable {

            System.out.println("finalize() called");

            super.finalize();
        }
    }

    public static void main(String[] args) {

        Student s = new Student("Rahul");

        s = null;

        // Requests the JVM to run Garbage Collection.
        // This does NOT guarantee that finalize() will run.
        System.gc();

        System.out.println("End of main");
    }
}


// ============================================================
// IMPORTANT POINTS
// ============================================================
//
// 1. finalize() was used before an object was garbage collected.
//
// 2. It was intended for cleanup of resources.
//
// 3. The Garbage Collector was responsible for calling it.
//
// 4. System.gc() only REQUESTS garbage collection.
//    It does NOT guarantee that GC will happen.
//
// 5. finalize() is NOT guaranteed to execute.
//
// 6. finalize() is DEPRECATED and should not be used
//    in modern Java.
//
// 7. Modern Java uses alternatives such as:
//      - try-with-resources
//      - AutoCloseable
//
// ============================================================
//
// FINAL:
//
// finalize() → historically used for cleanup before an object
//              was garbage collected.
//
// Modern Java → DO NOT use finalize().
// ============================================================
