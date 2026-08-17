public class hashcode {
// hashCode() → useful for collections
    static class Student {
        String name;

        Student(String name) {
            this.name = name;
        }

        @Override
        public int hashCode() {
            return name.hashCode();
        }
    }

    public static void main(String[] args) {

        Student a = new Student("Rahul");
        Student b = new Student("Rahul");

        System.out.println(a.hashCode());
        System.out.println(b.hashCode());
    }
}

// 2. hashCode()
// ------------------------------------------------------------
// Returns an integer (int) hash value for an object.
//
//     a.hashCode()
//
// Mainly used by hash-based collections:
//     - HashMap
//     - HashSet
//     - Hashtable
//
// IMPORTANT:
// If a.equals(b) is true,
// then a.hashCode() == b.hashCode() MUST be true.
//
// Therefore, when we override equals(),
// we should also override hashCode().
//