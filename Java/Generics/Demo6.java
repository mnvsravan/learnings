public class Demo6 {
    public static void main(String[] args) {
        Box<Integer> b1 = new Box<>();
        b1.value = 5;
        b1.printDouble();
    }
}
// Generics --> T can be anything
// Bounds in Generics
// Upper bound --> T is atleast Number or its subtype
// we are restricting the type parameter to be Number or its subtype like these float, double, int, long, short, byte come under Number class
// lower bound --> T is atleast Number or its supertype eg: for lower bound we can use super keyword like T super Number, then we can pass Number, Object etc

class Box<T extends Number> {
    T value;

    public void printDouble() {
        System.out.println(value.doubleValue());
    }
}
