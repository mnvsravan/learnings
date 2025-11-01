console.log("HELLO");
let btn1 = document.querySelector("#btn1");

btn1.onclick = (evt) => { // this is our pointer fucntion only
    console.log(evt);
  console.log("HANDLER1");
  let a = 25;
  a++;
  console.log(a); // 26
  console.log(evt.type);
  console.log(evt.target);
  console.log(evt.clientX,evt.clientY);
};

let div = document.querySelector("div");
div.onmouseover = (evt) => {
    console.log(evt);
  console.log("you are inside div");
  console.log(evt.type);
  console.log(evt.target);
  console.log(evt.clientX,evt.clientY);
};

// event listners
btn1.addEventListener("click", (evt) => {
  console.log("button1 was clicked - handler1");
});

btn1.addEventListener("click", () => {
  console.log("button1 was clicked - handler2");
});

const handler3 = () => {                                             // here we created a handler3 fucntion cuz we wanted to remove the handler 3 fucntion in the remove event list cuz the syntax is (event,function)
  console.log("button1 was clicked - handler3");
};

btn1.addEventListener("click", handler3);

btn1.addEventListener("click", () => {
  console.log("button1 was clicked - handler4");
});

btn1.removeEventListener("click", handler3);

let modeBtn = document.querySelector("#mode");
let body = document.querySelector("body");
let currMode = "light"; //dark

modeBtn.addEventListener("click", () => {
  if (currMode == "light") {
    currMode = "dark";
    body.classList.add("dark");
    body.classList.remove("light");
  } else {
    currMode = "light";
    body.classList.add("light");
    body.classList.remove("dark");
  }

  console.log(currMode);
});
