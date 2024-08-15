# AWS EC2 Automation with Python

## Project Overview

This project demonstrates how to automate the management of AWS EC2 instances using Python and the `boto3` library. The script performs the following tasks:

- Launches a new EC2 instance.
- Stops the instance after it has started.
- Starts the instance after it has been stopped.
- Terminates the instance, completing its lifecycle.
- Includes error handling to manage potential issues during these operations.

## Prerequisites

- AWS account with proper permissions to create and manage EC2 instances.
- Python 3 installed on your local machine or EC2 instance.
- `boto3` library installed. If not already installed, you can install it using:
  ```bash
  pip install boto3

How to Run the Script

-Activate Virtual Environment (if you have one):
--source myenv/bin/activate

-Run the Script:
--python aws_automation.py


The script will output the ID of the newly created instance and perform stop, start, and terminate operations sequentially.

Error Handling
The script includes basic error handling to catch issues such as attempting to stop an already terminated instance. Any errors encountered during the execution will be printed to the console.

Conclusion
This script is a simple but powerful demonstration of using Python to automate cloud operations on AWS. It serves as a foundation for more complex automation tasks in a DevOps environment.
