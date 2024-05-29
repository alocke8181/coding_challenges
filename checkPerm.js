//Write a script to determine if two strings are permutations of each other
//This script excludes whitespace characters
//Runtime will depend on the browser's sort method, but should be O(n log(n))

const stringOne = process.argv[2];
const stringTwo = process.argv[3];

let oneChars = [...stringOne].map(char => {if(char != ' '){return char}}).sort();
let twoChars = [...stringTwo].map(char => {if(char != ' '){return char}}).sort();

if(oneChars.toString() == twoChars.toString()){
    console.log(true);
}else{
    console.log(false);
}
