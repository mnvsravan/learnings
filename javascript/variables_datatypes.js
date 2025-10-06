console.log("This is the start of js!");
// this is used litrally for priinting the thing in the ""
// varibles are the things which store the value of the contaier 
// eg
Fullname = "Tony Stark";
// this is a string data type
// name = "tony stark" this will show like this only , like just keep a more menaingingful name (like name will get striked)
age = "24";
// this is a number data type
a = "null";
// this is a null data type
y = "undefined";
// this is a undefined data type
isFollow = "true";
// this is a boolean data type
console.log(y); // like here we dont use "" again
// the rules for variables are the same as in c programming 
// there are types formats of writing like : fullName- camel casel , fullname-no type, full_name-snake case, full-name- kebab cse, FullName-pascal case etc
// In JavaScript, variables are used to store data values.
// There are three main ways to declare variables: var, let, and const.
// Each has different rules for scope, hoisting, and reassignment.

// 1. var

// • Function Scoped – Variables declared with var are visible throughout the function in which they are declared. If declared outside any function, they become global variables.

// • Can be Redeclared and Reassigned – You can declare the same variable multiple times using var.

// • Hoisting – Variables declared with var are hoisted to the top of their scope. Only the declaration is hoisted, not the value. So, using it before declaration gives "undefined" instead of an error.

// • No Block Scope – If var is declared inside a block (like within curly braces {}), it can still be accessed outside that block.

// Example idea: If you declare var x = 10 inside an if block, you can still use x outside that block.

// 2. let

// • Block Scoped – Variables declared with let are only available within the block ({}) where they are defined.

// • Can be Reassigned but NOT Redeclared – You can change the value of a let variable but cannot declare the same variable name again in the same scope.

// • Hoisting with Temporal Dead Zone (TDZ) – let variables are hoisted but not initialized. Accessing them before declaration causes a ReferenceError.

// • Safer than var – let prevents accidental overwriting or unwanted access from other parts of the program.

// Example idea: If you declare let y = 5 inside a loop block, it cannot be accessed outside that loop.

// 3. const

// • Block Scoped – Like let, const is also block scoped.

// • Cannot be Redeclared or Reassigned – Once you declare a const variable, you cannot change its value or declare it again with the same name.

// • Must be Initialized – You must assign a value when declaring a const variable. Declaring without initializing causes an error.

// • Mutable Objects – const does not make objects or arrays immutable. You cannot reassign them, but you can modify their contents.
// For example, if you declare a const array, you can still push or change elements inside it.

var age = "24"
var age="34"
// like this u can change var any time and how ever u want
let num="55";
 num="66"
// let num = "45" we cant use this cuz we used it once but u can change it by keeping new num but not a let word
const ok="69";
// now u cant change this const by any means 
console.log(ok)
// Global variable → Declared outside any block or function, accessible everywhere.

// Block → A section of code inside { }.  var is global , let and const are block
let s= BigInt("123");
let z=Symbol("Hello!");
console.log(s);
console.log(typeof s); // like this we can use console also
// for now learn that object is like set of collections 
const student={
    fullName :"Mnv Sravan", // this is key:value,
    CGPA:9,
    age:18,
    isPass:true,

};
 student["fullName"]="sravan";
student["age"] = student["age"]+1;
console.log(student);
console.log(student["age"]); // like this we can ask any thing in it , we can use student.age instead of that
console.log(student.fullName);
