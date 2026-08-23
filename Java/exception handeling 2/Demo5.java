import java.io.*;

public class Demo5 {

    public static void main(String[] args) {

        try {
            readFile();
        }
        catch (IOException e) {
            System.out.println("File error: " + e.getMessage());
        }
    }

    // throws = declares that this method may throw IOException
    static void readFile() throws IOException {

        FileReader file = new FileReader("data.txt");

        System.out.println("File opened");
    }
}
// throws → tells the caller that an exception may occur
