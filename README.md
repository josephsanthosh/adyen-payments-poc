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
'''
{
	"status":422,
	"errorCode":"174",
	"message":"Unable to decrypt data",
	"errorType":"validation"
}
'''
