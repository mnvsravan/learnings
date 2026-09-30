class MyTask implements Runnable {

    public void run() {
        System.out.println(Thread.currentThread().getName());
    }
}


public class Demo6 {

    public static void main(String[] args) {

        MyTask obj = new MyTask();

        Thread t1 = new Thread(obj);

        t1.setName("worker-1");

        t1.start();
    }
}


/*
    currentThread() --> reference of current running thread
*/