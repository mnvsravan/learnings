public class Demo3 {
    public static void main(String[] args) {

        MyThread r1 = new MyThread(1);
        MyThread r2 = new MyThread(2);

        Thread t1 = new Thread(r1);
        Thread t2 = new Thread(r2);

        t1.start();
        t2.start();
    }
}


class MyThread implements Runnable {

    int n;

    MyThread(int n) {
        this.n = n;
    }

    @Override
    public void run() {

        for(int i = 1; i <= 100; i++) {

            if(n == 1 && i % 2 == 0) {
                System.out.println("T1 : " + i);
            }

            if(n == 2 && i % 2 != 0) {
                System.out.println("T2 : " + i);
            }
        }
    }
}
