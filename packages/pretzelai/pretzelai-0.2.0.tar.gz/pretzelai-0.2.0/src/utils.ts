export async function calculateHash(input: string) {
  const encoder = new TextEncoder();
  const data = encoder.encode(input);
  const hashBuffer = await crypto.subtle.digest('SHA-256', data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  return hashHex;
}

export const cosineSimilarity = (vecA: number[], vecB: number[]): number => {
  const dotProduct = vecA.reduce(
    (acc: number, current: number, index: number) =>
      acc + current * vecB[index],
    0
  );
  const magnitudeA = Math.sqrt(
    vecA.reduce((acc: number, val: number) => acc + val * val, 0)
  );
  const magnitudeB = Math.sqrt(
    vecB.reduce((acc: number, val: number) => acc + val * val, 0)
  );
  return dotProduct / (magnitudeA * magnitudeB);
};
