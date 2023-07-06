# STEDI Human Balance Analytics
Building a data lakehouse solution for sensor data that trains a machine learning model
## Project Details
The STEDI Team has been hard at work developing a hardware STEDI Step Trainer that trains the user to do a STEDI balance exercise and has sensors on the device that collect data to train a machine-learning algorithm to detect steps has a companion mobile app that collects customer data and interacts with the device sensors.
STEDI has heard from millions of early adopters who are willing to purchase the STEDI Step Trainers and use them.
Several customers have already received their Step Trainers, installed the mobile application, and begun using them together to test their balance. The Step Trainer is just a motion sensor that records the distance of the object detected. The app uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions.
The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Privacy will be a primary consideration in deciding what data can be used.
Some of the early adopters have agreed to share their data for research purposes. Only these customers’ Step Trainer and accelerometer data should be used in the training data for the machine learning model.

We'll need to extract the data produced by the STEDI Step Trainer sensors and the mobile app, and curate them into a data lakehouse solution on AWS so that Data Scientists can train the learning model.

## Project Data
STEDI has three JSON data sources to use from the Step Trainer.

customer  (https://github.com/udacity/nd027-Data-Engineering-Data-Lakes-AWS-Exercises/tree/main/project/starter/customer )
step_trainer  (https://github.com/udacity/nd027-Data-Engineering-Data-Lakes-AWS-Exercises/tree/main/project/starter/step_trainer )
accelerometer  (https://github.com/udacity/nd027-Data-Engineering-Data-Lakes-AWS-Exercises/tree/main/project/starter/accelerometer )

We will upload the json data after downloading it to our local. 
``` git clone https://github.com/anwesha-git/nd027-Data-Engineering-Data-Lakes-AWS-Exercises.git
``` cd nd027-Data-Engineering-Data-Lakes-AWS-Exercises//project/starter/
``` aws s3 ls s3://as-glue/customer/landing/
``` aws s3 cp ./accelerometer s3://as-glue/accelerometer/landing/ --recursive
``` aws s3 cp ./step_trainer s3://as-glue/step_trainer/landing/ --recursive



