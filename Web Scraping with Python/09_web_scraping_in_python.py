# Course 9
# Web Scraping in Python

# Chapter 1
# Introduction to HTML

#Fill in the blank within the string variable html so that the HTML code matches its tree representation (including the text within the two paragraph children).
html = '''
<html>
  <head>
    <title>Intro HTML</title>
  </head>
  <body>
    <p>Hello World!</p>
    <p>Enjoy DataCamp!</p>
  </body>
</html>
'''

#Fill in the blank in the HTML code string html to assign a class attribute to the second div element which has the value "you-are-classy".
# HTML code string
html = '''
<html>
  <body>
    <div class="class1" id="div1">
      <p class="class2">Visit DataCamp!</p>
    </div>
    <div class="you-are-classy">
      <p class="class2">Keep up the good work!</p>
    </div>
  </body>
</html>
'''
# Print out the class of the second div element
whats_my_class( html )

# Chapter 2
# XPaths and Selectors

#Using only single forward-slashes to move between generations, and brackets to select the correct element, assign a string to the variable xpath that directs to the paragraph element containing "Where am I?".
#Do not include any blank spaces in the string you assign to xpath.
# Fill in the blank
xpath = '/html/body/div[2]/p'

#Using double forward-slash notation, assign to the variable xpath a simple XPath string navigating to all paragraph p elements within any HTML code.
# Fill in the blank
xpath = '//span[@class="span-class"]'

#Assign to the variable xpath an XPath string which directs to all child elements of the body element. There is only one body element in this HTML document and it is a child of the root html element.
# Create an XPath string to direct to children of body element
xpath = '/html/*'

# Print out the number of elements selected
how_many_elements( xpath )

#Assign to the variable xpath an XPath string to direct to the paragraph element containing the phrase: "Choose DataCamp!".

# Create an XPath string to the desired paragraph element
xpath = '/html/body/div[1]/div/p'

# Print out the element text
print_element_text( xpath )

#Fill in the blanks in the XPath string to select the paragraph element containing the phrase: "Thanks for Watching!".
# Create an Xpath string to select desired p element
xpath = '//*[@id="div3"]/p'

# Print out selection text
print_element_text( xpath )

#Fill in the blanks in the xpath below to select the paragraph element containing the phrase: "Hello World!".
# Create an XPath string to select p element by class
xpath = '//p[@class="class-1 class-2"]'

# Print out select text
print_element_text( xpath )

#Fill in the blanks to complete the variable xpath below to select the href attribute value from the DataCamp hyperlink.
# Create an xpath to the href attribute
xpath = '//p[@id="p2"]/a/@href'

# Print out the selection(s); there should be only one
print_attribute( xpath )

#Fill in the blanks below to assign an XPath string to the variable xpath which directs to all href attribute values of the hyperlink a elements whose class attributes contain the string "package-snippet". Remember that we use the contains call within the XPath string to check if an attribute value contains a particular string.
# Create an xpath to the href attributes
xpath = '//a[contains(@class,"package-snippet")]/@href'

# Print out how many elements are selected
how_many_elements( xpath )
# Preview the selected elements
preview( xpath )

#Fill in the blank below to chain together two xpath calls which result in the same selection as
# Chain together xpath methods to select desired p element
sel.xpath( '//div' ).xpath( './span/p[3]' )

#Set up the Selector object sel with the html variable passed as the text argument.
#Assign to the variable divs a SelectorList of all div elements within the HTML document.

from scrapy import Selector

# Create a Selector selecting html as the HTML document
sel = Selector( text = html )

# Create a SelectorList of all div elements in the HTML document
divs = sel.xpath( '//div' )

#Fill in the two blanks below to assign to create the Selector object sel which uses the string html as the text it inputs.
# Import a scrapy Selector
from scrapy import Selector

# Import requests
import requests

# Create the string html containing the HTML source
html = requests.get( url ).content

# Create the Selector object sel from html
sel = Selector( text = html)

# Print out the number of elements in the HTML document
print( "There are 1020 elements in the HTML document.")
print( "You have found: ", len( sel.xpath('//*') ) )

# Chapter 1
# CSS Locators, Chaining, and Responses

