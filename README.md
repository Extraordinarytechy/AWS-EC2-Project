# AWS-EC2-INSTANCE

# **AWS EC2 Instance Management**  

## **Overview**  
This project provides a simple Python-based interface for managing AWS EC2 instances. It allows users to **start, stop, and check the status** of their EC2 instances using **Boto3 (AWS SDK for Python)**.  

## **Features**  
✅ Start an EC2 instance  
✅ Stop an EC2 instance  
✅ Check the current status of an instance  
✅ Uses **Boto3** for AWS API interactions  

## **Setup Instructions**  

### **1 Prerequisites**  
Before running the script, ensure you have:  
- An **AWS account** with IAM permissions for EC2 management  
- **Python 3.x** installed on your system  
- **Boto3 library** installed (`pip install boto3`)  
- **AWS CLI** installed and configured (`aws configure`)  

### **2 Installation**  
1. Clone this repository:  
   ```bash
   git clone git@github.com:Extraordinarytechy/AWS-EC2-INSTANCE.git  
   cd AWS-EC2-INSTANCE  
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt  
   ```  

## **Usage**  

### **Start an EC2 Instance**  
```python
python ec2_manager.py start  
```  

### **Stop an EC2 Instance**  
```python
python ec2_manager.py stop  
```  

### **Check EC2 Instance Status**  
```python
python ec2_manager.py status  
```  

## **Configuration**  
- Replace `INSTANCE_ID = "your-instance-id"` in **ec2_manager.py** with your actual **EC2 instance ID**  
- Replace `region_name="your-region"` with your AWS region  

## **Example Output**  
```bash
Instance i-08b2c34c763ca44a3 is running.  
Starting instance i-08b2c34c763ca44a3...  
Stopping instance i-08b2c34c763ca44a3...  
```  

## **Project Structure**  
```
AWS-EC2-INSTANCE/  
│── ec2_manager.py  # Main script for EC2 management  
│── README.md       # Project documentation  
│── requirements.txt # Dependencies  
└── .gitignore      # Git ignored files  
```  

## **Contributing**  
Feel free to fork this repository** and submit pull requests for improvements.  

## License
This project is licensed under the MIT License.  

## **Connect with Me**  
📩 LinkedIn: [Your Profile Link]  
🚀 GitHub: [Extraordinarytechy](https://github.com/Extraordinarytechy)  

-
