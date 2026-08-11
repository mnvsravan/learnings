public class actualabstraction {

    // Abstract class , even if we use one abstract method in class then we have to declare class as abstract
    abstract class Car {

        protected String brand;
        protected int speed;

        // Constructor
        Car(String brand) {
            this.brand = brand;
            this.speed = 0;
        }

        // Abstract methods
        abstract void start(); // we dont declare cuz it is abstract method and we dont know what it will do in future so we just declare it and then we will implement it in child class

        abstract void stop();

        abstract void accelerate();

        // Concrete method
        void showDetails() {
            System.out.println("Brand: " + brand);
            System.out.println("Speed: " + speed + " km/h");
        }

        // Concrete method
        void brake() {
            speed = 0;
            System.out.println("Car is braking...");
        }
    }


    // Fuel Car
    class FuelCar extends Car {

        private int fuel;

        FuelCar(String brand, int fuel) {
            super(brand);
            this.fuel = fuel;
        }

        @Override  // we use @Override to tell the compiler that we are overriding the method from the parent class
        void start() {
            if (fuel > 0) {
                System.out.println("Fuel engine started");
            } else {
                System.out.println("Cannot start: No fuel");
            }
        }

        @Override
        void accelerate() {
            if (fuel > 0) {
                speed += 20;
                fuel -= 2;

                System.out.println("Fuel car accelerated");
                System.out.println("Fuel remaining: " + fuel + " litres");
            } else {
                System.out.println("Cannot accelerate: No fuel");
            }
        }

        @Override
        void stop() {
            speed = 0;
            System.out.println("Fuel car stopped");
        }
    }


    // Electric Car
    class ElectricCar extends Car {

        private int battery;

        ElectricCar(String brand, int battery) {
            super(brand);
            this.battery = battery;
        }

        @Override
        void start() {
            if (battery > 0) {
                System.out.println("Electric motor started");
            } else {
                System.out.println("Cannot start: Battery empty");
            }
        }

        @Override
        void accelerate() {
            if (battery > 0) {
                speed += 25;
                battery -= 5;

                System.out.println("Electric car accelerated");
                System.out.println("Battery remaining: " + battery + "%");
            } else {
                System.out.println("Cannot accelerate: Battery empty");
            }
        }

        @Override
        void stop() {
            speed = 0;
            System.out.println("Electric car stopped");
        }
    }


    // Main method
    public static void main(String[] args) {

        actualabstraction obj = new actualabstraction();

        Car car;


        System.out.println("----- FUEL CAR -----");

        car = obj.new FuelCar("BMW", 10);

        car.start();
        car.accelerate();
        car.accelerate();

        car.showDetails();

        car.brake();
        car.stop();


        System.out.println();


        System.out.println("----- ELECTRIC CAR -----");

        car = obj.new ElectricCar("Tesla", 50);

        car.start();
        car.accelerate();
        car.accelerate();

        car.showDetails();

        car.brake();
        car.stop();
    }
}