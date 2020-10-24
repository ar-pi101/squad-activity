# ParkingLot
## Problem Statement

We own a parking lot that can hold up to ‘n’ cars at any given point in time. Each slot is given a number starting at one increasing with increasing distance from the entry point in steps of one. We want to create an automated ticketing system that allows our customers to use our parking lot without human intervention.
When a car enters the parking lot, we want to have a ticket issued to the driver. The ticket issuing process includes:- 
1.	We are taking note of the number written on the vehicle registration plate and the age of the driver of the car.
2.	And we are allocating an available parking slot to the car before actually handing over a ticket to the driver (we assume that our customers are kind enough to always park in the slots allocated to them).

The customer should be allocated a parking slot that is nearest to the entry. At the exit, the customer returns the ticket, marking the slot they were using as being available.

Due to government regulation, the system should provide us with the ability to find out:- 
- Vehicle Registration numbers for all cars which are parked by the driver of a certain age,
- Slot number in which a car with a given vehicle registration plate is parked. 
- Slot numbers of all slots where cars of drivers of a particular age are parked.

We interact with the system via a file-based input system, i.e. it should accept a filename as an input. The file referenced by filename will contain a set of commands separated by a newline, we need to execute the commands in order and produce output.

## Environment

```bash
version : 1.0
environment : python2.7
```
## How to run

The bash file *parking_lot* is used to take filepath. Run the below command in the home directory of the project.
```bash
./parking_lot file_inputs.txt
```

# Getting Started

## Project structure

```
parking_lot-master/
|-- README.md
|-- parking_lot
|-- file_inputs.txt
|-- requirements.txt
|-- source
|   |-- __init__.py
|   |-- car.py
|   |-- driver.py
|   |-- lot.py
|   |-- parking.py
|   |-- parking_lot.py
|-- tests
|   |-- __init__.py
|   |-- env.py
|   |-- test_parking_lot.py

```

Source directory contains the following python source files:
- car.py : Containing Car Attributes and Behavior
- driver.py : Containing Driver Attributes and Behavior
- lot.py : Containing Parking Lot Attributes and Behavior
- parking_lot.py : Used to parse the content of the files and process the commands as input from the file. 
- parking.py : Used to apply commands as directed in the input file

Tests directory contains unit tests for models and env, all executable from **test_parking_lot.py**.

Input File - 
- *file_inputs.txt* is used as input file. Kindly place the test cases in this file.

## Design
Every command in the input file can take upto 3 different properties – Registration Number, Age of the driver and Parking slot number. All the properties are independent of each other and thus it was needed to be defined separately.

Hence, 3 different Classes are created for **Car, Driver and ParkingSlot** to define their properties and behaviors. The same will be useful if we think of scaling the application for more functionalities.

Initially, the command *Create_parking_lot* is used to create a complete new parking lot of a defined length and an object of class ParkingSlot is created of the same length, with null values. Regex is used to check the validity of the registration number and a range is used to check the validity of the driver’s age. (range : 18 years to 100 years)

- The command *Park* is used to add cars in the parking slot at the nearest possible available slot. The nearest available slot is picked from the ParkingSlot object and defined by the registration number of the car and age of the driver.
- The command *Leave* is used to remove the cars in the parking slot. First it is checked if the car is present in the Parking Slot, if yes, the data of Car and Driver is removed from the respective slot.

3 other commands are noted to be - 
- *Slot_numbers_for_driver_of_age* – First checked if there exist a driver with the defined age, then displays the respective parking slot numbers separated by commas
- *Slot_number_for_car_with_number* – First checked if there exist a car with the defined registration number, then displays the respective parking slot number
- *Vehicle_registration_number_for_driver_of_age* - First checked if there exist a driver with the defined age, then displays the respective vehicle registration numbers separated by commas

