# Address Book Application
This is a simple project for looking up the address-book and giving the result back to the user, whether the contact is present or not. Having two API's written with Python and Flask, one API to load the address book and the second API to search for a contact using the First Name.

The project also contains script to install jenkins as a container so you can run this as a pipeline job in Jenkins [jenkins_install.sh]

## Pre-requisite to run this: 
  1. A system to build and run docker images with docker.io installed
  2. Just the basics of python or not
  3. A web browser or Postman to call the API's

## Build and Run commands:
  1. You can build the image using:
     ```
     docker build -t <image-name> .
     docker build -t addressbook .
     ```
  
  2. Running the image:
    In the Dockerfile exposing the 5254 port so you can run the image(without attaching volumen) like:
     ```
     docker run -p 5254:5254 -d --name=address-app addressbook
     
    
     Attaching a filesystem as volume
     docker run -p 5254:5254 --volume=<localfile>:/app -d --name=<container-name> <image-name>
     docker run -p 5254:5254 --volume=/opt/address-book:/app -d --name=nitishaddress addressbook
     ```
## Work with the application:
  Once you have application running as a container, the application will be running as:
    http://<IP-address>:5254/load_data
  IP will be your machine IP where docker is running is taken care by socket.gethostname()
  You can load the data by just invoking, this will also display the data that you would have invoked:
    http://<IP-address>:5254/load_data
  And you can Search the address-book invoking this api:
  
    ```
    http://<IP>:5254/query?key=first_name&value=dave
    or 
    http://9.193.198.157:5254/query?key=first_name&value=Dave
    ```
  Depending on the key you are searching, you will get appropriate feedback. Please try it out the application.  
 
  

