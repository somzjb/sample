**Get EC2 instance details**
This utility is used to get all the EC2 instaces that are running per region. Except the terminated ones.

getEC2.py
=========
prerequisities:
    1. You need boto3 installed
    2. You need to configure your AWS credentials in your local machine. The credentials should have appropriate "GET" permissions attached to it.
    
Usage:
    you can specify the --region_name or --instance_type flags optionally to get its sepcfic details. If you dont specify --region_name it will pick up the default region using the environment variable AWS_DEFAULT_REGION configured. If you dont specify --instance_type, it will show all the instances available on that particular region.
    example: 
        getEC2.py --instance_type t2.micro --region_name ec-central-1
        
 ec2-instance-create.yaml
 ========================
 You can use the ansible playbook to launch EC2 instance to run the getEC2.py utility. This playbook resolves all the dependencies required for the getEC2.py script to run. you can change the vars section in the playbook to customize the values that you desire to setup an ec2 machine.
 instructions:
 prerequisites:
        1. to run ansible playbook, you should have installed ansible on your local machine.
        2. you should have AWS credentials configured in your local machine with appropriate permissions to launch an EC2 instance.
        
 Usage:
    ansible-playbook ec2-instance-create.yaml
        
 
        
        
        
 