#Assign to the variable css_locator a CSS Locator string which is equivalent to the XPath string given.

# Create the XPath string equivalent to the CSS Locator 
xpath = '/html/body/span[1]//a'

# Create the CSS Locator string equivalent to the XPath
css_locator = 'html > body > span:nth-of-type(1) a'

#Assign to the variable xpath a XPath string which is equivalent to the CSS Locator string given.
# Create the XPath string equivalent to the CSS Locator 
xpath = '//div[@id="uid"]/span//h4'

# Create the CSS Locator string equivalent to the XPath
css_locator = 'div#uid > span h4'

#Fill in the blank below to create the Selector object sel using the string html as the text input.
from scrapy import Selector

# Create a selector from the html (of a secret website)
sel = Selector( text=html )

#Assign the variable css_locator a CSS Locator string which directs to the hyperlink (a element) children of all div elements belonging to the class "course-block".
from scrapy import Selector

# Create a selector from the html (of a secret website)
sel = Selector( text = html )

# Fill in the blank
css_locator = 'div.course-block > a'

# Print the number of selected elements.
how_many_elements( css_locator )

#Assign to the variable css_locator a CSS Locator string which will select all children (regardless of tag-type) of the unique element in the HTML document that has its id attribute equal to uid.
# Create the CSS Locator to all children of the element whose id is uid
css_locator = "#uid > *"

#Set up the Selector object sel using the string html as the text input.
#Assign to the variable hrefs_from_xpath the href attribute values from the elements in course_as. Your solution should match hrefs_from_css!

from scrapy import Selector

# Create a selector object from a secret website
sel = Selector( text = html )

# Select all hyperlinks of div elements belonging to class "course-block"
course_as = sel.css( 'div.course-block > a' )

# Selecting all href attributes chaining with css
hrefs_from_css = course_as.css( '::attr(href)' )

# Selecting all href attributes chaining with xpath
hrefs_from_xpath = course_as.xpath( './@href' )

#Assign to the variable xpath an XPath string directing to the text within the paragraph p element with id equal to p3, which does not include the text of future generations of this p element.
#Assign to the variable css_locator a CSS Locator string directing to this same text.
# Create an XPath string to the desired text.
xpath = '//p[@id="p3"]/text()'

# Create a CSS Locator string to the desired text.
css_locator = 'p#p3::text'

# Print the text from our selections
print_results( xpath, css_locator )

# Create an XPath string to the desired text.
xpath = '//p[@id="p3"]//text()'

# Create a CSS Locator string to the desired text.
css_locator = 'p#p3 ::text'

# Print the text from our selections
print_results( xpath, css_locator )

#Assign to the variable this_url the URL used to load the response variable.
#Assign to the variable this_title the title of the website used to load the response variable. Since we only want the text from the single element we will select, we use the extract_first() method to extract the text.
#Regardless of whether you use xpath or css, make sure that you are selecting the text within the title element, and not just the title itself.

# Get the URL to the website loaded in response
this_url = response.url

# Get the title of the website loaded in response
this_title = response.xpath('/html/head/title/text()').extract_first()

# Print out our findings
print_url_title( this_url, this_title )

#Assign to the variable css_locator a CSS Locator string which directs to all hyperlink a elements belonging to the class course-block__link.
#Assign to the variable response_as the output of passing the css_locator variable to the css method in response.
#Assign to the variable sel_as the output of passing the css_locator variable to the css method in sel.
# Create a CSS Locator string to the desired hyperlink elements
css_locator = 'a.course-block__link'

# Select the hyperlink elements from response and sel
response_as = response.css( css_locator )
sel_as = sel.css( css_locator )

# Examine similarity
nr = len( response_as )
ns = len( sel_as )
for i in range( min(nr, ns, 2) ):
  print( "Element %d from response: %s" % (i+1, response_as[i]) )
  print( "Element %d from sel: %s" % (i+1, sel_as[i]) )
  print( "" )

#Assign to the variable divs a SelectorList which selects all div elements belonging to the class course-block.
#Assign to the variable h4_text the text from the only h4 element within the content selected in first_div. Since we only want the text from the single element we will select, we use the extract_first() method to extract the text.

# Select all desired div elements
divs = response.css( 'div.course-block' )

