# Name

__name__ uses NLP techniques to detect plagiarism is text files. It can be used to find plagiarism in essays and other exam responses with about 80% accuracy.

## Usage

To run the web server, install dependencies using the command:

```bash
pip3 install -r <requirements.txt
```

Then, run the server using:

```bash
export FLASK_APP=main.py
# uncommend following line to run the server in debug mode
# export FLASK_ENV=development
flask run
```

To run the cli, install dependencies using: 

```bash
pip3 install -r <requirements_2.txt
```

Then, to run the server, use:

```bash
python3 cli.py
```

