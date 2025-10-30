console.log("hello");
console.dir(window);
console.dir(window.document);
//in the Document Object Model (DOM), a node is any single point in the document tree — every part of an HTML or XML document (like elements, text, comments, etc.) is represented as a node.
//🧩 Types of DOM Nodes:
///Node Type	Example	Description
//Element Node	<p>, <div>	Represents HTML elements.
//Text Node	"Hello World"	The actual text inside an element or attribute.
//Attribute Node	class="title"	Represents attributes of an element (accessed via .attributes).
//Comment Node	<!-- comment -->	Represents comments in the HTML.
//Document Node	document	Represents the entire webpage/document itself
console.dir(document.body);
console.dir(document.body.childNodes);
console.dir(document.body.childNodes[3]);
// we can do dynamic changes by like document.body.style.background="green" etc
// document.body.childNodes[3].innerText="YO BRO"
// DOM Manupulation

let one = document.getElementById("heading");
console.dir(one);
let two=document.getElementsByClassName("myclass");
console.dir(two);
console.log(two);
let para=document.getElementsByTagName("p");
console.dir(para);
let firstEl=document.querySelector(".myclass"); // 1st element
console.dir(firstEl);
let El=document.querySelectorAll(".myclass"); // ALL element
console.dir(El);
// in "" we need to use the same titles like in css like . for class # for id etc
console.dir(firstEl.tagName);
let div=document.querySelector("div");
console.dir(div.innerText);
console.dir(div.innerHTML);
// u can change dynamically like div.innerText="ahjagyugfd"
// same like for inner HTML also
let hidden=document.querySelector("h4");
console.dir(hidden.innerText);
console.dir(hidden.textContent); // even shows hidden elemets
//
//
let h2 = document.querySelector("h2");

console.dir(h2.innerText);

h2.innerText = h2.innerText + " from Apna College students";

let divs = document.querySelectorAll(".box");

let idx = 1;
for (div of divs) {
    div.innerText = `new unique value ${idx}`;
    idx++;
}

