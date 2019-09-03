// leetcode 396

const rotateArrayMaxForMaxValue = (A) => {
  let len_A = A.length;
  let sum_A = 0;
  let product_sum = 0;

  for (let i=0; i < len_A; i++) {
    sum_A += A[i];
    product_sum += A[i] * i;
  }
  let max = product_sum;
  for (let j=len_A-1; j > 0; j--) {
    product_sum += sum_A - (A[j] * len_A);
    max = Math.max(product_sum, max);
  }
  return max
}

console.log(rotateArrayForMaxValue([3,4,2,1,2]));
    
    

