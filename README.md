# ISE 435 Final Project

The goal of this project is to use Python to produce a Kaplan-Meier plot from an input .csv file.

The Kaplan Meier Estimator plotted in the output graph is the probability of survival (or non failure) of an element over time derived from a set of lifetime data. It is generally used in the real world to measure the time-to-failure of machine parts, or measure the fraction of patients living for a certain amount of time after treatment.

In order to achieve the goal I have provided a python implementation that reads data from a user provided .csv file and calculates its Kaplan Meier Estimates, adding it to a data frame in order to output a visual representation of the Kaplan-Meier Curve.

## Program Input Data

Given data as a .csv file with columns with headers `elementID` , `time` , `event_type` .

Example input CSV table:

|elementID  |time      |event_type|
| -         | -        | -        |
| 101       | 5        | 1        |
| 328       | 9        | 1        |
| 171       | 10       | 0        |
| 362       | 13       | 1        |
| 721       | 13       | 1        |
| 410       | 15       | 1        |
| $\vdots$  | $\vdots$ | $\vdots$|

The entries in column `time` give the time when an event occured. The entries in column `event_type` give the type of event that occured, where
* 1 represents an event in which the associated element failed at the associated time, and
* 0 represents an event in which the associated time is the last time at which any information about the service time of the element is known. (Censored data point)

In its current state the program reads the kaplan-meier_sample_data_set.csv file provided in the repository.

The program reads the file using the file name entered on line 26 of the KaplanMeier.py program. Modify this filename to read from other input files.

**Make sure other input files are in the same folder or you will need to declare the filepath!**

## Program Description & Libraries Used
The KaplanMeier.py python program uses the following libraries:

pandas to read a .csv file and modify data frames (tables)

numpy to perform mathematical operations on the data (sum)

seaborn to plot the resulting Kaplan Meier Estimate to a graph output

In order to output a plotted survival estimate line using the Kaplan Meier Estimate Formula.

The estimate is calculated using a for loop that iterates over the provided data and first calculates $n_{i}$ (the number of elements that have not failed or been censored up to time t), followed by $d_{i}$ (the number of events that have happened at time $t_{i}$) using the numpy libraries sum function, and lastly the Kaplan Meier Estimator: 
 
 $\hat{S}(t)$ where $t$ is time, and
$$ \hat{S}(t) = \prod_{i: \;t_{i} \leq t} \left( 1 - \frac{d_{i}}{n_{i}}\right)$$
where $t_{i}$ is a time when at least one event happened, $d_{i}$ is the number of events that happened at time $t_{i}$, and $n_{i}$ is the number of elements known to have survived (i.e., elements that have not failed or been censored) up to time $t_{i}$
This estimate is then added as a row in the data frame to be plotted.


## Program Execution
Open a command prompt terminal and use cd to change the directory to where you have cloned the repository (use ls to show potential directories to enter)

To Install Python refer to: https://www.python.org/downloads/

To Ensure Python is installed run `py --version`

To Install Pip run after ensuring python is installed: `python -m ensurepip --upgrade`

Start a virtual environment by entering: 
`.\env\Scripts\activate`

_Note: If this does not work due to microsoft execution policies try_

`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` 

Install libraries into environment in order to run:

`pip install pandas`

`pip install seaborn`

`pip install numpy`


Enter the following and press enter to execute the program:
    `python3 KaplanMeier.py`

## Results

This will display the graph, which until modifying the read in file, will match the kaplanMeierPlotSampleOutput.png file provided

![Sample Output](https://github.ncsu.edu/rcwarner/ise435project/blob/main/kaplanMeierPlotSampleOutput.PNG?raw=true)

## Author Note

If there are any issues with installing the libraries, running a virtual environment, changing the input file or executing the python program please contact rcwarner@ncsu.edu with your questions! 


