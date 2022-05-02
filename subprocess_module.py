import subprocess

cmd="ls -l"
sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rt=sp.wait()
out,err=sp.communicate()
print(out)