# Take the first div element
first_div = divs[0]

# Extract the text from the h4 element in first_div
h4_text = first_div.css('h4::text').extract_first()

# Print out the text
print( "The text from the h4 element is:", h4_text )

#Using response, assign to the variable crs_title_els a SelectorList of the selected course titles.
#Assign to the variable crs_titles a list created by extracting the course titles from crs_title_els.

# Create a SelectorList of the course titles
crs_title_els = response.css( 'h4::text' )

# Extract the course titles 
crs_titles = crs_title_els.extract()

# Print out the course titles 
for el in crs_titles:
  print( ">>", el )

#Fill in the blank below to chain on a call to xpath so that we can calculate the number of children of the mystery element; we assign this number to the variable how_many_kids.
#Remember, if you use xpath, this really is an instance of chaining, so don't forget to use a period (.) as glue.

# Calculate the number of children of the mystery element
how_many_kids = len( mystery.xpath( './*' ) )

# Print out the number
print( "The number of elements you selected was:", how_many_kids )

# Chapter 4
# Spiders

#Pass scrapy.Spider as an argument to the class YourSpider; this will make it so that YourSpider inherits the methods from scrapy.Spider.
# Import scrapy library
import scrapy

# Create the spider class
class YourSpider(scrapy.Spider):
  name = "your_spider"
  # start_requests method
  def start_requests(self):
    pass
  # parse method
  def parse(self, response):
    pass
  
# Inspect Your Class
inspect_class(YourSpider)

#Fill in the blank within the start_requests method to assign the variable urls a list with the two strings: "https://www.datacamp.com" and"https://scrapy.org".
# Import scrapy library
import scrapy

# Create the spider class
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    urls = ["https://www.datacamp.com","https://scrapy.org"]
    for url in urls:
      yield url
  # parse method
  def parse( self, response ):
    pass
  
# Inspect Your Class
inspect_class( YourSpider )

#Fill in the required scrapy object into the class YourSpider needed to create the scrapy spider.
#Pass the string argument "Hello World!" to fill in the blank in the start_requests method to use the print_msg method.
# Import scrapy library
import scrapy

# Create the spider class
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    self.print_msg( 'Hello World!' )
  # parse method
  def parse( self, response ):
    pass
  # print_msg method
  def print_msg( self, msg ):
    print( "Calling start_requests in YourSpider prints out:", msg )
  
# Inspect Your Class
inspect_class( YourSpider )

#Fill in the required scrapy object into the class YourSpider needed to create the scrapy spider.
#Fill in the blank in the yielded scrapy.Request call within the start_requests method so that the URL this spider would start scraping is "https://www.datacamp.com" and would use the parse method (within the YourSpider class) as the method to parse the website.
# Import scrapy library
import scrapy

# Create the spider class
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = "https://www.datacamp.com", callback = self.parse )
  # parse method
  def parse( self, response ):
    pass
  
# Inspect Your Class
inspect_class( YourSpider )

#Fill in the required arguments to the parse method so that it will work as required when called in the start_requests method.
#Within the parse method, create a variable author_names, which is a list of strings created by extracting the text from the paragraph elements belonging to the class course-block__author-name.
# Import the scrapy library
import scrapy

# Create the Spider class
class DCspider( scrapy.Spider ):
  name = 'dcspider'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = url_short, callback = self.parse )
  # parse method
  def parse( self, response ):
    # Create an extracted list of course author names
    author_names = response.css( 'p.course-block__author-name::text' ).extract()
    # Here we will just return the list of Authors
    return author_names
  
# Inspect the spider
inspect_spider( DCspider )

#Fill in the two blanks below (one in each of the parsing methods) with the appropriate entries so that the spider can move from the first parsing method to the second correctly.
# Import the scrapy library
import scrapy

# Create the Spider class
class DCdescr( scrapy.Spider ):
  name = 'dcdescr'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = url_short, callback = self.parse )
  
  # First parse method
  def parse( self, response ):
    links = response.css( 'div.course-block > a::attr(href)' ).extract()
    # Follow each of the extracted links
    for link in links:
      yield response.follow( url = link, callback = self.parse_descr )
      
  # Second parsing method
  def parse_descr( self, response ):
    # Extract course description
    course_descr = response.css( 'p.course__description::text' ).extract_first()
    # For now, just yield the course description
    yield course_descr


