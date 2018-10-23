// Here, we’re checking that every item (x) is greater than or equal to the item before it (arr[i - 1]) 
// or has no item before it (i === 0).

function isAscending(arr) {
    return arr.every(function (x, i) {
        return i === 0 || x >= arr[i - 1];
    });
}

// Flip >= to <= for isDescending.
