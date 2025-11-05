const student={
    fullName:"MNVSRAVAN",
    marks:99,
    printMarks: function () {
        console.log("marks= ",this.marks); // this this key word is for like getting access
    },
};
const employee={
    calcTax () {
        console.log("tax is 10%");
    }
    // you can also write like calcTax: function (){
    //  content
    //          }
};

const Sravan={
    salary:1000000,
};
Sravan.__proto__=employee;
// like this u can create so many ppls and __proto__=employee them
// now like if in sravan also there is some calc tax same varible , them prefernce is sravan

// classes other formats also

class ToyotaCar {
  constructor(brand, mileage) {
    console.log("creating new object");
    this.brand = brand;
    this.mileage = mileage;
  }

  start() {
    console.log("start");
  }

  stop() {
    console.log("stop");
  }
}

let fortuner = new ToyotaCar("fortuner", 10); //constructor
console.log(fortuner);
let lexus = new ToyotaCar("lexus", 12); //constructor
console.log(lexus);

// Inheritance

class Person {
    constructor(){
        this.species="homo sapiens";
    }
  eat() {
    console.log("eat");
  }

  sleep() {
    console.log("sleep");
  }

  work() {
    console.log("do nothing");
  }
}

class Engineer extends Person {
  work() {
    console.log("solve problems, build something");
  }
}

class Doctor extends Person {
  work() {
    console.log("treat patients");
  }
}
let obj = new Engineer;

// SUPER like when constructors are sep
class Human {
  constructor() {
    console.log("enter parent constructor");
    this.species = "homo sapiens";
  }

  eat() {
    console.log("eat");
  }
}

class Me extends Human {
  constructor(branch) {
    console.log("enter child constructor");
    super(); // to invoke parent class constructor
    this.branch = branch;
    console.log("exit child constructor");
  }

  work() {
    super.eat();// u can call like this also 
    console.log("solve problems, build something");
  }
}

let myObj = new Me("CSE");

// u can pass values also

class Human1 {
  constructor(name) {
    console.log("enter parent constructor");
    this.species = "homo sapiens";
    this.name=name;
  }

  eat() {
    console.log("eat");
  }
}

class Me1 extends Human1 {
  constructor(name,branch) {
    console.log("enter child constructor");
    super(name); // to invoke parent class constructor
    this.branch = branch;
    console.log("exit child constructor");
  }

  work() {
    console.log("solve problems, build something");
  }
}

let myObj1 = new Me1("MNVSRAVAN","CSE");



// eg problem

let DATA = "secret information";

class User {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  viewData() {
    console.log("data = ", DATA);
  }
}

class Admin extends User {
  constructor(name, email) {
    super(name, email);
  }

  editData() {
    DATA = "GUESS WHAT I CAN SEE IT ";
  }
}

let student1 = new User("shradha", "abc@email.com");
let student2 = new User("Messi", "messi@email.com");
let sravan=new Admin("GOAT","mnvsravan07@gmail.com")

// how to track errors
// ususallly if errors occur the programme stops there and excecuton stops , but this just stops the problem and let the remaingin code continue





let a = 5;
let b = 10;
console.log("a = ", a);
console.log("b = ", b);
console.log("a+b = ", a + b);

try {
    console.log("a+b = ", a + c); //error
} 
catch (err) {
    console.log(err);
}

console.log("a+b = ", a + b);
console.log("a+b = ", a + b);
console.log("a+b = ", a + b);
console.log("a+b = ", a + b);
console.log("a+b = ", a + b);
