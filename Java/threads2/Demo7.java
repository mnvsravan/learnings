class Task1 implements Runnable {

    public void run() {
        System.out.println("Custom thread running");
    }
}


class Task2 implements Runnable {

    public void run() {
        System.out.println("Custom-2 thread running");
    }
}


public class Demo7 {

    public static void main(String[] args) {

        Task1 obj1 = new Task1();
        Task2 obj2 = new Task2();

        Thread t1 = new Thread(obj1);
        Thread t2 = new Thread(obj2);

        t1.start();
        t2.start();

        t1.setPriority(10);

        System.out.println(t1.getPriority());
    }
}


/*
    Thread Priority
    MAX_PRIORITY = 10
    MIN_PRIORITY = 1
    NORM_PRIORITY = 5

    Depends on OS
    -> may respect Priority
    -> may partially respect
    -> may not at all

*/