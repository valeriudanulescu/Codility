from selenium import webdriver
import time
import Variables

driver = webdriver.Chrome('ChromeDriver.exe')
driver.maximize_window()
driver.get("https://testscriptdemo.com")
time.sleep(1)
print("testscriptdemo.com is Loaded\n")
time.sleep(1)

print("Will now click Home\n")
Home = driver.find_element_by_xpath('//*[@title="Home"]')
Home.click()
time.sleep(1)

# First Item
print("Will now add the First Item from Features Products section to the wish list\n")
FirstItemName = driver.find_element_by_xpath(Variables.FeaturedProductsSection + "/li[1]//h2").text
print("First Item to add to Wish List is: " + FirstItemName + "\n")

FirstItemAddToWishList = driver.find_element_by_xpath(Variables.FeaturedProductsSection + 'li[1]//*[@data-title = "Add to wishlist"]')
FirstItemAddToWishList.click()
print(FirstItemName + " Added to WishList\n")
time.sleep(1)

# Second Item
print("Will now add the Second Item from Features Products section to the wish list")
SecondItemName = driver.find_element_by_xpath(Variables.FeaturedProductsSection + "/li[2]//h2").text
print("Second Item to add to Wish List is: " + SecondItemName + "\n")

print("Will now add the Second Item from Features Products section to the wish list")
SecondItemAddToWishList = driver.find_element_by_xpath(Variables.FeaturedProductsSection + 'li[2]//*[@data-title = "Add to wishlist"]')
SecondItemAddToWishList.click()
print(SecondItemName + " Added to WishList\n")
time.sleep(1)

# Third Item
print("Will now add the Third Item from Features Products section to the wish list")
ThirdItemName = driver.find_element_by_xpath(Variables.FeaturedProductsSection + "/li[3]//h2").text
print("Third Item to add to Wish List is: " + ThirdItemName + "\n")

print("Will now add the Third Item from Features Products section to the wish list")
ThirdItemAddToWishList = driver.find_element_by_xpath(Variables.FeaturedProductsSection + 'li[3]//*[@data-title = "Add to wishlist"]')
ThirdItemAddToWishList.click()
print(ThirdItemName + " Added to WishList\n")
time.sleep(1)

# Fourth Item
print("Will now add the Fourth Item from Features Products section to the wish list")
FourthItemName = driver.find_element_by_xpath(Variables.FeaturedProductsSection + "/li[4]//h2").text
print("Third Item to add to Wish List is: " + FourthItemName + "\n")

print("Will now add the Fourth Item from Features Products section to the wish list")
FourthItemAddToWishList = driver.find_element_by_xpath(Variables.FeaturedProductsSection + 'li[4]//*[@data-title = "Add to wishlist"]')
FourthItemAddToWishList.click()
print(FourthItemName + " Added to WishList\n")
time.sleep(1)


print("Will now click on Wish List from the Page Header\n")
WishList = driver.find_element_by_xpath('//*[@class="container"]//*[@title = "Wishlist"][1]')
WishList.click()
print("Wish List Heart Symbol in Header clicked\n")

print("Will now check how many elements we added to the Wish List\n")
rows = driver.find_elements_by_xpath('//*[tbody[@class="wishlist-items-wrapper"]]/tbody/tr')
# len method is used to get the size of that list
print("Numbers of items in the Wish List is " + str(len(rows)) + "\n")

print("Searching for lowest price in the Wish List:\n")
FourthElementPriceInWishList = Variables.WishListTableBody + 'tr[1]/td[@class="product-price"]'
FourthPrice =  driver.find_element_by_xpath(FourthElementPriceInWishList).text
ThirdElementPriceInWishList = Variables.WishListTableBody + 'tr[2]/td[@class="product-price"]'
ThirdPrice = driver.find_element_by_xpath(ThirdElementPriceInWishList).text
SecondElementPriceInWishList = Variables.WishListTableBody + 'tr[3]/td[@class="product-price"]'
SecondPrice = driver.find_element_by_xpath(SecondElementPriceInWishList).text
FirstElementPriceInWishList = Variables.WishListTableBody + 'tr[4]/td[@class="product-price"]'
FirstPrice = driver.find_element_by_xpath(FirstElementPriceInWishList).text
min_price = min(FirstPrice,SecondPrice,ThirdPrice,FourthPrice)
print("Minimum price of items in Wish List is: " + min_price + "\n")

ListProductsInWishList = [FirstPrice, SecondPrice, ThirdPrice, FourthPrice]


# reached here, not figuring out the selectors for lowest prices. The issue is with the Deleted prices that are reported as prices for Items :(
def LowestPricedProduct():
    print("List of Prices in Wish List is: " + ListProductsInWishList)
    for i in ListProductsInWishList:
        if i  == min_price:
            print("This is the minimum price: " + i)
            CheapestItemAddToCart = driver.find_element_by_xpath(Variables.WishListTableBody + 'tr[' + i + ']/td[@class="product-add-to-cart"]')
            CheapestItemAddToCart.click()
            print("Cheapest Item Added to Cart\n")
            time.sleep(1)
            break

LowestPricedProduct(ListProductsInWishList)

print("We now click on Cart")
Cart = driver.find_element_by_xpath('//*[@class="container"]/div/div[3]//*[@data-tooltip="Cart"]')
Cart.click()


