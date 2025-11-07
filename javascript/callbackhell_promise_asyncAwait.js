//function hello(){
  //  console.log("hello");
//}
//setTimeout(hello,2000); // like 2000 is 2s
console.log("one");
console.log("one1");
console.log("one2");
setTimeout (()=>{
console.log("hello"); 
},2000);
console.log("one3");
// like this are wont go in order

function sum(a,b){
    console.log(a+b);
}
function calculator(a,b,sumcallback){
//sumcallback=sum;
sumcallback(a,b);
}
calculator(1,2,sum);

function getData(dataId, getNextData) {
  setTimeout(() => {
    console.log("data", dataId);
    if (getNextData) {
      getNextData(); // ✅ call the callback after printing
    }
  }, 2000);
}

getData(1, () => {
  getData(2);
});


/*
function getData(dataId, getNextData) {
  setTimeout(() => {
    console.log("data", dataId);
    if (getNextData) {
      getNextData();
    }
  }, 2000);
}

getData(1, () => {
  getData(2, () => {
    getData(3, () => {
      getData(4, () => {
        getData(5, () => {
          getData(6, () => {
            getData(7);
          });
        });
      });
    });
  });
});
*/

// PROMISE
let promise= new Promise((resolve,reject)=>{
    console.log("I fuck u");
    reject("not u nigga");
});

function getData1(dataId) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log("data", dataId);  // ✅ this will print
      resolve("success bro");       // ✅ this will resolve
    }, 2000);
  });
}

// ✅ NOW call the function properly:
getData1(1).then((res) => {
  console.log(res);  // ✅ prints the resolved message
});
// if we used reject instead of resolves we use .catch instead of then
// like 
const getPromise=()=>{
    return new Promise((resolve,reject)=>{
        console.log("wrgergrge");
        reject("errorororoor");
    });
};
let promise2=getPromise();
promise2.then((res) => {
    console.log("nice",res);
});
promise2.catch((err) => {
    console.log("fool",err);
});


