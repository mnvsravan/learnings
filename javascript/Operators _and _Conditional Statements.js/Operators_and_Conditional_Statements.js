//arthemetic operators
let a=5;
let b=2;
console.log("Vale of a is ",a,"value of b is",b);
console.log("Value of a+b is ", a+b);
console.log("Value of a-b is ", a-b);
console.log("Value of a*b is ", a*b);
console.log("Value of a/b is ", a/b);
console.log("Value of a%b is ", a%b);
console.log("Value of a**b is ", a**b); // this is like 5^2
// console.log("value of a++ is ",a++); // we get 5
// console.log("value of ++a is ",++a); // we get 6
a++;
console.log("value of a++ is ",a); // same way for decrement also
a+=4;
console.log("value of a is ",a); // like not the a values will be the answer of previous ones
a*=3;
console.log("value of a is ",a);
a**=3;
console.log("value of a is ",a); // this is like multiplaying same number 3 times
// like a%=3 these things are like a=a%3


// comparition operators 
// == is for equal === is like more accurate equal like if we keep a=5 and b="5" this is strring so it wont be equal
// != is not equal and !== is for more accurate 
// others are normal like <= >= < >
// this kind of things just true/false outcomes
let c=1;
let d=2;
console.log("c===d is ",c===d);
console.log("c!==d ",c!==d);

//logical operaators 
// && is for and , || is for or , ! is for not
 let condition1=c===d;
 let condition2=c<d;
console.log("the condition1 && condition2 is ",condition1 && condition2);
console.log("the condition1 || condition2 is ",condition1 ||  condition2);
console.log("!(the condition1 && condition2 is) ",!(condition1 && condition2)); // like gives opp output

// conditon state

let mode ="light";
let color;
if(mode==="dark"){
    color="black"
    console.log(color);
}
if(mode==="light"){
    color="white"
    console.log(color);
}

else{
    console.log("invalid");

}
// for more statemnts we use else if loop like we use if first and then how many else if we want and end it with else statemnt
let screen = "silver";
let background;

if (screen === "dark") {
    background = "black";
} else if (screen === "blue") {
    background = "blue";
} else if (screen === "pink") {
    background = "pink";
} else {
    background = "white";
}

console.log(background);

// ternary
let age=19;
let result = age>=18? "adult":"not adult";
console.log(result); // this like seeing if the condition is ture and prints the the value if its right if no then the right option
// refer MDN for new things if u want in any thing like switch and etc and stuff
// promt 
let score = prompt("Enter your score:");
let grade;

if (score >= 90 && score <= 100) {
    grade = "A";
} else if (score >= 70 && score <= 89) {
    grade = "B";
} else if (score >= 60 && score <= 69) {
    grade = "C";
} else if (score >= 50 && score <= 59) {
    grade = "D";
} else if (score >= 0 && score <= 49) {
    grade = "F";
}

console.log("According to your scores, your grade was:", grade);

