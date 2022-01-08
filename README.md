# ECM2429-Jan-2022-ex2
ECM2429 residential exercise 2

## Getting Started
Install the requests module using the following command in cmd or terminal
`pip install requests`

If you get unknown command try
`python -m pip install requests`

You can obtain a subscription key by googling "Azure For Students"
Sign up to Azure using your exeter account filling out the required fields

Once signed in, search for "speech services" at the top and click on the result

Click create and then fill in the required details. You will need to create a resource group if you haven't already.
Make sure to use subscription "Azure for Students" and not "Education"
Make sure to set the region to UK South. If you are using another region you will need to set environment variable `AZURE_REGION`

Once created, go to the page "Keys and Endpoint" and grab a key

Then store the key in an environment variable.

On windows run the following in cmd or terminal
`set AZURE_API_SUBSCRIPTION_KEY=<your key>`

On other operating systems run in terminal:
`export AZURE_API_SUBSCRIPTION_KEY=<your key>`

Failing that, you can hardcode the key by replacing `os.getenv("AZURE_API_SUBSCRIPTION_KEY")` with your subscription key.
