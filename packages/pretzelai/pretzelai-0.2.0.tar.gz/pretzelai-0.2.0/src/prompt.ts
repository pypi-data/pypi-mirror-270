export function generatePrompt(
  userInput: string,
  oldCode: string,
  topSimilarities: string[]
): string {
  return `The user wants to do the following:
"""
${userInput}
"""

${
  oldCode
    ? `The following code already exists in the notebook cell:
"""
${oldCode}
"""

`
    : ''
}
${
  topSimilarities.length > 0
    ? `We also have the following matching code chunks in the notebook\n---\n${topSimilarities.join('\n---\n')}\n---\n`
    : ''
}
Based on the above, return ONLY executable python code, no backticks.`;
}

export const systemPrompt =
  'You are a helpful assistant that helps users write python code in Jupyter notebook cells. ' +
  'You are helping the user write new code and edit old code in Jupyter notebooks. ' +
  'You write code exactly as if an expert python user would write, reusing existing variables and functions as needed. ' +
  'You respond with the clean, good quality, working python code only, no backticks.';
