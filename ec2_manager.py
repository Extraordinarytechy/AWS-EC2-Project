import boto3
import sys
import logging

# Set up logging
logging.basicConfig(filename="ec2_manager.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    
#initialize EC2 client

ec2_client= boto3.client("ec2", region_name="Your-region")

# Replace with your instance id
INSTANCE_ID = "Your-instance-id"


def start_instance():
    """ Start the EC instance """
    try:
        response = ec2_client.start_instances(InstanceIds=[INSTANCE_ID])
        print(f"Starting instance {INSTANCE_ID}...")
        logging.info(f"Started instance {INSTANCE_ID}.")

    except Exception as e:
        print(f"Error starting instance: {e}")
        logging.error(f"Error starting instance: {e}")

def stop_instance():

    """Stop the EC2 instance"""
 
    try:
   
        response = ec2_client.stop_instances(InstanceIds=[INSTANCE_ID])
        print(f"stopping instance {INSTANCE_ID}...")
        logging.info(f"Stopped instance {INSTANCE_ID}.")

    except Exception as e:
        print(f"Error stopping instance: {e}")
        logging.error(f"Error stopping instance: {e}")

def check_status():

    """Check the EC2 instance status"""
   
    try:


        response = ec2_client.describe_instances(InstanceIds=[INSTANCE_ID])
        state = response["Reservations"][0]["Instances"][0]["State"]["Name"]
        print(f"Instance {INSTANCE_ID} is {state}.")
        logging.info(f"Instance {INSTANCE_ID} is {state}.")
   
    except Exception as e:

        print(f"Error checking status: {e}")
        logging.error(f"Error checking status: {e}")

if __name__ == "__main__":
    
    if len(sys.argv) !=2:
        
        print(f"Usage: python3 ec2_manager.py <start|stop|status>")
        
        sys.exit(1)

    action = sys.argv[1].lower()

    if action == "start":

        start_instance()

    elif action == "stop":
       
        stop_instance()

    elif action == "status":

        check_status()
   
    else:
     
        print("Invalid command. Use 'start','stop', or 'status'.")

