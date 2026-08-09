public class keywords {

    // Static variable
    static String college = "JNTUH";

    // Non-static variables
    String name;
    int age;

    // Constructor
    keywords(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Static method
    static void displayCollege() {
        System.out.println("College: " + college);
    }

    // Static method with parameters
    static int add(int a, int b) {
        return a + b;
    }

    // Static method calling another static method
    static void showMessage() {
        System.out.println("Welcome Student");
        displayCollege();
    }

    // Static method accessing non-static variables through an object
    static void displayStudent(keywords s) { // LIKE WE ARE ACCESSING THE NON STATIC VARIABLES THROUGH THE OBJECT OF THE CLASS CUZ WE PASSED ARGUMENTS
        System.out.println("Name: " + s.name); // IF WE DIDN'T PASS THE OBJECT AS ARGUMENT THEN WE CAN'T ACCESS THE NON STATIC VARIABLES IN STATIC METHOD LIKE NORMAL VOID FUCNTIUON WITHOUT STATIC KEYWORD
        System.out.println("Age: " + s.age); // ONLY A STATIC CAN CALL STATIC METHODS AND STATIC VARIABLES BUT A STATIC METHOD CAN'T CALL NON STATIC METHODS AND NON STATIC VARIABLES WITHOUT OBJECT OF THE CLASS
    }

    // Non-static method
    void displayStudent2() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }

    public static void main(String[] args) {

        // Creating an object
        keywords s = new keywords("Nitish", 20);

        // Calling static method using class name
        keywords.displayCollege();

        // Calling static method with parameters
        int result = keywords.add(10, 20);
        System.out.println("Sum: " + result);

        // Static method calling another static method
        keywords.showMessage();

        // Static method accessing non-static data through object
        keywords.displayStudent(s);

        // Calling non-static method using object
        s.displayStudent2();
    }
}
// we can initialize static varbales like this after declaring
// static{
//     college = "JNTUH";
// }