function bribe(arr){
    let moves = 0;
    // check for fast fail
    for (let num = 0; num < arr.length; num++){
        if(arr[num+1]){
            if (arr[num]-arr[num+1] > 2) {
                console.log(arr[num],arr[num+1]);
                return ('fail');
            }
        }
    }
    console.log('before ',arr);
    for (let num = 0; num < arr.length; num++){
        if (arr[num+1]){
            if (arr[num+1] < arr[num]){
                console.log(arr[num],arr[num+1])
                let temp = arr[num];
                arr[num]=arr[num+1];
                arr[num+1]=temp
                moves+=1;
                // console.log('between ', arr);
            }
        }
    }
    console.log('after ',arr);
    return(moves);
}


// console.log(bribe([5,2,3,1,4]));
// console.log(bribe([1,3,2,4,5]));
console.log(bribe([1,4,3,2,5]));
// console.log(bribe([4,3,1,2]));