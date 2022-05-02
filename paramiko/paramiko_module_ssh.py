import paramiko
import time
import os

password=os.environ.get('PASSWORD')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # By default, paramiko client rejects the unknown host or key.
# ssh.connect(hostname='<ip of remote server>',username='centos',key_filename='<location of key>') # For key_files
ssh.connect(hostname='<ip of remote server>',username='centos',password='<password>') 
stdin,stdout,stderr = ssh.exec_command("free -m")
time.sleep(5)
print(stdout.readlines())
ssh.close()