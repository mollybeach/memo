let onlyChar= [...s].filter(e => /[a-z0-9]/.test(e)) filter out everything ot a letter or number 

let noSelf = arr.filter(e=> arr[e]!=nums[i]); happy random filter one array 
by unwanted in of another

  let y = Math.max(...(words.map(e => e.length)));
    res = words.filter(e => e.length<y);
/*********************************************************************************/

var productExceptSelf = function(nums) {
  let a=[], len=nums.length, res, pop;
  function multi(arr, ind, stop);
  if(stop>len) return res
let noSelf = arr.filter(i=> arr[i]!=nums[ind]);
console.log(noSelf)
  res = noSelf.reduce((a, b)=> a*b, 1)
   a.push(res)

  ind++;
  stop++;
  //arr.shift();
  
  multi(nums, ind, stop)
  }

 multi(nums, 0, 0)

return a
};
let noSelf = arr.filter(e=> arr[e]!=nums[i]); happy random filter one array 
by unwanted in of another 
with one e and one i not two i(s)?

/*[ 1, 2, 3, 4 ]
[ 2, 3, 4 ]
[ 1, 3, 4 ]
[ 1, 2, 4 ]
[ 1, 2, 3 ]
[ 24, 24, 12, 8, 6 ]*/
with two 
let noSelf = arr.filter(i=> arr[i]!=nums[i]);
[]
[]
[]
[]
[]
[ 1, 1, 1, 1, 1 ]
/****************************************FILTER EXAMPLES******************************/

The filter() method creates a new array with all elements that pass the test implemented by the provided function.
const words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];
const result = words.filter(word => word.length > 6);
console.log(result);

// expected output: Array ["exuberant", "destruction", "present"]

/*******Arrow function******/
filter((element) => { ... } )
filter((element, index) => { ... } )
filter((element, index, array) => { ... } )

/*****Callback function*******/
filter(callbackFn)
filter(callbackFn, thisArg)

/*****Inline callback function*******/
filter(function callbackFn(element) { ... })
filter(function callbackFn(element, index) { ... })
filter(function callbackFn(element, index, array){ ... })
filter(function callbackFn(element, index, array) { ... }, thisArg)

/*****************Find all prime numbers in an array********************/
The following example returns all prime numbers in the array:

const array = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];

function isPrime(num) {
  for (let i = 2; num > i; i++) {
    if (num % i == 0) {
      return false;
    }
  }
  return num > 1;
}

console.log(array.filter(isPrime)); // [2, 3, 5, 7, 11, 13]
Example 2. filter() and reduce() together
Problem Statement: This time we are required to print the sum of marks of the students with id > 120.
let totalMarks = studentRecords.filter(stu => stu.id > 120).reduce((acc,curr) => acc + curr.marks ,0)
console.log(totalMarks); // logs: 143



var productExceptSelf = function(nums) {
  let a=[], len=nums.length, i=0;
   while(i<len){
  if(i>=len) return res
  a.push(nums.filter(e => e!=nums[i]).reduce((acc,curr) => acc * curr ,1))
    i++; 
   }
return a;
};
productExceptSelf(nums = [1,2,3,4]); //Input



For a simple array you can do it like this with the filter method:

var req = ['test','#test1','#test2','test3','test4'];

var result = req.filter(item => !item.includes("#"));

console.log(result);
/*********************************************************************************/
let output =  "c2o0v1i9d";
  var reformat = function(s) {
  let cStr = [...s].filter(item => isNaN(item))
	let nStr = [...s].filter(item => !isNaN(item))
console.log(cStr)
  //return res
  }

  reformat( s = "j"); 


  var reformat = function(s) {
  let cArr = [...s].filter(e => isNaN(e))
	let nArr = [...s].filter(e => !isNaN(e))
  let cLen = cArr.length, nLen = nArr.length;
  if(Math.abs(nLen-cLen)>1) return ''
  let ifCArr = cLen > nLen ? cArr : nArr;
  let ifNArr = cLen > nLen ? nArr : cArr;
  	return ifCArr.reduce((a, c, i) => {
		return a + c + (ifNArr[i] || '')
	}, '')
  }

  reformat( s = "ec"); 
  }