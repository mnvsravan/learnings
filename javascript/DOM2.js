
let div= document.querySelector("div")
console.log(div);
let id=div.getAttribute("id");
console.log(id);
let name=div.getAttribute("name");
console.log(name);
// we can
let para=document.querySelector("p");
console.log(para.getAttribute("class"));
let para2=document.querySelector("p");
console.log(para2.setAttribute("class","fku"));
div.style.backgroundColor="brown";
div.style.fontsize="26px";
//div.innerText="hello";
div.style.width="100px";
div.style.height="300px";
div.style.textAlign="center";
//div.style.visibility="hidden"
// insert eleemts: , we create first like docuemnt.createelement
// first create trhen acess
let newBtn=document.createElement("button");
newBtn.innerText="clickme!";
console.log(newBtn);

div.prepend(newBtn);
div.append(newBtn); // format is node.append(el)
div.before(newBtn);
div.after(newBtn);
// BRO in all these above things im not using queryselector div cuz i already used it on top , for others u must use it every time
//div.remove(); it removews
let newheading=document.createElement("h1");
newheading.innerText="<i>hi, im sravan!</i>"
console.log(newheading);
let body=document.querySelector("body");
body.prepend(newheading);
// i already called the queryseselector for para so im not calling again
para.style.color="red";
para.classList("class","fku");
// classList is also like setarttribute


