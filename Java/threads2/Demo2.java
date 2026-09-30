class MyTask implements Runnable {
@Override 
    public void run() {
        try {
            Thread.sleep(2000);
        }
        catch(InterruptedException e) {
        }

        System.out.println("Thread-0 starts");
    }
}


public class Demo2 {

    public static void main(String[] args) throws InterruptedException {

        System.out.println("Main thread starts");

        MyTask obj = new MyTask();

        Thread t1 = new Thread(obj);

        t1.start();

        // t1.join();
        t1.join(4000); // let the t1 thread first complete its execution

        System.out.println("Main thread ends");
    }
}

// join()
/*
Main thread --> WAITING
t1 thread --> RUNNABLE --> TERMINATED
Main thread --> WAITING -> RUNNABLE --> TERMINATED
*/