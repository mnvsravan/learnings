function printMorning() {
  console.log("Good morning!");
  console.log("Have a great day!");
}

printMorning();
printMorning();
function myFunction(msg){
    console.log(msg);
}
myFunction("suck my cock");
//
function sum(x,y) {
s=x+y;
return s;
}
let val= sum(6,7);
console.log(val);
//
// arrow fucntions syntax: u need to go to console and operate these
// cost sum(x,y)=>{
    //   return a+b
    //      }
    const arrowsum=(x,y) =>{
        return x+y;
    }
    const printhellow=() =>{
        console.log("hello");
    }
    //
    function vowels(string) {
  let count = 0;
  for (const char of string.toLowerCase()) {  // convert to lowercase for safety
    if (char === "a" || char === "e" || char === "i" || char === "o" || char === "u") {
      count++;
    }
  }
  return count;
}
let Number= vowels("SRAVAN");
console.log(Number);
 // even console.log(vowels("Luffy")); 
//console.log(vowels("One Piece"));
//
const arrowvowels=(string)=>{
    let count = 0;
  for (const char of string.toLowerCase()) {  // convert to lowercase for safety
    if (char === "a" || char === "e" || char === "i" || char === "o" || char === "u") {
      count++;
    }
  }
  return count;
}

// for each fucntion synatax: arr.forEach(callbackfunction)
// A function passed into another function as an argument, which is then executed inside that outer function. this is callbackfunction
let arr=["pune", "delhi", "hyderabad"];
arr.forEach((val,idx,arr)=>{
    console.log(val.toUpperCase(),idx,arr);
}) // look those paraenthesis carefully
// 
let nums=[67,52,39];
let calcsquare=(num)=>{
    console.log(num*num) ;
};
nums.forEach(calcsquare);
// or do like this 
/*
let nums = [67, 52, 39];

nums.forEach((num) => {
  let square = num * num;   // calculate
  console.log(square);      // use (print) it right here
  return square;            // this return does nothing outside
});
*/
// 
// maps : creates a new array with the results optained the value its callback rteturns are used to form a new array
//arr.map(callbackfnx(value,index,array))
let digits = [67, 52, 39];

let newArr = nums.map((val) => {
  return val * 2;
});

console.log(newArr);
//
// filter: creates a new array of elements that give true for a condition/filter
// let newarr=arr.filter((val)=>{
  //  return val %2==0;
//}
let arrr = [1, 2, 3, 4, 5, 6, 7,8,9];

let evenArr = arrr.filter((val) => {
  return val % 2;
});

console.log(evenArr);
//
//  reduce : performs some operations and reduces the array to a single value. it returns that single value
let set = [5, 6, 2, 1, 3];

const output = set.reduce((prev, curr) => {
  return prev + curr;
});

console.log(output); // 17 
// like this prev is the 1st elemetn and curr is the second element
let ter = [5, 6, 2, 1, 3];

const answer = ter.reduce((prev, curr) => {
  return prev>curr? prev:curr
});

console.log(answer); // 17
// 
// questrion
let n = prompt("enter a number : ");

let diddy = [];

for (let i = 1; i <= n; i++) {
  diddy[i - 1] = i;
}

console.log(diddy);

let cum = diddy.reduce((res, curr) => {
  return res + curr;
});

console.log("sum = ", cum);

let factorial = diddy.reduce((res, curr) => {
  return res * curr;
});

console.log("factorial = ", factorial);
