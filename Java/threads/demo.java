public class demo {
    public static void main(String[] args) {

        // Using Thread class
        MyThread t1 = new MyThread();
        t1.start();

        // Using Runnable
        Myruntime r1 = new Myruntime();
        Thread t2 = new Thread(r1);
        t2.start();
    }
}


// Thread class Extend
class MyThread extends Thread {

    @Override
    public void run() {
        System.out.println("Thread is running");
    }
}


// Runnable interface
class Myruntime implements Runnable {

    @Override
    public void run() {
        System.out.println("Runnable thread is running");
    }
}

/*
t1.start() --> JVM asks OS to create a new thread --> Thread gets Stack/PC space -->
Thread execute run()


we can use lamda functions also instead of these classes
we prefer using runnable rather than creating from thread class cuz see notes

*/