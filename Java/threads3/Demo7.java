public class Demo7 {
    public static void main(String[] args) {

        Test test = new Test();

        Thread t1 = new Thread(test);
        Thread t2 = new Thread(test);

        t1.start();
        t2.start();
    }
}

class Test implements Runnable {

    static void m1() {
        synchronized(Test.class) {

            System.out.println("m1 entered");

            try {
                Thread.sleep(2000);
            }
            catch(Exception e) {}

            System.out.println("m1 exit");
        }
    }

    void m2() {
        synchronized(this) {

            System.out.println("m2 entered");

            try {
                Thread.sleep(2000);
            }
            catch(Exception e) {}

            System.out.println("m2 exit");
        }
    }

    @Override
    public void run() {

        if(Thread.currentThread().getName().equals("Thread-0")) {
            m1();
        }
        else {
            m2();
        }
    }
}
