public class demo2 {
    public static void main(String[] args) {
        college.student s1 = new college.student();
        s1.print();

        school.student s2 = new school.student();
        s2.print();
    }
}
// this is is the meaning of public  and we this one slide pr sheet is known as package 
// even in other folders we are using stuff cuz of public cuz it is accessed via package
// instead of college.student s1 = new college.student(); we can use import college.student; and then student s1 = new student();
// or even we can use import college.*; then it will import all the classes in the college package like student and teacher 