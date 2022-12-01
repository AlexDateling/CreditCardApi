# CreditCardApi
CreditCardvalidator using luhnn algo

Need postman to input credit card number

step 1
to build docker image use command
    - docker build -t creditcardapi . 
    you can verify that your image is added by using command
    -   docker images
[OPTIONAL]
If you would like to run it as a container use command
    - docker run -d -p 8001:8001 creditcardapi:latest
    you can verify that your container is running using command
    -   docker ps
    to stop this from running use command
    -   docker stop <containerId>

step 2
to set it up into a cluster use command
    - kubectl apply -f deployment.yml

    Note: can only apply deployment if image has been built and is locally registry please use step 1

step 3
to use it through postman through localhost use command 
    - kubectl port-forward credit-card-api 8001:8001