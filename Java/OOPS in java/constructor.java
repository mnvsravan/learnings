public class constructor {
    public static void main(String args[]) {
        student s1 = new student(); 
        student s2 = new student("Alice", 20, 101, "JNTUH");
        s1.display(); // comes with default values of the data members of the class, because we have not initialized them yet   
        s2.display();
        // we can have so many constructors in a class, but the name of the constructor should be same as the class name and it should not have any return type, and we can have parameterized constructor as well
        
    }

     static class student {
        String name;
        int age;
        int rollNumber;
        String college;
        
            void display() {
                System.out.println(name+" "+age+" "+rollNumber+" "+college);
            }

        // constructor is a special method which is used to initialize the object of a class
// synatx is same as method but it has no return type and name of the constructor is same as class name
         student() {
            
            System.out.println("Constructor called");

        }
        // paramaterized constructor
        student(String name,int age,int rollNumber,String college) { 
            this.name=name; // this is like pointer in c, it is used to refer the current object of the class, so we can use this to refer the current object of the class
            this.age=age;
            this.rollNumber=rollNumber;
            this.college=college;
        }
          
        
    }
}