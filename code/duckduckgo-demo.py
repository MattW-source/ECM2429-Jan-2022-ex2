import requests

"""
For more information on the DuckDuckGo Instant Answers API see
https://duckduckgo.com/api

For more information of the Python Requests library see
https://docs.python-requests.org/en/latest/
"""

uri = 'https://api.duckduckgo.com'
query = {'q': 'Exeter University', 'format': 'json', 'pretty': True}
r = requests.get(uri, params=query)
print(r.text)
