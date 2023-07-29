# Talkative

## Installation 

### Create virtual environment

```
python -m venv <env_name>
```

### Activate the virtual environment

```
source <venv>/bin/activate
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

Create an environment file named `.env` inside the root folder and set the OpenAI API key inside the file. For e.g: 

```
apikey = 'my-api-key'
```


## Running the app

```
streamlit run app.py
```

