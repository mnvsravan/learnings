public class actualinterface {

    // Interface
    interface Payment { // it like set of rules which we have to follow and implement in our class

        void pay(double amount);

        void refund(double amount);

        void checkStatus();
    }


    // Credit Card Payment
    class CreditCardPayment implements Payment {

        private  final String cardHolder;

        // Constructor
        CreditCardPayment(String cardHolder) {
            this.cardHolder = cardHolder;
        }

        @Override
        public void pay(double amount) {
            System.out.println(cardHolder + " is paying ₹" + amount + " using Credit Card");
            System.out.println("Connecting to bank...");
            System.out.println("Payment successful");
        }

        @Override
        public void refund(double amount) {
            System.out.println("Refunding ₹" + amount + " to " + cardHolder);
        }

        @Override
        public void checkStatus() {
            System.out.println("Credit Card payment status: SUCCESS");
        }
    }


    // UPI Payment
    class UPIPayment implements Payment {

        private final String upiId;

        // Constructor
        UPIPayment(String upiId) {
            this.upiId = upiId;
        }

        @Override
        public void pay(double amount) {
            System.out.println(upiId + " is paying ₹" + amount + " using UPI");
            System.out.println("Verifying UPI ID...");
            System.out.println("Payment successful");
        }

        @Override
        public void refund(double amount) {
            System.out.println("Refunding ₹" + amount + " to " + upiId);
        }

        @Override
        public void checkStatus() {
            System.out.println("UPI payment status: SUCCESS");
        }
    }


    // Net Banking Payment
    class NetBankingPayment implements Payment {

        private final String accountHolder;

        // Constructor
        NetBankingPayment(String accountHolder) {
            this.accountHolder = accountHolder;
        }

        @Override
        public void pay(double amount) {
            System.out.println(accountHolder + " is paying ₹" + amount + " using Net Banking");
            System.out.println("Connecting to bank server...");
            System.out.println("Authenticating account...");
            System.out.println("Payment successful");
        }

        @Override
        public void refund(double amount) {
            System.out.println("Refunding ₹" + amount + " to " + accountHolder);
        }

        @Override
        public void checkStatus() {
            System.out.println("Net Banking payment status: SUCCESS");
        }
    }


    // Main method
    public static void main(String[] args) {

        actualinterface obj = new actualinterface();

        // Interface reference
        Payment payment;


        System.out.println("----- CREDIT CARD -----");

        payment = obj.new CreditCardPayment("Rahul");

        payment.pay(5000);
        payment.checkStatus();
        payment.refund(1000);


        System.out.println();


        System.out.println("----- UPI -----");

        payment = obj.new UPIPayment("rahul@upi");

        payment.pay(2500);
        payment.checkStatus();
        payment.refund(500);


        System.out.println();


        System.out.println("----- NET BANKING -----");

        payment = obj.new NetBankingPayment("Rahul");

        payment.pay(10000);
        payment.checkStatus();
        payment.refund(2000);
    }
}