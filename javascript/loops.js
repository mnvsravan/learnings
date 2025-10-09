// console.log("hi");
for(let count=1; count<=5;count++){
    console.log("sravan is the best"); // the circle of the number beside shows how many times it printed
}

let sum=0
for(let num=1;num<=10;num++){
    sum=sum+num;
    console.log("sum is ",sum);
}
console.log("sum is ", sum); // this out of loop it dosent print each number again and again
console.log("sum is ended");

// for infinite loop we do like 
// for(let i=1;1>=0;i++){ // i used 1 isntead of i here cuz it implements our pc will crash
//     sum=sum+1
//     console.log(sum)

//do while loop
console.log("ok");
let a=1;
while(a<10){
    console.log("im the best");
    a++;
}
// do while 
let b = 1;
do {
    console.log(b);
    b++;
} while (b <= 10);
// for -of-loop
let str="FUCK YOU NIGGA";
let size=0;
for(let val of str){ // this does all the work
    console.log("val is ",val);
    size++;
}
console.log("size of str is ",size);
// for in loop
//for in loop

let student = {
    name: "Rahul Kumar",
    age: 20,
    cgpa: 7.5,
    isPass: true,
};

for (let key in student) {
    console.log("key=", key, " value=", student[key]);
}
// The for...of loop in JavaScript is used to iterate over the values of an iterable object such as an array, string, map, or set. It gives each element’s actual value one by one. For example, if you use it on an array of numbers, it will give you each number directly. It is mainly used when you only need the values and not the index or property name.

// Example in words: if you have an array [10, 20, 30], the for...of loop will first take 10, then 20, then 30.

// The for...in loop, on the other hand, is used to iterate over the keys or property names of an object. It goes through each property name inside an object and allows you to access its value using that key. It can also be used on arrays, but then it gives the indexes (0, 1, 2, etc.) instead of the actual values. It is mainly used for looping through objects.

// Example in words: if you have an object with properties name, age, and grade, the for...in loop will give you first “name”, then “age”, then “grade”
for (let num = 0; num <= 100; num++) {
    if (num % 2 == 0) {
        //even number
        console.log("num =", num);
    }
}
// game
let gameNum = 25;
let userNum = prompt("Guess the game number: ");

while (userNum != gameNum) {
    userNum = prompt("You entered wrong number. Guess again: ");
}

console.log("Congratulations, you entered the right number");
