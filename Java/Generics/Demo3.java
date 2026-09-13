public class Demo3 {
    public static void main(String[] args) {
        Box<Integer> b1 = new Box<>(10); // Type argument
        Box<String> b2 = new Box<>("Hello");
        Box<Boolean> b3 = new Box<>(false); // this can give compile time error if we try to pass any other type

        System.out.println(b1.getValue() + 5);
        System.out.println(b2.getValue().toUpperCase());
        System.out.println(b3.getValue());

        //String s = (String) b1.getValue(); gives compile time error
    }
}

// Generics
class Box<T> { // type parameter
    private T value;

    Box(T value) {
        this.value = value;
    }

    public T getValue() {
        return this.value;
    }

    public void setValue(T value) {
        this.value = value;
    }
}

// Type information is not lost