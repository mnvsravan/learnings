public class EQUALS {

    static class Student {
        String name;

        Student(String name) {
            this.name = name;
        }

        @Override // if u dont overide u get the value like == which compares refernces
        public boolean equals(Object obj) {

            Student other = (Student) obj;

            return this.name.equals(other.name);
        }
    }

    public static void main(String[] args) {

        Student a = new Student("Rahul");
        Student b = new Student("Rahul");

        System.out.println(a.equals(b));
    }
}

// 1. equals()
// ------------------------------------------------------------
// Used to compare two objects.
//
// Default Object.equals() compares references (same object).
//
//     a.equals(b)
//
// Returns:
//     true  → objects are considered equal
//     false → objects are not equal
//
// We can override equals() to compare object contents.