# TPlag

TPlag uses NLP techniques to detect plagiarism is text files. It can be used to find plagiarism in essays and other exam responses with about 80% accuracy.

## Usage

The app can be used as a command line interface or a web interface.

The web interface supports uploading multiple files and a pair-wise plagiarism check for all the files. You can choose whether you want to classify files on basis of optimizing the F score or optimizing the accuracy. This is the recommended method for testing plagiarism in exams with large number of answers.

Meanwhile, the command line interface is recommended for exploratory purposes. It provides an option to optimizes either the F score (threshold around 5.64) of the classifications or the accuracy(threshold around 2.27) or provide a custom threshold!

For both, the server and the CLI, GLoVe embeddings are required. You can download them using the following command:

```bash
bash dl-script.sh # This will take some time
```

To run the web server, install dependencies using the command:

```bash
pip3 install -r <requirements.txt
```

Then, run the server using:

```bash
rm -rf files
mkdir files
export FLASK_APP=main.py
# uncommend following line to run the server in debug mode
# export FLASK_ENV=development
flask run
```

To run the CLI, install dependencies using: 

```bash
pip3 install -r <requirements_2.txt
```

Then, to run the server, use:

```bash
python3 cli.py
```

## Accuracy

The file was test against corpus from [here](https://ir.shef.ac.uk/cloughie/resources/plagiarism_corpus.html). Of the 95 files, 80% were classified correctly as plagiarised or not plagiarised in accuracy mode while an F score of 0.95 was achieved in f_score mode!

## To Do

1. Explore better model
2. Create UI
