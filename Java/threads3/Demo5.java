public class Demo5
 {
    public static void main(String[] args) {

        Bank b1 = new Bank();

        Thread t1 = new Thread(b1);
        Thread t2 = new Thread(b1);

        t1.start();
        t2.start();
    }
}

class Bank implements Runnable {

    Object lock1 = new Object(); // just for the sake of creating we use objects as locks. We can use any object as lock. It can be String, Integer, etc.
    Object lock2 = new Object();

    void m1() {

        synchronized(new Object()) {

            System.out.println(Thread.currentThread().getName() + " Entered m1");

            try {
                Thread.sleep(2000);
            }
            catch(Exception e) {}

            System.out.println(Thread.currentThread().getName() + " Exiting m1");
        }
    }

    void deposit() {

        synchronized(lock1) {

            System.out.println("Deposit logic"+
                Thread.currentThread().getName() + " Entered deposit");

            try {
                Thread.sleep(2000);
            }
            catch(Exception e) {}
        }
    }

    void withdraw() {

        synchronized(lock2) {

            System.out.println("Withdraw logic"+
                Thread.currentThread().getName() + " Entered withdraw");

            try {
                Thread.sleep(2000);
            }
            catch(Exception e) {}
        }
    }

    @Override
    public void run() {

        // THESE BOTH CAN RUN IN PARALLEL BECAUSE THEY ARE SYNCHRONIZED ON DIFFERENT OBJECTS
        // BUT IF WE SYNCHRONIZE THEM ON SAME OBJECT THEN THEY WILL NOT RUN IN PARALLEL
        // EG. IF WE SYNCHRONIZE THEM ON lock1 THEN THEY WILL NOT RUN IN PARALLEL

        deposit();

        withdraw();

        // m1();
    }
}