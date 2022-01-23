FeaturedProductsSection = '//*[@id="site-content"]//*[@class="products columns-5"]/'

WishListTable = '//*[tbody[@class="wishlist-items-wrapper"]]'

WishListTableBody = WishListTable + '/tbody/'

AddFourthItemToCart = WishListTableBody + 'tr[1]/td[@class="product-add-to-cart"]'
AddThirdItemToCart = WishListTableBody + 'tr[2]/td[@class="product-add-to-cart"]'
AddSecondItemToCart = WishListTableBody + 'tr[3]/td[@class="product-add-to-cart"]'
AddFirstItemToCart = WishListTableBody + 'tr[4]/td[@class="product-add-to-cart"]'


