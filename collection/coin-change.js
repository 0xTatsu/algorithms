const countChange = function(coins, amount) {
  let cb = Array(amount + 1).fill(0); // [0, 0, 0]
  cb[0] = 1;
  for (let i = 0; i < coins.length; i++) {
    for (let j = 0; j <= amount; j++) {
      cb[j] += cb[j - coins[i]];
    }
  }
  return db[amount];
};

const countChange2 = function(coins, amount, index = coins.length - 1) {
  if (amount === 0) return 1;
  if (amount < 0 || index < 0) return 0;
  return (
    countChange2(coins, amount, index - 1) +
    countChange2(coins, amount - coins[index], index)
  );
};
