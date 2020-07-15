# Price_tracker_website
### Requirements
* Users should be able to search for a product.
* If a user Clicks on a product then a page containing the description of the product and its features along with a list of prices from different websites should be displayed in ascending order.
* If the product user searched for isn't available, then the user should be able to add a product by URL or by sharing to our mobile application.
* Users should be able to add Multiple websites for the same product.
* There should be a validation process to validate URLs provided by the user and then the product will be added to our website's product database table. 
* Users will be notified when a price drop or desired price is reached for the products added to their wishlist.

### Ideas under review
* Can we use scrapy framework instead of beautifulsoup to introduce proxies and asymmetric request and throttling.
* Can we scrap multiple products and multiple websites based of model number of particular product (using direct search in website or by crawling from google advanced search).
