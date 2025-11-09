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
    console.log("I fuck u"); // Till here it is pending
    reject("not u nigga"); // here it gets rejected, this pops up like an error btw
    // resolve("suceesss"); here it gets resolved
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

// prmomise chain
function asyncFunc1() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log("some data1");
      resolve("success");
    }, 2000);
  });
}

function asyncFunc2() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log("some data2");
      resolve("success");
    }, 2000);
  });
}

console.log("fetching results for 1...");
let p1 = asyncFunc1(); // ✅ call the function
p1.then((res) => {
  console.log(res);
});

console.log("fetching results for 2...");
let p2 = asyncFunc2(); // ✅ call the function
p2.then((res) => {
  console.log(res);
});
// if u want to run async2 after 1 then same like callback hell use insdie func

//console.log("fetching for 1");
//let p1 = asyncFunc1();
//p1.then((res) => {
 // console.log(res);
 // console.log("fetching for 2");
 // let p2 = asyncFunc2();
 // p2.then((res) => {
  //  console.log(res);
 // });
//});

// THE ABOVE CODE IS SAME AS

// console.log("fetching for 1...");
// asyncFunc1().then((res) => {
//   console.log(res);

//   console.log("fetching for 2...");
//   return asyncFunc2();  // return a new promise so it chains
// }).then((res) => {
//   console.log(res);
// });

function getinfo(dataID) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log("data", dataID);
      resolve("success");
    }, 2000);
  });
}

getinfo(1)
  .then((res) => {
    return getinfo(2);
  })
  .then((res) => {
    return getinfo(3);
  });
  // SAME ONLY BRO

  // function getinfo(dataID) {
//   return new Promise((resolve, reject) => {
//     setTimeout(() => {
//       console.log("data", dataID);
//       resolve("success");
//     }, 2000);
//   });
// }

// getinfo(1).then((res) => {
//   console.log(res);
//   getinfo(2).then((res) => {
//     console.log(res);
//   });
// });

// async-await 

async function getAllData() { // declare a async func
  console.log("getting data1....");
  await getinfo(1); // we use the base body code
  console.log("getting data2....");
  await getinfo(2);
  console.log("getting data3....");
  await getinfo(3);
  
}
getAllData(); // we call it to invoke

// if u want to self invoke we use IIFE

// (async function getAllData() { // declare an async function
//   console.log("getting data1....");
//   await getinfo(1); // we use the base body code
//   console.log("getting data2....");
//   await getinfo(2);
//   console.log("getting data3....");
//   await getinfo(3);
// })();
 /// we notice that we dint call getAllData at the last , i.e self invoking





