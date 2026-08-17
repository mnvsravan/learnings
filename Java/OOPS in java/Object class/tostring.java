// The Object Class is parent of all classes this has some builtin methods 
// we gota override them if we want our own working style like for eg

public class tostring {

    static class Student {
        String name;

        Student(String name) {
            this.name = name;
        }
        // if u dont overide and do toString u get something like tostring$Student@5e2de80c

        @Override
        public String toString() {
            return "Student name: " + name;
        }
    }

    public static void main(String[] args) {

        Student s = new Student("Rahul");

        System.out.println(s.toString());
    }
}
   // 3. toString()
// ------------------------------------------------------------
// Returns a String representation of an object.
//
//     a.toString()
//
// Default Object.toString() gives something like:
//     Student@5e2de80c
//
// We can override toString() to get readable output.
//
// Example:
//     @Override
//     public String toString() {
//         return "Student: " + name;
//     }
//
// Then:
//     System.out.println(a);
//
// automatically calls:
//     a.toString()