# Inspect the spider
inspect_spider( DCdescr )

#Fill in the one blank at the end of the parse_pages methods to assign the chapter titles to the dictionary whose key is the corresponding course title.
# Import scrapy
import scrapy

# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class DC_Chapter_Spider(scrapy.Spider):
  name = "dc_chapter_spider"
  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url = url_short,
                         callback = self.parse_front)
  # First parsing method
  def parse_front(self, response):
    course_blocks = response.css('div.course-block')
    course_links = course_blocks.xpath('./a/@href')
    links_to_follow = course_links.extract()
    for url in links_to_follow:
      yield response.follow(url = url,
                            callback = self.parse_pages)
  # Second parsing method
  def parse_pages(self, response):
    crs_title = response.xpath('//h1[contains(@class,"title")]/text()')
    crs_title_ext = crs_title.extract_first().strip()
    ch_titles = response.css('h4.chapter__title::text')
    ch_titles_ext = [t.strip() for t in ch_titles.extract()]
    dc_dict[ crs_title_ext ] = ch_titles_ext

# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(DC_Chapter_Spider)
process.start()

# Print a preview of courses
previewCourses(dc_dict)

#Fill in the one blank below in the parse_pages method with a CSS Locator string which directs to the text within the paragraph p element which belongs to the class course__description.
# Import scrapy
import scrapy

# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class DC_Description_Spider(scrapy.Spider):
  name = "dc_chapter_spider"
  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url = url_short,
                         callback = self.parse_front)
  # First parsing method
  def parse_front(self, response):
    course_blocks = response.css('div.course-block')
    course_links = course_blocks.xpath('./a/@href')
    links_to_follow = course_links.extract()
    for url in links_to_follow:
      yield response.follow(url = url,
                            callback = self.parse_pages)
  # Second parsing method
  def parse_pages(self, response):
    # Create a SelectorList of the course titles text
    crs_title = response.xpath('//h1[contains(@class,"title")]/text()')
    # Extract the text and strip it clean
    crs_title_ext = crs_title.extract_first().strip()
    # Create a SelectorList of course descriptions text
    crs_descr = response.css('p.course__description::text')
    # Extract the text and strip it clean
    crs_descr_ext = crs_descr.extract_first().strip()
    # Fill in the dictionary
    dc_dict[crs_title_ext] = crs_descr_ext

# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(DC_Description_Spider)
process.start()

# Print a preview of courses
previewCourses(dc_dict)

#Assign to the variable crs_titles the extracted list of course titles on the DataCamp course directory page. You should use the contains call within your XPath, and your XPath string should point to the text of the selected objects.
#Assign to the variable crs_descrs the extracted list of short course descriptions. You should use the contains call within your XPath. You should use the contains call within your XPath, and your XPath string should point to the text of the selected objects.
#(Since we want a list of extracted data, we will use the extract() call (rather than extract_first()). )
# parse method
def parse(self, response):
  # Extracted course titles
  crs_titles = response.xpath('//h4[contains(@class,"block__title")]/text()').extract()
  # Extracted course descriptions
  crs_descrs = response.xpath('//p[contains(@class,"block__description")]/text()').extract()
  # Fill in the dictionary
  for crs_title, crs_descr in zip(crs_titles, crs_descrs):
    dc_dict[crs_title] = crs_descr

#Fill in the four blanks below with the necessary entries to complete your spider.
# Import scrapy
import scrapy

# Import the CrawlerProcess
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class YourSpider(scrapy.Spider):
  name = 'yourspider'
  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url = url_short, callback = self.parse)
      
  def parse(self, response):
    # My version of the parser you wrote in the previous part
    crs_titles = response.xpath('//h4[contains(@class,"block__title")]/text()').extract()
    crs_descrs = response.xpath('//p[contains(@class,"block__description")]/text()').extract()
    for crs_title, crs_descr in zip(crs_titles, crs_descrs):
      dc_dict[crs_title] = crs_descr
    
# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(YourSpider)
process.start()

# Print a preview of courses
previewCourses(dc_dict)