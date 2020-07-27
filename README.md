# notifynow-api

This is a REST API which handles Notifications to WhatsApp when ever a certain Email notifications from Netflix and Amazon Prime video are received by the registered  email.

The design flow of the API i.e. details of Models and Routes 

https://coggle.it/diagram/Xq15iZ_ZnDahT6H9/t/whatsapp-notify


### Steps to achieve the whats app notify:

- Register the user with email and phonenumber(WhatsApp enabled): 

   /api/users/create/
- Create the Token for the given user to Achieve Token Based Authentication for rest of the APIs:

   /api/users/token/

- Consents of whether notification(i.e. like notify on whatsApp, chrome extension) is required or not is provided for the given user :

   /api/consents/
   
  and notification types(i.e. like Netflix/Prime Video) should be defined at :
  
   /api/notifications/
   
- Once the user set up is done , we need to setup the Gmail- emails auto forward to user **vayu@notifynow.in** using following email filters 

  please import the following filters 
  
    
  
  The email auto-forward email code can be received from follwoing end point, which captures all the mails received by the user
  
   /api/user_mails/

- Then user with given whatsapp number while registering should subscribe to the whatsApp notification sending "join knew-signal" message to our WhatsApp account :

> https://api.whatsapp.com/send?phone=+14155238886&text=join%20knew-signal




#### After all the setup ... if you receive any email notifications containing following subjects , 

        1. is now on Netflix
        
        2. recently added on Prime Video

#### then it will be auto forwaded to our endpoint '/api/notify' and which is responsible to notify you as following to your whats app

![WhatsApp Notification](https://i.imgur.com/dy9bVPF.png)

