let boxes= document.querySelectorAll(".box");
let reset=document.querySelector("#reset");
let newgame=document.querySelector("#new");
let container=document.querySelector(".idk");
let msg=document.querySelector("#msg");
let turnO=true;
const winPatterns = [
  [0, 1, 2],
  [0, 3, 6],
  [0, 4, 8],
  [1, 4, 7],
  [2, 4, 6],
  [2, 5, 8],
  [3, 4, 5],
  [6, 7, 8],
];

const resetGame=()=>{
    turnO=true;
    enableBoxes();
    container.classList.add("hide");
    msg.innerText="";
}

boxes.forEach((box) => {
  box.addEventListener("click", () => {
    console.log("box was clicked");
    if (turnO) {
      box.innerText = "O";
      turnO = false;
    } else {
      box.innerText = "X";
      turnO=true;
    }
    box.disabled=true;
    checkWinner();
  });
});

const disableBoxes=()=>{
    for(let box of boxes){
        box.disabled=true;
    }
};

const enableBoxes=()=>{
    for(let box of boxes){
        box.disabled=false;
        box.innerText="";
    }
};

const showwinner=(winner)=>{
    msg.innerText=`Congratulations , winner is ${winner}`;
    container.classList.remove("hide");
};

const checkWinner = () => {
  for (let pattern of winPatterns) {
    let pos1Val = boxes[pattern[0]].innerText;
    let pos2Val = boxes[pattern[1]].innerText;
    let pos3Val = boxes[pattern[2]].innerText;

    if (pos1Val != "" && pos2Val != "" && pos3Val != "") {
      if (pos1Val === pos2Val && pos2Val === pos3Val) {
        console.log("winner is ",pos1Val);
        showwinner(pos1Val);
        disableBoxes();
      }
    }
  }
};

newgame.addEventListener("click",resetGame);
reset.addEventListener("click",resetGame);



