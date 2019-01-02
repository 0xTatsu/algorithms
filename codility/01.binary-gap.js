function solution(N) {
  return Math.max(
    ...N.toString(2)
      .replace(/^0+|0+$/g, '')
      .split(1)
      .map(l => l.length)
  );
}

console.log('solution(529)', solution(529));
