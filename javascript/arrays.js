let marks = [100 ,99 ,88 ,46,48 ,65];
marks[0]=33; // arrays are mutable unlike strings
console.log(marks);
console.log(marks.length);
for(let mark of marks){
    console.log(mark);
}
let heroes=["ironamn", "thor", "spiderman"];
console.log(heroes);
for(let i=0;i<heroes.length;i++){ // u can use i<3 also
    console.log(heroes[i]);
    console.log(heroes[i].toUpperCase())
}
let numbers=[100,100,200,200,400];
let sum=0;
for(let val of numbers){
    sum+=val;
}
let avg=sum/numbers.length;
console.log(`AVG MARKS ARE = ${avg}`);

let item = [250, 645, 300, 900, 50];

for (let i = 0; i < item.length; i++) {
    let offer = item[i] - (0.1 * item[i]);
    console.log("The final price is", offer);
}
// or 
// let items = [250, 645, 300, 900, 50];

// let i = 0;
// for (let val of items) {
//     let offer = val / 10;
//     items[i] = items[i] - offer;
//     console.log(`value after offer = ${items[i]}`);
//     i++;
// }


// push() : adds to end
// pop(): delete from end and return
// toString(): converts array to string (dosent change actual array)
let trial1 = ["potato", "banana", "mango"];
trial1.push("chips", "lays", "kurkure");
console.log(trial1);
let deleteditem=trial1.pop("mango"); // u need to do like this
console.log(trial1);
console.log(trial1.toString());

// concat(): joins multiple arrays and returns result(dosent change original array)
// unshift(): adds to the start
// shift(): deletes from start
let marvel=["sravan","antman"];
let dcheroes=["superman","batman"];
let aurafarmers=trial1.concat(marvel,dcheroes);
console.log(aurafarmers);
aurafarmers.unshift("prabhas");
console.log(aurafarmers);
aurafarmers.shift("prabhas");
console.log(aurafarmers);

// slice(): retuerns a piece of array(no change in original)
// like in format ( startidx,endidx)
// splice(): change origianl array(add,rmove,reeplace)
// syntax(startidx,delcount,newaddons)

console.log(marks.slice(1,2));
console.log(marks.slice(1,6));
console.log(marks.slice(0,2));
console.log(marks.slice(4));
console.log(marks.splice(2,2,101,102));
console.log(marks);
console.log(marks.splice(2,0,103));
console.log(marks);
console.log(marks.splice(2,1));
console.log(marks);
console.log(marks.splice(2));
console.log(marks);
