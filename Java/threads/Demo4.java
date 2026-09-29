public class Demo4 {
    public static void main(String[] args) {

        // Thread new stage

        Thread mainThread = Thread.currentThread();

        MyThread r1 = new MyThread(mainThread);
        Thread t1 = new Thread(r1);

        System.out.println(t1.getState());

        // Runnable stage
        t1.start();

        System.out.println(t1.getState()); // RUNNABLE

        try {
            Thread.sleep(2000);
        }
        catch(Exception e) {}

        System.out.println(t1.getState()); // TERMINATED
    }
}


class MyThread implements Runnable {

    Thread mainThread;

    MyThread(Thread mainThread) {
        this.mainThread = mainThread;
    }

    @Override
    public void run() {

        System.out.println("Name of current thread is "
                + Thread.currentThread().getName());

        System.out.println("Main thread state "
                + mainThread.getState());
    }
}
