# Talkative

## Installation 

### Create virtual environment

```
python -m venv <env_name>
```

### Activate the virtual environment

```
source <env_name>/bin/activate
```

### Install dependencies
Install the dependencies using the following command:

```
pip install -r requirements.txt
```

NOTE: The following dependencies will be installed:
`streamlit`, 
`langchain`, 
`SpeechRecognition`,
`pyaudio`, 
`pydub`, 
`python-dotenv`, 
`openai`

### Update the OpenAI API key

Create an environment file (`.env`) inside the root folder and set the OpenAI API key inside it as below: 

```
apikey = 'my-api-key'
```


## Running the app

Run the following command inside the root folder. If everything is fine, you should hear the voice of the AI bot. 

```
streamlit run app.py
```

