
function oneEditAway(s1,s2) {
    if(Math.abs(s1.length-s2.length>1)){
        return false;
    }
    var short = s1.length < s2.length ? s1 : s2;
    var long = s1.length < s2.length ? s1 : s2;
    console.log(short);

    var index1 = 0;
    var index2 = 0;
    fd = false;
    while(index2 < s2.length && index1 < s1.length){
        if(s1[index1] != s2[index2]){
            // ensure this is the first difference found
            console.log(s1[index1] ,' and ', s2[index2])
            if(fd){return false}
            fd = true;

            if (s1.length == s2.length){
                console.log('index1 incd');
                index1+=1;
            }
        }else{
            index1+=1;
        }
        index2+=1;
    }
    return true;
}


// console.log(oneEditAway('aaale','paale'));
// console.log(oneEditAway('pale','pale'))
console.log(oneEditAway('pales','pale'))
// console.log(oneEditAway('pale','bale'))
// console.log(oneEditAway('pale','bake'))
// console.log(oneEditAway('paa','paaa'))
