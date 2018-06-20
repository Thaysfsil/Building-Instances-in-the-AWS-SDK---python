# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:55:49 2015

@author: thayssilva
"""
import AWSClass
from senha import*
import boto3

from datetime import datetime
from boto3.session import Session
import subprocess as sp


def start():
    # start menu
    loop1=True
    while(loop1):
        tmp = sp.call('cls',shell=True)
        print("'")
        print("____________________________________")
        print('Input a option')
        print('Ex:. input 2 to register a user')
        print('[1] Login')
        print('[2] Register')
        print('[3] Admin Controls')
        print('[4] exit')
        option = str(input('Option: ')) # Get human input
        if option == '1':
            acesskey= login()
            acessUser(acesskey)
        elif option == '2':
            register()
        elif option == '3':
            acesskey= adminlogin()
            adminAcess(acesskey)
        elif option== '4':
            loop1=False
        else:
            print('Invalid Option!')
            



def adminAcess(acesskey):  
    aWs= AWS_ec2(acesskey[0],acesskey[1])
    loop2=True
    while (loop2):
        print("  ")
        print("____________________________________")
        print("_______Administrador________")
        print("Entre a opcao desejada:")
        print("___Instancia___")
        print("[1] Report Instances")
        print("[2] Create Instances")
        print("[3] Stop Instances")
        print("[4] Finish Instances")
        print("   ")
        print("____Security Group___")
        print("[5] Report Security Group")
        print("[6] Create Security Group")
        print("[7] Update Instances")
        print("[8] Remove Group")
        print("[9] Intances Cost")
        print("[10] exit")
        option= str(input('input option: ')) # Get human input
        
        #________________ist all instances        
        if option =='1':
            intances= aWs.list_instances()
            if intances:
                for x in intances:
                    print ("id: %s   Intances type: %s   Status: %s" %(x[0],x[1],x[2] ))
            else: 
                print("There are no instances to report")
                
                
        #___________________Create Intance
        elif option == '2':
            print ("Images available:"  )
            print("[1] Image 001: Amazon Linux AMI 2015.09.1 (HVM), SSD Volume Type")
            print("    Instances type: t2.micro " )
            print("[2] Image 002: Amazon Linux AMI 2015.09.1 (PV)")
            print("    Intsances type: t1.micro" )
            op= str(input("Image option:" ))
            if op =="1":
                image_id="ami-a0cdd0c1"
                instancetype="t2.micro"
            
            elif op=="2":
                image_id="ami-a3a0bdc2"
                instancetype="t1.micro"
                
            securityGroup=(str(input("Input security group ID:")))
            while not(securityGroup in str(aWs.list_group())):
                print ("You have not entered a valid security group")
                securityGroup = (str(input("Input security group ID: ")))
            responce=aWs.create_instances(image_id, securityGroup, instancetype)
            print(responce)
            
            
        #___________________Stop instance
        elif option == '3':
            instanceId=(str(input("Input instance ID:")))
            
            while not(instanceId in str(aWs.list_instances())):
                print ("You did not enter a valid instance id")
                intanceType = (str(input("Input instance ID: ")))
            responce = aWs.instance_stop(instanceId)
            print(responce)
            
            
        #___________________Finish instance
        elif option == '4':
            instanceId=(str(input("Input instance ID:")))
            
            while not(instanceId in str(aWs.list_instances())):
                print ("You did not enter a valid instance id")
                intanceType = (str(input("Input instance ID: ")))
            responce = aWs.instance_terminate(instanceId)
            print(responce)
            
            
            
        #___________________Report security group    
        elif option == '5':
            groupS= aWs.list_group()
            if groupS:
                for x in groupS:
                    print ("id: %s   Group Name: %s" %(x[0],x[1]))
            else: 
                print("There are no reporting instances")
                
                
        #___________________Create security group    
        elif option == '6':
            nome=(str(input("Input security group name:")))
            descri=(str(input("Input security group description:")))
            responce = aWs.create_group(nome,descri)
            print(responce)
            
        #___________________Update security group   
        elif option == '7':
            ids=(str(input("Input security group name:")))
            while not(ids in str(aWs.list_group())):
                print ("You have not entered a valid security group")
                ids = (str(input("Input a security group: ")))
            print ("Enter the desired protocol: tcp, udp, icmp. ")
            print("For other protocols see AWS-Protocol Number")
            protocol= ((str(input("Input protocol (tcp, udp,imp): "))))
            fport=(str(input("From port: ")))
            tport=(str(input("To port: ")))
            ip=(str(input("Destino IP (ex. 0.0.0.0/0 : ")))
            
            responce=aWs.update_group_inbound(ids,protocol,fport,tport,ip)
            print(responce)
            
        #___________________Remove security group           
        elif option == '8':
            ids=(str(input("Input security group ID:")))
            while not(ids in str(aWs.list_group())):
                print ("You have not entered a valid security group")
                ids = (str(input("Input security group: ")))
            
            nome=(str(input("Input security group name:")))
            while not(nome in str(aWs.list_group())):
                print ("You have not entered a valid security group")
                nome = (str(input("Input security group: ")))
                
            responce=aWs.delete_group(ids,nome)
            print(responce)
        
        #___________________Instance cost
        elif option =='9':
            intances= aWs.list_instances()
            now = datetime.now()
            value =0
            total=0
            if intances:
                for x in intances:
                    if (x[1] == 't2.micro' ):
                        day= ((x[3].date() - now.date()).days)*24
                        hour = c = (x[3].hour - now.hour) -1
                        value=int(day+hour)* (9.53)          
                        total=total+valor
                        print (" Intance: %s Custo: %.3f" %(x[0],value) )
                    else:
                        day= ((x[3].date() - now.date()).days)*24
                        hour=c = (x[3].hour - now.hour) -1
                        value=int(day+hour)* (14.64)
                        total=total+valor
                        print (" Intance: %s Custo: %.3f" %(x[0],value) )
            print(" Total: %.3f"%total)
        
        
        
            
            
            
        #___________________end
        elif option == '10':
            print("End")
            loop2=False
        else:
            print('This is not a valid option.')
            anykey = input('Press Enter to continue.')
        
        
    

  
def acessUser(acesskey):
    aWs= AWS_ec2(acesskey[0],acesskey[1])
    loop3 = True
    while (loop3):
        print("'")
        print("____________________________________")
        print("_______User Access________")
        print("___Instances___")
        print("[1] Report Intances")
        print("   ")
        print("____Security Group___")
        print("[2] Report Security Group") 
        print("[3] Instance cost)
        print("[4] exit")
        option= str(input('Opcao escolhida: ')) # Get human input
        
        #________________list all instances         
        if option =='1':
            intances= aWs.list_instances()
            if intances:
                for x in intances:
                    print ("id: %s   Instance type: %s Status: %s" %(x[0],x[1],x[2]))
            else: 
                print("There are no Instances to report")
        
        #___________________Reportar all security group   
        elif option == '2':
            groupS= aWs.list_group()
            if groupS:
                for x in groupS:
                    print ("id: %s   Group Name: %s" %(x[0],x[1]))
            else: 
                print("There are no instances to report)
        
        
        
        #___________________end
        elif option == '4':
            print("end)
            loop3=False
            
        #___________________Cost  
        elif option =='3':
            intances= aWs.list_instances()
            now = datetime.now()
            valor =0
            total=0
            if intances:
                for x in intances:
                    if (x[1] == 't2.micro' ):
                        day= ((x[3].date() - now.date()).days)*24
                        hour = c = (x[3].hour - now.hour) -1
                        valor=int(day+hour)* (9.53)          
                        total=total+valor
                        print (" Instance: %s Custo: %.3f" %(x[0],valor) )
                    else:
                        day= ((x[3].date() - now.date()).days)*24
                        hour=c = (x[3].hour - now.hour) -1
                        valor=int(day+hour)* (14.64)
                        total=total+valor
                        print (" Intsance: %s Custo: %.3f" %(x[0],valor) )
            print(" Total: %.3f"%total)
                    
            
            
            
     
        
        
        else:
            print('This is not a valid option.!')
            anykey = input('Press Enter to continue.')
        

start()
        

       
       
       
            

    
