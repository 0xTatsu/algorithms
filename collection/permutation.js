function permuteStr(inputStr) {
  let result = [];

  for (let i = 0; i < inputStr.length; i++) {
    const firstChar = inputStr[i]; // firstChar = 'J'
    const leftChars = inputStr.substring(0, i) + inputStr.substring(i+1); // leftChars = 'ACK'
    let leftCharsArr = leftChars.split(""); // leftCharsArr = ['A', 'C', 'K']

    for (let j = 0; j < leftCharsArr.length; j++) {
      result.push(firstChar + leftCharsArr.join("")); // result = ['JACK']
      leftCharsArr.unshift(leftCharsArr.pop()); // leftCharsArr = ['C', 'K', 'A']
    }

  }
  return result;
}
console.log(permuteStr("JACK"));

// Complexity: O(n!)
// Ref: https://initjs.org/all-permutations-of-a-set-f1be174c79f8
