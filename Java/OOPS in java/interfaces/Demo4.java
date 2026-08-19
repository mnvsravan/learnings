// ============================================================
//                 INTERFACE INHERITANCE
// ============================================================
//
// Interfaces can also INHERIT from other interfaces.
//
// We use:
//
//              extends
//
// when one interface inherits another interface.
//
// Example:
//
//     Dog extends Animal
//
// This means Dog gets the contract of Animal.
//
// ============================================================


public class Demo4 {

    public static void main(String[] args) {

        // StreetDog implements Dog.
        // Dog extends Animal.
        //
        // Therefore StreetDog must implement BOTH:
        //
        //     eat()  -> from Animal
        //     bark() -> from Dog

        StreetDog dog = new StreetDog();

        dog.eat();
        dog.bark();
    }
}


// ============================================================
//                    PARENT INTERFACE
// ============================================================
//
// Animal is the parent interface.
//
// It defines the common behaviour of animals.
//
// ============================================================

interface Animal {

    // Automatically:
    //
    // public abstract void eat();

    void eat();
}


// ============================================================
//                    CHILD INTERFACE
// ============================================================
//
// Dog extends Animal.
//
// Therefore Dog inherits the eat() method from Animal.
//
// Dog also adds its own behaviour:
//     bark()
//
// So Dog now has:
//
//     eat()
//     bark()
//
// ============================================================

interface Dog extends Animal {

    void bark();
}


// ============================================================
//                  IMPLEMENTING INTERFACE
// ============================================================
//
// StreetDog implements Dog.
//
// Since Dog extends Animal:
//
//     StreetDog
//          ↓
//        Dog
//          ↓
//       Animal
//
// StreetDog must implement methods from BOTH interfaces.
//
// ============================================================

class StreetDog implements Dog {

    // eat() originally comes from Animal.
    //
    // Because Dog inherited Animal,
    // StreetDog is required to implement eat().

    @Override
    public void eat() {

        System.out.println("Eating");
    }


    // bark() comes directly from Dog.

    @Override
    public void bark() {

        System.out.println("Barking");
    }
}


// ============================================================
//                       KEY POINTS
// ============================================================
//
// 1. INTERFACE CAN EXTEND ANOTHER INTERFACE.
//
//       interface Dog extends Animal
//
//
//
// 2. For INTERFACE → INTERFACE inheritance, use:
//
//       extends
//
//
//
// 3. For CLASS → INTERFACE implementation, use:
//
//       implements
//
//
//
// 4. The inheritance chain is:
//
//       Animal
//          ↑
//         Dog
//          ↑
//      StreetDog
//
//
//
// 5. Dog inherits eat() from Animal.
//
//    Therefore Dog effectively contains:
//
//       eat()
//       bark()
//
//
//
// 6. StreetDog implements Dog.
//
//    Therefore StreetDog must implement:
//
//       eat()
//       bark()
//
//
//
// 7. A class can implement an interface that has inherited
//    methods from other interfaces.
//
//
//
// ============================================================
//              FAANG-STYLE EXAMPLE
// ============================================================
//
// Think about a large software system:
//
// interface Employee {
//     void work();
// }
//
// interface SoftwareEngineer extends Employee {
//     void code();
// }
//
// class GoogleEngineer implements SoftwareEngineer {
//
//     @Override
//     public void work() {
//         System.out.println("Working on a product");
//     }
//
//     @Override
//     public void code() {
//         System.out.println("Writing scalable code");
//     }
// }
//
// ------------------------------------------------------------
//
// Employee
//     ↑
// SoftwareEngineer
//     ↑
// GoogleEngineer
//
// GoogleEngineer must implement BOTH:
//
//     work()  → inherited from Employee
//     code()  → declared in SoftwareEngineer
//
// This is called INTERFACE INHERITANCE.
//
// ============================================================
