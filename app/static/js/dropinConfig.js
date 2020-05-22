const paymentMethods = JSON.parse(JSON.parse(document.getElementById('payment-methods').innerHTML));
const originKey = JSON.parse(document.getElementById('origin-key').innerHTML);

const completePayment = (resultCode) => {
  if (resultCode === 'Authorised' || resultCode === 'Received') {
      window.location.href = "http://localhost:8080/success";

  } else if (resultCode === 'Pending') {
      window.location.href = "http://localhost:8080/pending";

  } else if (resultCode === 'Error') {
      window.location.href = "http://localhost:8080/error";

  } else {
      window.location.href = "http://localhost:8080/failed";
  }
};


const configuration = {
    paymentMethodsResponse: paymentMethods, // The `/paymentMethods` response from the server.
    originKey: originKey,
    locale: "en-US",
    environment: "test",
    paymentMethodsConfiguration: {
      card: { // Example optional configuration for cards
          hasHolderName: true,
          holderNameRequired: true,
          enableStoreDetails: true,
          billingAddressRequired: true,
      }
    },
    onSubmit: (state, dropin) => {
        // Your function calling your server to make the `/payments` request
        console.log("\nMake payment request triggered\n");
        fetch(`/makePayment`, {
            method: 'POST',
            headers: {
                'Accept': 'application/json ,text/plain, */*',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(state.data)
        }).then(response => response.json())
            .then(response => {
              console.log("\nMake payment response triggered\n");
              if (response.action) {
                console.log("\RESPONSE ACTION triggered\n");
                // Drop-in handles the action object from the /payments response
                if (response.resultCode === 'RedirectShopper') {
                  localStorage.setItem('redirectPaymentData', response.action.paymentData);
                }
                dropin.handleAction(response.action);
              } else {
                // Your function to show the final result to the shopper
                completePayment(response.resultCode);
              }
          })
          .catch(error => {
            throw Error(error);
          });
      },
    onAdditionalDetails: (state, dropin) => {
      // Your function calling your server to make a `/payments/details` request
      console.log("\nON-ADDITIONAL triggered\n");
        fetch(`/additionalDetails`, {
        method: 'POST',
        headers: {
            Accept: 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(state.data)
    }).then(response => response.json())
        .then(response => {
          if (response.action) {
            // Drop-in handles the action object from the /payments response
            dropin.handleAction(response.action);
          } else {
            // Your function to show the final result to the shopper
            completePayment(response.resultCode);
          }
        })
        .catch(error => {
          throw Error(error);
        });
    }
   };


const checkout = new AdyenCheckout(configuration);
const dropin = checkout.create('dropin').mount('#dropin-container');