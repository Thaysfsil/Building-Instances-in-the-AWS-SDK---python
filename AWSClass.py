# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:55:49 2015

@author: thayssilva
"""

import boto3
from boto3.session import Session


class AWS_ec2:

    def __init__(self, aws_access_key_id,aws_secret_access_key):
        self.aws_access_key_id= aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        
        session = Session(aws_access_key_id=self.aws_access_key_id,
                  aws_secret_access_key=self.aws_secret_access_key,
                  region_name='us-west-2')
                  
        self.ec2 = session.resource('ec2','us-west-2')
        self.key_pair = self.ec2.KeyPair('Key_pair_demo')
        
    def create_instances(self, image_id, securityGroup, instancetype):
        response= self.ec2.create_instances(ImageId='ami-a0cdd0c1', MinCount=1, MaxCount=1,SecurityGroupIds=[
        'sg-2a89114e'], InstanceType='t2.micro')
        return response
    
    def list_instances(self):
        l_instance = []
        instances = self.ec2.instances.filter()
        for instance in instances:
            if instances:
                x= (instance.id, instance.instance_type, instance.state.get("Name"),instance.launch_time)
                l_instance.append(x)
        return l_instance
        
    def instance_stop(self, ids):
        responce=self.ec2.instances.filter(InstanceIds=[ids]).stop()
        return responce
        
    def instance_terminate(self, ids):
        responce= self.ec2.instances.filter(InstanceIds=[ids]).terminate()
        return responce
        
    def list_group(self):
        lGroup = []
        security_group = self.ec2.security_groups.all()
        for group in security_group:
            x= (group.id, group.group_name)
            lGroup.append(x)
        return lGroup
    
    def create_group(self,nome,descri="___"):  
        response = self.ec2.create_security_group( GroupName=nome, Description= descri, VpcId='vpc-bb6d24de')
        return response
        
    def delete_group(self,ids,nome):
        security_group = self.ec2.SecurityGroup(ids)
        response = security_group.delete(GroupName=nome)
        return response 
        
    def update_group_inbound(self,ids,protocol,fport,tport,ip):
        security_group = self.ec2.SecurityGroup(ids)
        response = security_group.authorize_ingress(IpProtocol=protocol,FromPort=int(fport),ToPort=int(tport),CidrIp=ip)
        return response

