function getRandomNumber(min: number, max: number): number {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}


function createRandomArray(length: number): number[] {
  const randomArray: number[] = [];
  for (let i = 0; i < length; i++) {
    randomArray.push(getRandomNumber(1, 100));
  }
  return randomArray;
}

export const postIds: number[] = createRandomArray(10);
