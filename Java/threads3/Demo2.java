public class Demo2 {

    static volatile boolean flag = false;

    public static void main(String[] args) {

        Task1 task1 = new Task1();
        Task2 task2 = new Task2();

        Thread t1 = new Thread(task1);
        Thread t2 = new Thread(task2);

        t1.start();
        t2.start();
    }
}

class Task1 implements Runnable {

    @Override
    public void run() {

        try {
            Thread.sleep(1000);
        }
        catch(Exception e) {}

        Demo2.flag = true;
    }
}

class Task2 implements Runnable {

    @Override
    public void run() {

        while(!Demo2.flag) {
            // do nothing
        }

        System.out.println("Thread 2 finished");
    }
}