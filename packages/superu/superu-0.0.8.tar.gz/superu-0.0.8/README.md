# superU Python Package

## Intent Classification for LLM

This functionality is designed to help you build and test models for intent classification for various user queries. Below, you will find the list of defined classes and how to use the functionality. 

### Intent categories on user queries:

- Informational
- Navigational
- Transactional
- Commercial

### Additional tags:

- Human Support (Requested for human support)
- Support (Looking for help)
- FAQ
- Language: {English, Hindi, Mandarin}


## User Persona

This functionality is designed to identify the persona of a user based on their conversations or statements. By analyzing the text, it extracts and identifies key aspects of a user's persona, such as age, gender, profession, hobbies, relationship status, and city.

### Requirements for building user persona with open source LLaMA3
To inference LLaMA3 on CPU it is necessary to have completed the setup of Ollama.
1. Ensure you have installed docker on your desktop. You can install it from https://docs.docker.com/engine/install/
2. Run the below command on your terminal to clone the ollma image on your docker container
```bash
docker pull ollama/ollama
```
3. Run the docker container using the below command
```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```
4. Go to Exec/Terminal in docker and run the command to install the LLaMA3 model
```bash
ollama run llama3
```
5. Once you have completed the above steps, you can successfully build user persona using open source LLaMA3 via Ollama

### Key data points considered
- Age
- Gender
- City
- Profession
- Relationship Status
- Interests
- Contact Info


## LLM Analytics

This functionality allows you to track metrics (cost, latency, quality) about the usage of your LLM in the chatbot and gain key insights about your users.


### Get your API Credentials for LLLM Analytics

To start using the superU's Free Analytics API service, follow these steps:

1. Visit analytics.superu.ai.
2. Sign up for a free account or log in if you already have one.
3. Create a new Project.
4. Navigate to the Settings > API keys section.
5. Generate your superU API keys.


## Usage

### Installing the package

```bash
pip install superu
```

### Example Usage
```python
import openai
import superu

openai.api_type = ""
openai.api_key = ""
openai.azure_endpoint = ""
openai.api_version = ""
User_Persona_1 = superu.superU.Build_User_Persona_OpenAI(openai, llm_deploymentname='')
User_Persona_2 = superu.superU.Build_User_Persona_LLaMA3()
Intent_Classification_1 = superu.superU.Intent_Classification()

prompt = "What is 1 + 1"

intent = Intent_Classification_1.get_intent(prompt)
user_persona_openai = User_Persona_1.build([prompt])
user_persona_llama3 = User_Persona_2.build([prompt])


messages = [{"role": "system", "content":"You are a helpful assistant."}]
message_r = {"role": "user", "content": f"{prompt}"}
messages.append(message_r)
response = openai.chat.completions.create(model="", messages=messages)

data = {
    "input_messages": messages,                                         # Required - Input Messages 
    "output_messages": response.choices[0].message.content,      # Required - the output from the model
    "metadata": {"user": "test-user", "context": "openai testing"},     # Optional - to give some metadata to the conversation
    "model": response.model,                                     # Required - Name of the model
    "user_id": "pip package test",                                                      # Optional - if not given a user_id will be generated
    "usage": response.usage.model_dump(),                        # Optional - usage details to track the model usage and costs
    "name": "test"                                                          # Optional - to name the given conversation 
}

service_client = superu.superU.LLM_Analytics(public_key="", secret_key="")

service_client.analyse(data)

print("Intent: ", intent)
print("User Details OpenAI: ", user_persona_openai)
print("User Details LLaMA3: ", user_persona_llama3)

```


## Contributing

We welcome contributions to this project! If you have suggestions for improvements or bug fixes, feel free to open an issue or submit a pull request.
