public class Demo6 {
    public static void main(String[] args) {

        Counter c1 = new Counter();

        Thread t1 = new Thread(c1);
        Thread t2 = new Thread(c1);

        t1.start();
        t2.start();
    }
}

// Static Synchronization

class Counter implements Runnable {

    static int count = 0;

    static void increment() {

        synchronized(Counter.class) { // this locks the class itself, so that no other thread can access the class until the lock is released

            try {
                Thread.sleep(2000);
            }
            catch(Exception e) {}

            count++;

            System.out.println(count);
        }
    }

    @Override
    public void run() {
        increment();
    }
}

// even this is same as above, but here we are locking the method itself, so that no other thread can access the method until the lock is released
// class Counter implements Runnable {

//     static int count = 0;

//     static synchronized void increment() {

//         try {
//             Thread.sleep(2000);
//         }
//         catch(Exception e) {}

//         count++;

//         System.out.println(count);
//     }

//     @Override
//     public void run() {
//         increment();
//     }
// }