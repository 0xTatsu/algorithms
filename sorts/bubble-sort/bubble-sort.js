/**
 *  Bubble Sort
 *  Complexity: O(n^2)
 *  @param {Array} arr
 *  @return {Array} sorted data
 */

function bubbleSort(arr){
    const len = arr.length;
    for (let i = len-1; i >= 0; i--){
        for (let j = 0; j < i; j++){
            if (arr[j] > arr[j+1]){
                [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
            }
        }
    }
    return arr;
}

const data = [9, 2, 5, 6, 4, 3, 7, 10, 1, 8];
const sortedData = bubbleSort(data);
console.log(sortedData);