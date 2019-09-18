# rsagraphy

This is a encryption and decryption software developed using Python3 on Linux platform. This desktop application can encrypt and decrypt simple text files(e.g. .txt, .py) , Image files(8, 16, 24 bit depth jpg, jpeg, bmp, png etc), Audio files(8 and 16bit Mono and Stereo PCM files), Video files(.avi, .mp4). 
This application use RSA algo to perform encryption and decryption of files, though for image and audio files the algo is enhanced to make the encryption and decryption more efficient. 
Here the application respect the properties of the file than converting the file into bytestring and apply the algorithm. The examples are attached.  



To install the dependencies use: 

sudo yum/apt-get install python3  

sudo yum/apt-get install python3-pip 

pip3 install opencv-python 

pip3 install numpy  

pip3 install matplotlib 

pip3 install imageio 

pip3 install scipy  

pip3 install tqdm  

pip3 install pypng  

pip3 install wave 




Keep all the files in one dir. 
