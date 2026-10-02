public class Demo4 {
    public static void main(String[] args) {

        Test test = new Test();

        Thread t1 = new Thread(test);
        Thread t2 = new Thread(test);

        t1.start();
        t2.start();
    }
}

class Test implements Runnable {

    synchronized void m1() {

        System.out.println("m1 entered");

        try {
            Thread.sleep(2000);
        }
        catch(Exception e) {}

        System.out.println("m1 exit");
    }

    synchronized void m2() {

        System.out.println("m2 entered");

        try {
            Thread.sleep(2000);
        }
        catch(Exception e) {}

        System.out.println("m2 exit");
    }

    @Override
    public synchronized void run() {

        if(Thread.currentThread().getName().equals("Thread-0")) {
            m1();
        }
        else {
            m2();
        }
    }
}