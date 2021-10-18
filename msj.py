from twilio.rest import Client 
 
account_sid = '#####################' 
auth_token = '#####################' 
client = Client(account_sid, auth_token) 

def mesaj():
    message = client.messages.create( 
                              from_='#',  
                              body='Luna',      
                              to='#' 
                          ) 
 
    print(message.sid)