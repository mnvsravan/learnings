public class Demo {
    public static void main(String[] args) {

        Box box = new Box();

        Thread t1 = new Thread(box);
        Thread t2 = new Thread(box);

        t1.start();
        t2.start();
    }
}

class Box implements Runnable {

    Integer item;
    Boolean flag = false;

    public void run() {

        if(Thread.currentThread().getName().equals("Thread-0")) {

            for(int i = 1; i <= 20; i++) {

                try {
                    Thread.sleep(100);
                }
                catch(Exception e) {}

                producer(i);
            }
        }

        else {

            for(int i = 1; i <= 20; i++) {

                try {
                    Thread.sleep(70);
                }
                catch(Exception e) {}

                consumer();
            }
        }
    }

    void producer(int value) {
        item = value;
        flag = true;

        System.out.println("Producer produces " + item);
    }

    void consumer() {
        System.out.println("Consumer consumes " + item);

        item = null;
        flag = false;
    }
}

// Runnable -> WHAT the thread should do
// Thread   -> actually executes that work

// start() -> creates a new thread and calls run()
// run()   -> contains the work performed by the thread

// sleep() -> pauses the CURRENT thread

// Shared resource -> Box
// Race condition -> multiple threads access shared data at the same time

// flag = false -> Box empty
// flag = true  -> Box contains an item

// synchronized -> protects shared data from concurrent access
// wait()       -> makes a thread wait and releases the monitor
// notify()     -> wakes a waiting thread