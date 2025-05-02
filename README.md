# Project Milestone Timeline

- [x] **Project Proposal**
- [x] **Literature Review and Research**
- [x] **UML Diagram / Design Document**  
- [x] **Model Implementation**
- [x] **Simulation Runs / Data Collection**
- [x] **Sensitivity and Scenario Analysis**
- [x] **Validation and Verification**
- [x] **Final Project Report**

# Bank Queue Simulation

This project simulates a real-world banking environment using a multi-server queuing system. It demonstrates how varying the number of bank tellers affects customer wait times and overall service efficiency. The simulation models random customer arrivals and variable service times across different banking transactions.

## Features

- Single queue with multiple teller model (M/M/c queuing syste, )
- Randomized customer arrival times (between 1 and 3 minutes)
- Randomized service tasks (withdrawing money, depositing money, sending money, opening and account, closing an account, applying for a new credit line, getting bank documents for the last 6 months)
  
- Uses Python’s `threading` and `queue` modules
- Tracks and displays average wait times, maximum wait time, and average service time
- Console outputs statement with interaction details of the service task

##  How It Works

Customers arrive at random intervals and are placed in a shared queue. Each teller runs on a separate thread, continuously checking the queue for customers. Once a customer is dequeued, the teller performs a randomly assigned task, simulating a real banking operation (3–9 minutes in duration). The wait time for each customer is calculated and stored. The simulation ends when all customers are served, and the average wait time is reported. User can choose how many customers and tellers per simulation.

## Requirements

- Python 3.6 or higher


## How to Run

1. Clone the repository or copy the Python code into a local file, e.g., `bank_simulation.py`.
2. Open a terminal or command
3. Enter desired number of customers and bankers available



