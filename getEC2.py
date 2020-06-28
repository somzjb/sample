'''#############get the ec2 instances##########
author: Soma
email: somasekarjb@gmail.com'''
import argparse
import boto3
import sys
import os
all_instances = []
#get the ec2instance and its types except terminated ones
def getEC2Instances(**kwargs):
    region_name=kwargs.get('region_name')
    instance_type = kwargs.get('instance_type')
    client = boto3.client('ec2', region_name= region_name)

    if bool(instance_type):
        instanceResult = client.describe_instances(Filters = [ { 'Name': 'instance-type','Values': [ instance_type]}])
    else:
         instanceResult = client.describe_instances()

    instances = instanceResult['Reservations'][0]['Instances']

    for inx in instances:
        all_instances.append(inx['InstanceId'])
        print(inx['InstanceId']+','+inx['InstanceType'])

#get the instance type from the user
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--region_name')
    parser.add_argument('--instance_type')
    args = parser.parse_args()
    getEC2Instances(region_name=args.region_name,instance_type=args.instance_type)





#print(all_instances)





