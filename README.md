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

 `git clone https://github.com/anwesha-git/nd027-Data-Engineering-Data-Lakes-AWS-Exercises.git`
  cd nd027-Data-Engineering-Data-Lakes-AWS-Exercises//project/starter/
  aws s3 ls s3://as-glue/customer/landing/
  aws s3 cp ./accelerometer s3://as-glue/accelerometer/landing/ --recursive
  aws s3 cp ./step_trainer s3://as-glue/step_trainer/landing/ --recursive 

Below is the record details:
### Customer Records
contains the following fields:
serialnumber
sharewithpublicasofdate
birthday
registrationdate
sharewithresearchasofdate
customername
email
lastupdatedate
phone
sharewithfriendsasofdate
### Step Trainer Records
contains the following fields:
sensorReadingTime
serialNumber
distanceFromObject
### Accelerometer Records
contains the following fields:
timeStamp
user
x
y
z

## Requirement
  To simulate the data coming from the various sources, we will need to create our own S3 directories for customer_landing, step_trainer_landing, and accelerometer_landing zones, and copy the data there as a starting point.
  To get a feel for the data we are dealing with in a semi-structured format, we will create two Glue tables for the two landing zones. customer_landing and accelerometer_landing
  Sanitize the Customer data from the Website (Landing Zone) and only store the Customer Records who agreed to share their data for research purposes (Trusted Zone) - creating a Glue Table called customer_trusted.
  Sanitize the Accelerometer data from the Mobile App (Landing Zone) - and only store Accelerometer Readings from customers who agreed to share their data for research purposes (Trusted Zone) - creating a Glue Table called accelerometer_trusted
  Sanitize the Customer data (Trusted Zone) and create a Glue Table (Curated Zone) that only includes customers who have accelerometer data and have agreed to share their data for research called customers_curated.
  The serial number should be a unique identifier for the STEDI Step Trainer they purchased. The data from the Step Trainer Records has the correct serial numbers. We need to join them with customer data. Read the Step Trainer IoT data stream (S3) and populate a Trusted Zone Glue Table called step_trainer_trusted that contains the Step Trainer Records data for customers who have accelerometer data and have agreed to share their data for research (customers_curated).
  Create an aggregated table that has each of the Step Trainer Readings, and the associated accelerometer reading data for the same timestamp, but only for customers who have agreed to share their data, and make a glue table called machine_learning_curated.
