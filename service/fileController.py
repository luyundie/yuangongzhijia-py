import paramiko
import os
def download(filename:str):
    try:
        t = paramiko.Transport(("121.36.90.163", 22))
        t.connect(username="root", password="HUNhan794")
        sftp = paramiko.SFTPClient.from_transport(t)
        # print("successful")
        localfile = os.path.join("sx","tempFile",filename)
        sftp.get( "/StaffHome/tempFile/"+filename,localfile)
    except Exception as e:
        print(e)
    t.close()
    return localfile

def upload(localfile:str,filename:str):
    try:
        t = paramiko.Transport(("121.36.90.163", 22))
        t.connect(username="root", password="HUNhan794")
        sftp = paramiko.SFTPClient.from_transport(t)
        # print(filename)
        sftp.put(localfile, "/StaffHome/tempFile/"+filename)
        os.remove(localfile)
    except Exception as e:
        print(e)
    t.close()
   
