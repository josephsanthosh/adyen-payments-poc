# adyen-payments-poc

## Technical requirements
* Python 3.8
* Python libraries:
    * flask
    * requests

## Assumptions
* For credit card payments, the following values have been hard coded in the code
    * expiryMonth is set to '03' replacing field encryptedExpiryMonth from front end
    * expiryYear is set to '2030' replacing field encryptedExpiryYear from front end
    * number is set to '371449635398431' replacing field encryptedCardNumber from front end
    * cvc is set to is set to '7373' replacing field encryptedSecurityCode from front end

I had to do this as sending the encrypted fields was getting an error response as below:
```json
{
	"status":422,
	"errorCode":"174",
	"message":"Unable to decrypt data",
	"errorType":"validation"
}
```
I did raise an Adyen support ticket(#1348839), but it took too long for them to respond. So i took it upon myself to atleast run a bare minimum.
* countryCode for all calls are 'NL', to keep it simple.
* As requested, I have not used any existing adyen libraries, but direct API calls. 
* I have used some adyen HTML templates(success, failure, layout, fetchPayments, css files) after discovering them on github, so as to reuse and reduce work on the front end. Only dropin file has been created from scratch.
