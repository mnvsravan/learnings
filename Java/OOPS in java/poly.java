public class poly {

    // ==============================
    // PARENT CLASS
    // ==============================

    class Animal {

        private final String name;
        private final int age;

        // Constructor
        Animal(String name, int age) {
            this.name = name;
            this.age = age;
        }

        // Getters
        String getName() {
            return name;
        }

        int getAge() {
            return age;
        }

        // Method for Runtime Polymorphism
        void sound() {
            System.out.println(name + " makes a sound");
        }

        // Method Overloading
        void eat() {
            System.out.println(name + " is eating");
        }

        void eat(String food) {
            System.out.println(name + " is eating " + food);
        }

        void eat(String food, int quantity) {
            System.out.println(
                name + " is eating " + quantity + " grams of " + food
            );
        }

        // Final method
        final void sleep() {
            System.out.println(name + " is sleeping");
        }

        // Static method
        static void category() {
            System.out.println("Animals are living organisms");
        }
    }


    // ==============================
    // DOG CLASS
    // ==============================

    class Dog extends Animal {

        private final String breed;

        // Constructor
        Dog(String name, int age, String breed) {

            super(name, age);

            this.breed = breed;
        }

        // Getter
        String getBreed() {
            return breed;
        }

        // Method Overriding
        @Override
        void sound() {
            System.out.println(
                getName() + " barks"
            );
        }
    }


    // ==============================
    // CAT CLASS
    // ==============================

    class Cat extends Animal {

        private final String color;

        // Constructor
        Cat(String name, int age, String color) {

            super(name, age);

            this.color = color;
        }

        // Getter
        String getColor() {
            return color;
        }

        // Method Overriding
        @Override
        void sound() {
            System.out.println(
                getName() + " meows"
            );
        }
    }


    // ==============================
    // MAIN
    // ==============================

    public static void main(String[] args) {

        poly obj = new poly();

        // =========================================
        // COMPILE-TIME POLYMORPHISM
        // METHOD OVERLOADING
        // =========================================

        System.out.println("----- COMPILE-TIME POLYMORPHISM -----");

        Animal animal = obj.new Animal("Animal", 5);

        animal.eat();

        animal.eat("meat");

        animal.eat("meat", 500);


        // =========================================
        // RUNTIME POLYMORPHISM
        // METHOD OVERRIDING
        // =========================================

        System.out.println();
        System.out.println("----- RUNTIME POLYMORPHISM -----");

        Animal a;

        // Parent reference → Dog object
        a = obj.new Dog("Bruno", 4, "Labrador");

        a.sound();

        System.out.println("Name: " + a.getName());
        System.out.println("Age: " + a.getAge());

        a.sleep();


        System.out.println();


        // Parent reference → Cat object
        a = obj.new Cat("Luna", 3, "White");

        a.sound();

        System.out.println("Name: " + a.getName());
        System.out.println("Age: " + a.getAge());

        a.sleep();


        // =========================================
        // STATIC METHOD
        // =========================================

        System.out.println();

        Animal.category();
    }
}