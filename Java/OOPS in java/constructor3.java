public class constructor3 {
    public static void main(String[] args) {
        // call my value
         int x = 4;
        int y = 5;

        System.out.println(x + " , " + y);

        addTen(x, y);
        
        System.out.println(x + " , " + y);


        // there is no call by reference in java, only call by value
        // but it call by reference kind of acitivites can be done by using object reference, because object reference is passed by value but the object itself is not copied, so the changes made to the object inside the method will affect the original object.


        random r1=new random(4,5);
        System.out.println(r1.a + " , " + r1.b);
        addTen(r1);
        System.out.println(r1.a + " , " + r1.b);

    }
    
    static void addTen(int x, int y) {
        x = x + 10;
        y = y + 10;
    }
     static void addTen(random r) {
        r.a = r.a + 10;
        r.b = r.b + 10;
    }

    static class random{
        int a;
        int b;

        random(int a, int b){
            this.a=a;
            this.b=b;
        }
    }
}


// REFER HIS NOTES FOR BETTER UNDERSTANDING OF THIS CONCEPT
// and we can return objects also like 
// static random addTen(random r) {
//     r.a = r.a + 10;
//     r.b = r.b + 10;
//     return r;
// we can copy also like random r2=addTen(r1); and then we can use r2 also, but it will be same as r1 because it is not copied, it is just a reference to the same object.

// we can even do stuff like in constructer
// random(random r) {
//     this.a=r.a;
//     this.b=r.b;
// }