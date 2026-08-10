public class abstraction {

    // PRIVATE
    private double balance = 50000;
    private String pin = "1234";


    // DEFAULT
    String accountType = "Savings";
    String branch = "Hyderabad";


    // PROTECTED
    protected String accountHolder = "Rahul";


    // PUBLIC
    public String bankName = "SBI";


    // PRIVATE METHOD
    private void securityCheck() {
        System.out.println("Security check completed");
    }


    // DEPOSIT
    public void deposit(double amount, String enteredPin) {

        if (!enteredPin.equals(pin)) {
            System.out.println("Wrong PIN");
            return;
        }

        // Correct PIN → call private method
        securityCheck();

        if (amount > 0) {
            balance = balance + amount;
            System.out.println("₹" + amount + " deposited successfully");
        }
        else {
            System.out.println("Invalid amount");
        }
    }


    // WITHDRAW
    public void withdraw(double amount, String enteredPin) {

        if (!enteredPin.equals(pin)) {
            System.out.println("Wrong PIN");
            return;
        }

        // Correct PIN → call private method
        securityCheck();

        if (amount <= 0) {
            System.out.println("Invalid amount");
        }
        else if (amount > balance) {
            System.out.println("Insufficient balance");
        }
        else {
            balance = balance - amount;
            System.out.println("₹" + amount + " withdrawn successfully");
        }
    }


    // CHECK BALANCE
    public void checkBalance(String enteredPin) {

        if (!enteredPin.equals(pin)) {
            System.out.println("Wrong PIN");
            return;
        }

        // Correct PIN → call private method
        securityCheck();

        System.out.println("Current Balance: ₹" + balance);
    }


    // TRANSFER
    public void transfer(double amount, String enteredPin) {

        if (!enteredPin.equals(pin)) {
            System.out.println("Wrong PIN");
            return;
        }

        // Correct PIN → call private method
        securityCheck();

        if (amount <= 0) {
            System.out.println("Invalid amount");
        }
        else if (amount > balance) {
            System.out.println("Insufficient balance");
        }
        else {
            balance = balance - amount;
            System.out.println("₹" + amount + " transferred successfully");
        }
    }


    // MAIN
    public static void main(String[] args) {

        abstraction account = new abstraction();


        // PUBLIC
        System.out.println("Bank: " + account.bankName);


        // DEFAULT
        System.out.println("Account Type: " + account.accountType);
        System.out.println("Branch: " + account.branch);


        // PROTECTED
        System.out.println("Account Holder: " + account.accountHolder);


        // DEPOSIT
        account.deposit(10000, "1234");


        // WITHDRAW
        account.withdraw(5000, "1234");


        // CHECK BALANCE
        account.checkBalance("1234");


        // TRANSFER
        account.transfer(15000, "1234");


        // WRONG PIN
        account.withdraw(5000, "9999");
    }
}

// private → Accessible only within the same class.
// default → Accessible within the same package.
// protected → Accessible within the same package and child classes.
// public → Accessible from anywhere.