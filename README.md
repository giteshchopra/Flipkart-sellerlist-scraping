# Flipkart-sellerlist-scraping
I have written 2 scripts to fetch Seller information FROM Flipkart.

1) **Using Selenium and Beautiful Soup** : Since the data is loaded Dynamically on this page, we need to go to the main product's page, put in the Pin Code, click on View More sellers and then once the page is loaded, we will scrape the data using Beautiful Soup. For now, I'm showing just the top 2 sellers along with data for a particular seller named 'ADHYATM'. However, this can be extended to get data for all the sellers.

2) **Using Json**: We can directly make a Post request to the flipkart Api that sends a Json and populates the seller data on the page. We will have to send appropriate headers and payload so that flipkart returns a valid response. If User-Agent/X-User-Agent isn't specified properly, it will send 403 Forbidden message. Once we get the Json, we can parse it to display the seller list.
