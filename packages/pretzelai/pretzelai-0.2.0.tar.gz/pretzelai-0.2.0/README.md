Pretzel AI is an Jupyter extention for context-aware AI codegen in Jupyter.

# Quick start

## Installation

In the same virtual environment where Jupyter is installed, run:

```bash
pip install pretzelai
```

Reload Jupyter to enable the extension.

Next, you need to set up the OpenAI API key. Go to Settings > Settings Editor (or press Command + ,)

![](assets/screenshot_1.png)

Then, search for Pretzel AI in the top left search bar, select `OpenAI API key` as the AI Service and set the API key.

![](assets/screenshot_2.png)

## Usage

In any cell, press `Command + K` to prompt with GPT4. This opens a prompt window.

In the prompt window, type your instruction. Note that:

- you can refer to existing variables and dataframes with the `@variable` syntax (for example, if you have a dataframe `df`, you can refer to it with `@df`)
- The AI has access to all code in your current notebook as well so you can refer to other parts of the code as well

Press `Enter` or the Submit Button to get the answer. Press `Command + K` again to hide the prompt window.

![](assets/screenshot_3.png)

You can look at the AI response as a diff (if there was some code already in the cell).

![](assets/screenshot_4.png)

You can accept this by clicking the Accept button in the prompt window. This will update the cell with the new code **and run the new code!**

![](assets/screenshot_5.png)

# Choosing your AI Server

You have three options for AI Servers:

1. OpenAI API Key: This is the default, just set your OpenAI API key in the Settings Editor. We also allow setting a cutom URL in case your company has a local GPT-4 deployment.
2. Azure AI Server: If your company is running OpenAI models on Azure, you can set the Azure URL, project name and your API key here.
3. Pretzel AI Server: This is a wrapper of GPT-4 that we're running. It's free to use and the easiest way to get started. (AI responses aren't streamed with this server right now)

You can set the AI Service in the Settings Editor.
