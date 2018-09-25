// define a function to rotate a given array to the left n number of times.
// example array = 1,2,3,4,5 n = 1 output = 2,3,4,5,1

function rotate(arr,n){
    var newArr = []
    for (let i = n; i < arr.length; i++){
        newArr.push(arr[i]);
    }
    for (let i = 0; i < n; i++){
        newArr.push(arr[i]);
    }
    return newArr;
}

console.log(rotate([1,2,3,4,5],5));
    