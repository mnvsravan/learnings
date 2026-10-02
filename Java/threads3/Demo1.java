public class Demo1 {
    public static void main(String[] args) throws InterruptedException {

        Counter c1 = new Counter();

        Thread t1 = new Thread(c1);
        Thread t2 = new Thread(c1);

        t1.start();
        t2.start();

        t1.join();
        t2.join();

        System.out.println(c1.count);
    }
}

class Counter implements Runnable {

    public int count = 0;

    synchronized void increment() {
        count++;
    }

    @Override
    public void run() {
        for(int i=1; i<=10000; i++) {
            increment();
        }
    }
}