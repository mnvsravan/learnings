public class demo2 {
    public static void main(String[] args) {

        System.out.println(Thread.currentThread().getName());
        System.out.println(Thread.currentThread().getId());

        MyThread r1 = new MyThread();
        MyThread r2 = new MyThread();

        Thread t1 = new Thread(r1);
        Thread t2 = new Thread(r2);

        t1.start();
        t2.start();
    }
}


class MyThread implements Runnable {

    @Override
    public void run() {

        System.out.println("Name of my thread is " + Thread.currentThread().getName());
        System.out.println("Id of my thread is " + Thread.currentThread().getId());

    }
}


// WE CANNOT START THREAD TWICE LIKE t1.start() t1.start() isnt possible