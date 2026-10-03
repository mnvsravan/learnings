public class Demo3 {
    public static void main(String[] args) {

        Box box = new Box();

        Thread t1 = new Thread() {

            public void run() {

                for(int i = 1; i <= 20; i++) {

                    try {
                        Thread.sleep(100);
                    }
                    catch(Exception e) {}

                    try {
                        box.producer(i);
                    }
                    catch(Exception e) {}
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

                    try {
                        box.consumer();
                    }
                    catch(Exception e) {}
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

    synchronized void producer(int value) throws InterruptedException {

        while(flag == true) {
            wait();
        }

        item = value;
        flag = true;

        System.out.println("Producer produces " + item);

        notifyAll();
    }

    synchronized void consumer() throws InterruptedException {

        while(flag == false) {
            wait();
        }

        System.out.println("Consumer consumes " + item);

        item = null;
        flag = false;

        notifyAll();
}
}