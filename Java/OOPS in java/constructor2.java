
public class constructor2 {
    public static void main(String[] args) {

        Student s1 = new Student();
        Student s2 = new Student("Alice", 22, "XYZ University", 101);

        s1.display();
        s2.display();

        dimensions d1=new dimensions(5.0);
        dimensions d2=new dimensions(4.0,6.0);


        Car car = new Car().setBrand("BMW").setSpeed(180);
        car.display();
    }

    static class Student {
        String name;
        int age;
        String college;
        int rollNumber;
// we use constructor chaning with this like calling stuff


        // Default constructor
        Student() {
            this("Unknown", 0);
        }

        // 2-parameter constructor
        Student(String name, int age) {
            this(name, age, "Unknown");
        }

        // 3-parameter constructor
        Student(String name, int age, String college) {
            this(name, age, college, 0);
        }

        // 4-parameter constructor
        Student(String name, int age, String college, int rollNumber) {
            this.name = name;
            this.age = age;
            this.college = college;
            this.rollNumber = rollNumber;
        }

        void display() {
            System.out.println("Name: " + name + ", Age: " + age+ ", College: " + college + ", Roll Number: " + rollNumber);
        }
    }

    static class dimensions{
        double radius;
         double length;
          double width;
        double pi=3.14;

        dimensions(double radius){
            this.radius=radius;
            this.areaOfCircle();

        }
        void areaOfCircle(){
            double area=pi*radius*radius;
            System.out.println("Area of circle: "+area);
        }

        dimensions(double length,double width){
            this.length=length;
            this.width=width;
            this.areaOfRectangle();
        }
        void areaOfRectangle(){
            double area=length*width;
            System.out.println("Area of rectangle: "+area);
        }
 



    }



    static class Car {
    String brand;
    int speed;

    Car setBrand(String brand) {
        this.brand = brand;
        return this;
    }

    Car setSpeed(int speed) {
        this.speed = speed;
        return this;
    }

    void display() {
        System.out.println(brand + " " + speed);
    }
}
}