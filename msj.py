from twilio.rest import Client 
 
account_sid = 'AC7fab25b030d116b710155ccf9a906e08' 
auth_token = 'dcdf363fe4f4fec1f75565db7daf7764' 
client = Client(account_sid, auth_token) 

def mesaj():
    message = client.messages.create( 
                              from_='#',  
                              body='Luna',      
                              to='#' 
                          ) 
 
    print(message.sid)