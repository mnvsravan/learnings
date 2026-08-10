public class inheritance {

    // ==================================
    // PARENT CLASS
    // ==================================

    class BankAccount {

        // PRIVATE
        private double balance;
        private String pin;

        // DEFAULT
        String accountType;

        // PROTECTED
        protected String accountHolder;

        // PUBLIC
        public String bankName;


        // Parent constructor
        BankAccount(String accountHolder) {

            this.accountHolder = accountHolder;
            this.balance = 0;
            this.pin = "1234";
            this.bankName = "SBI";
        }


        // PRIVATE METHOD
        private void securityCheck() {

            System.out.println(
                "Security check completed"
            );
        }


        // PUBLIC METHOD
        public void deposit(double amount, String enteredPin) {

            if (!enteredPin.equals(pin)) {
                System.out.println("Wrong PIN");
                return;
            }

            securityCheck();

            if (amount > 0) {

                balance += amount;

                System.out.println(
                    "₹" + amount +
                    " deposited successfully"
                );
            }
            else {
                System.out.println("Invalid amount");
            }
        }


        // PUBLIC METHOD
        public void withdraw(double amount, String enteredPin) {

            if (!enteredPin.equals(pin)) {
                System.out.println("Wrong PIN");
                return;
            }

            securityCheck();

            if (amount <= 0) {

                System.out.println("Invalid amount");

            }
            else if (amount > balance) {

                System.out.println(
                    "Insufficient balance"
                );

            }
            else {

                balance -= amount;

                System.out.println(
                    "₹" + amount +
                    " withdrawn successfully"
                );
            }
        }


        // PUBLIC METHOD
        public void checkBalance(String enteredPin) {

            if (!enteredPin.equals(pin)) {
                System.out.println("Wrong PIN");
                return;
            }

            securityCheck();

            System.out.println(
                "Balance: ₹" + balance
            );
        }


        // PUBLIC METHOD
        public void displayAccount() {

            System.out.println(
                "Bank: " + bankName
            );

            System.out.println(
                "Account Holder: " + accountHolder
            );

            System.out.println(
                "Account Type: " + accountType
            );
        }
    }


    // ==================================
    // CHILD CLASS 1
    // ==================================

    class SavingsAccount extends BankAccount {

        private double interestRate;


        SavingsAccount(String accountHolder) {

            // Calls parent constructor
            super(accountHolder);

            accountType = "Savings";
            interestRate = 6.5;
        }


        public void calculateInterest() {

            System.out.println(
                "Interest Rate: " +
                interestRate + "%"
            );
        }


        public void showHolder() {

            // PROTECTED member
            System.out.println(
                "Account Holder: " +
                accountHolder
            );
        }
    }


    // ==================================
    // CHILD CLASS 2
    // ==================================

    class CurrentAccount extends BankAccount {

        private double overdraftLimit;


        CurrentAccount(String accountHolder) {

            // Calls parent constructor
            super(accountHolder);

            accountType = "Current";
            overdraftLimit = 50000;
        }


        public void showOverdraftLimit() {

            System.out.println(
                "Overdraft Limit: ₹" +
                overdraftLimit
            );
        }
    }


    // ==================================
    // MAIN METHOD
    // ==================================

    public static void main(String[] args) {

        inheritance obj = new inheritance();


        // ==============================
        // SAVINGS ACCOUNT
        // ==============================

        SavingsAccount savings =
            obj.new SavingsAccount("Rahul");


        savings.displayAccount();

        savings.deposit(50000, "1234");

        savings.withdraw(5000, "1234");

        savings.checkBalance("1234");

        savings.calculateInterest();

        savings.showHolder();


        System.out.println();


        // ==============================
        // CURRENT ACCOUNT
        // ==============================

        CurrentAccount current =
            obj.new CurrentAccount("Arjun");


        current.displayAccount();

        current.deposit(100000, "1234");

        current.withdraw(20000, "1234");

        current.checkBalance("1234");

        current.showOverdraftLimit();
    }
}

// remeber that we can even call methods and all in child with super like super.methodname() and also we can call parent constructor with super() in child constructor.