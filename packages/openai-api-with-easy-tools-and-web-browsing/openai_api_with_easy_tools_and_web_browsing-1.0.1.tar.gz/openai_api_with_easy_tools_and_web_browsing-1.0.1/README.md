# openai-api-with-easy-tools-and-web-browsing
An unofficial OpenAI library for Python, featuring an integrated Bing Custom Search API for web browsing (free) and easy-to-use custom tools.

See example below for a quick start.

First, get the library with [pip](https://pypi.org/project/openai-api-with-easy-tools-and-web-browsing/): **pip install openai-api-with-easy-tools-and-web-browsing**

Then, you can use the following code to get started:

```
import src.openai_api_with_easy_tools_and_web_browsing as webBrowsingApiGPT

# Enter our API keys
subscriptionKey = ""
openAIAPIKey = ""

### Creation of the Bing search tool ###

# Create a Bing search engine that synthesizes results with GPT-3.5-turbo
bingSearchEngine = webBrowsingApiGPT.BingSearchEngine(openAIAPIKey, subscriptionKey, model="gpt-3.5-turbo")
# Rename the Bing search function (otherwise it does not work as a tool in the OpenAI API)
bingSearch = bingSearchEngine.bingSearch
# Take the already made Bing search function description (the function must be named 'bingSearch')
bingSearchDescription = webBrowsingApiGPT.BING_SEARCH_DESCRIPTION

### Creation of the addition tool ###

def adder(a, b):
    """This function adds two numbers together"""
    return (str(a + b))

adderDescription = {
    "type": "function",
    "function": {
        "name": "adder",
        "description": "Add two numbers together",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {
                    "type": "integer",
                    "description": "The first number to add"
                },
                "b": {
                    "type": "integer",
                    "description": "The second number to add"
                },
            },
            "required": ["a", "b"]
        }
    }
}

# Create an instance of the 'OpenaiApiWithEasyToolsAndWebBrowsing' class
openaiEpiWithEasyToolsAndWebBrowsing = webBrowsingApiGPT.OpenaiApiWithEasyToolsAndWebBrowsing(openAIAPIKey)

### Return a response to a prompt in 'ponctual' mode ###
print("\n\n\nPONCTUAL MODE\n")
prompt = "Can you search the internet for the population of Paris and New York in the year 2015, then add the two values together and tell me the result, and then add 10,000,000 to that result"
# Use the 'getLLMAnswerWithWebBrowsingAndTools' function to get a response from a user message
answer = openaiEpiWithEasyToolsAndWebBrowsing.getLLMAnswerWithWebBrowsingAndTools(prompt, systemMessage="You are a helpful assistant", model="gpt-3.5-turbo", mode="ponctual", toolList=[bingSearch, adder], toolDescriptionList=[bingSearchDescription, adderDescription])
print(answer)

### Discussion in 'continuous' mode ###
print("\n\n\nCONTINUOUS MODE\n")
openaiEpiWithEasyToolsAndWebBrowsing.getLLMAnswerWithWebBrowsingAndTools(None, systemMessage="You are a helpful assistant", model="gpt-3.5-turbo", mode="continuous", toolList=[bingSearch, adder], toolDescriptionList=[bingSearchDescription, adderDescription])

```
