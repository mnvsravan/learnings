public class Demo2 {
    public static void main(String[] args) {

        Box box = new Box();

        Thread t1 = new Thread() {

            public void run() {

                for(int i = 1; i <= 20; i++) {

                    try {
                        Thread.sleep(100);
                    }
                    catch(Exception e) {}

                    box.producer(i);
                }
            }
        };

        Thread t2 = new Thread() {

            public void run() {

                for(int i = 1; i <= 20; i++) {

                    try {
                        Thread.sleep(70);
                    }
                    catch(Exception e) {}

                    box.consumer();
                }
            }
        };

        t1.start();
        t2.start();
    }
}

class Box {

    volatile Integer item;
    volatile Boolean flag = false;

    synchronized void producer(int value) {
         while(flag == true) {
            // do nothing
        }
        item = value;
        flag = true;

        System.out.println("Producer produces " + item);
    }

    synchronized void consumer() {
         while(flag == false) {
            // do nothing
        }

        System.out.println("Consumer consumes " + item);

        item = null;
        flag = false;
    }
}

// STEP 1:
// Without synchronization, both Producer and Consumer
// can access the shared Box at the same time.
// This can cause a race condition because both threads
// are accessing the same item and flag.


// STEP 2:
// volatile is used for visibility.
// If one thread changes item or flag, the other thread
// can see the latest value.
// But volatile does NOT prevent race conditions.
// It also does NOT make a thread wait.


// STEP 3:
// synchronized allows only one thread at a time
// to enter producer() or consumer().
// This prevents both threads from modifying the
// shared Box at the same time.
//
// But synchronized only provides mutual exclusion.
// It does NOT tell the thread when it should wait.
//
// Producer can still produce when the Box is full.
// Consumer can still consume when the Box is empty.


// STEP 4:
// wait() is needed for coordination.
//
// If the Box is full, the Producer must wait
// until the Consumer consumes the item.
//
// If the Box is empty, the Consumer must wait
// until the Producer produces an item.
//
// wait() also releases the lock so that the
// other thread can enter the synchronized method.


// STEP 5:
// notify() is used to wake up a waiting thread.
//
// After Producer produces an item,
// notify() tells the Consumer that an item is available.
//
// After Consumer consumes an item,
// notify() tells the Producer that the Box is empty
// and it can produce another item.


// FINAL IDEA:
//
// volatile     -> visibility
// synchronized -> only one thread at a time
// wait()       -> wait when the condition is not satisfied
// notify()     -> wake up the waiting thread
//
// Producer-Consumer needs wait() and notify()
// because synchronized alone cannot coordinate
// when the Producer or Consumer should wait.