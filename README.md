# Disease Prediction with NLP

In this project we will  [this](https://google.com)  .

This gives 2 deployment options:
- Sympthoms
- Desease

## Initial Setup:
This repo currently contains

Clone repo and create a virtual environment
```
$ git clone 
$ cd Engineering-Project-II
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package - REQUIREMENTS.TXT!
```
$ (venv) python
>>> import nltk
>>> nltk.download('all')
```
Modify `intents.json` with

Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python chat.py
```

Now for deployment `app.py` and `app.js`.

## Note
In the [standalone](/standalone) folder.

## Links
https://stackoverflow.com/questions/55037071/how-to-find-medical-words-from-a-sentence-using-python
https://stackoverflow.com/questions/37926652/how-to-find-best-match-of-disease-from-symptoms
https://healthitanalytics.com/news/identifying-disease-with-natural-language-processing-technology


