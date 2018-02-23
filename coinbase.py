from coinbase.wallet.client import Client

client = Client('', '', api_version='2018-01-01')

currency_code = 'USD'  # can also use EUR, CAD, etc.

# Make the request
price = client.get_spot_price(currency=currency_code)

print 'Current bitcoin price in %s: %s' % (currency_code, price.amount)