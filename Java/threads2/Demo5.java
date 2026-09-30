class MyTask implements Runnable {

    public void run() {
        try {
            Thread.sleep(2000);
        }
        catch(Exception e) {}
    }
}


public class Demo5 {

    public static void main(String[] args) {

        MyTask obj = new MyTask();

        Thread t1 = new Thread(obj);

        System.out.println(t1.isAlive()); // false

        t1.start();

        System.out.println(t1.isAlive()); // true

        try {
            Thread.sleep(3000);
        }
        catch(Exception e) {}

        System.out.println(t1.isAlive());  // false

    }
}


/*

    isAlive() --> start - terminate

*/
