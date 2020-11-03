# Automatic Injection Attack Detection in HTTP Requests

[![](https://img.shields.io/badge/python-2.7%2C%203.5%2B-green.svg)]()
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)


------------------

## Getting started

- Clone this repo 
- Install requirements
- Download Keras models from google drive
- Run the script
- Check http://localhost:5000
- Done! :tada:

------------------

### Download saved Keras Models

For the application to work as intented after cloning this repository head on to 
https://drive.google.com/folderview?id=1BBkuhpruIORHjWK4VgH7ABD3COVap7E0
to view and download the keras models to your local computer and place them in the models folder
### Note
DO NOT CHANGE THE FILE NAME OF THE FILES AS SEEN ON THE GOOGLE DRIVE FOLDER, PLEASE MAINTAIN THE FILE NAME AS THE
PROGRAM MAKES USES OF THAT INFORMATION

### Run the app

Run the script.
```
$ python app.py
```
## Using the web application
To use the web application there are 3 steps
- select the dataset at which you want to test on (either csic of ecml)
- select the model you want to use to get the prediction results (either the ecml trained DNN or ecml trained CNN or csic trained DNN or csic trained CNN)
- click the `Sample 5 requests` button
Before running for new sets of data, plase reload the web browser

## NOTE WHEN SELECTING MODELS TO USE WHEN PROGRAM IS RUNNING
### Ensure the corresponding keras model for the selected model option in the application is downloded and saved in the models folder
Please only select the models at which you downloaded the saved keras model for in the web application so as to avoid server errors
if for example you want to use the  `ECML DATASEST TRAINED CNN MODEL` you must first download the `ecmlcnnkeras.h5` file from the google drive link above and place the downloaded file (with the filename intact) into the models folder, then you can select the option in the web application.
