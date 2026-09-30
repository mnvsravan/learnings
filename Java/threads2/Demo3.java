class Task1 implements Runnable {
@Override
    public void run() {
        for(int i=1; i<=10; i++) {
            System.out.println("T1 : " + i);
            Thread.yield();
        }
    }
}


class Task2 implements Runnable {
@Override 
    public void run() {
        for(int i=1; i<=10; i++) {
            System.out.println("T2 : " + i);
        }
    }
}


public class Demo3 {

    public static void main(String[] args) {

        Task1 obj1 = new Task1();
        Task2 obj2 = new Task2();

        Thread t1 = new Thread(obj1);
        Thread t2 = new Thread(obj2);

        t1.start();
        t2.start();
    }
}

/*
 
Thread.yield() --> I am willing to give my cpu time to someone else with same priority and 
that wants to run

1. OS can reject this.

2. It is like a suggestion to the OS

3. Current thread does not go to WAITING, TIMED_WAITING, BLOCKED.
   It does go to only RUNNABLE state

*/