# Address Book Application
This is a simple project for looking up the address-book and giving the result back to the user, whether the contact is present or not. Having two API's written with Python and Flask, one API to load the address book and the second API to search for a contact using the First Name.

## Pre-requisite to run this: 
  1. A system to build and run docker images with docker.io installed
  2. Just the basics of python or not
  3. A web browser or Postman to call the API's

## Build commands:
  1. You can build the image using:
     ```
     docker build -t <image-name> .
     docker build -t addressbook .
     ```
  
  2. Running the image:
    In the Dockerfile exposing the 5254 port so you can run the image(without attaching volumen) like:
    ```
    docker run -p 5254:5254 -d --name=address-app addressbook
    ```
   
   Or you can attach a filesystem as Volume
    
    ```
    docker run -p 5254:5254 --volume=<localfile>:/app -d --name=nitishaddress addressbook
    docker run -p 5254:5254 --volume=/opt/address-book:/app -d --name=nitishaddress addressbook
    ```
    
  

