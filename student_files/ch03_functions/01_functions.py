def display_results(customer, purchase_amount):
    print('Customer: {first} {last}, amount: ${p_amt:,.2f}'
          .format(first=customer['first'], last=customer['last'], p_amt=purchase_amount))


cust = {
    'first': 'James',
    'last': 'Smith'
}

display_results(cust, 1108.23)
