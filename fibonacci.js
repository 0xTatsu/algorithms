// 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

const cache = {};

function fibonacci(number) {
    
    if (number < 1)
        return 0;

    if (number <= 2)
        return 1;
    
    if (number in cache)
        return cache[number];
    
    const value = fibonacci(number- 1) + fibonacci(number - 2);
        
    cache[number] = value;

    return value;
}

// Ref: https://bit.ly/2kFdtvR
