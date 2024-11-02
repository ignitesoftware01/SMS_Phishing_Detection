# SMS_Phishing_Detection

it's a SMS Phishing Detection Software

working,
when we paste sms in the text area of the website,
it goes through 3 different processes, and it will show 3 outputs in 3 areas

1. Check if the SMS contains common Phishing Keywords
2. Check whether the SMS contains a link or not
3. if the link is available, it checks whether the link is Spam or not according to the dataset

# Installing required packages
=> for app.py 
pip install Flask Flask-CORS scikit-learn numpy pandas requests
=> for model training



# How to run
  run app.py
  command- python app.py  
  
data set: url_spam_classification.csv
modeltraining.ipynb : training the model and stored to the model.py
metrics graph folder contains graphs according to different parameters, on this we got random forest algorithm got best accuracy, so model trained using random forest algorithm 
