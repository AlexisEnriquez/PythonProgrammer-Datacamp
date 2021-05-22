# Course 14
# Software Engineering for Data Scientists in Python

# Chapter 1
# Software Engineering & Data Science

''''
Complete the import statement to load the numpy package.
Use numpy's array class to define arr.
Use arr's sort method to sort the numpy array.
'''
# import the numpy package
import numpy as np

# create an array class object
arr = np.array([8, 6, 7, 5, 3, 0, 9])

# use the sort method
arr.sort()

# print the sorted array
print(arr)

#View the documentation of the Counter.most_common method using the help() function. Note, you need to run the import statement before completing this step.

# Load the Counter function into our environment
from collections import Counter

# View the documentation for Counter.most_common
help(Counter.most_common)

#Correctly call Counter.most_common() by reading its documentation.
#Print the results stored in top_5_words.

# Load the Counter function into our environment
from collections import Counter

# View the documentation for Counter.most_common
help(Counter.most_common)

# Use Counter to find the top 5 most common words
top_5_words = Counter(words).most_common(5)

# Display the top 5 most common words
print(top_5_words)

''''
Import the pycodestyle package.
Create an instance of StyleGuide named style_checker.
There are two files that we'll be checking; they're named 'nay_pep8.py' and 'yay_pep8.py'. Pass a list containing these file names to our style_checker's check_files method.
print() the results of our style check to the console. Make sure to read the output!
'''
# Import needed package
import pycodestyle
# Create a StyleGuide instance
style_checker = pycodestyle.StyleGuide()

# Run PEP 8 check on multiple files
result = style_checker.check_files(['nay_pep8.py', 'yay_pep8.py'])

# Print result of PEP 8 style check
print(result.messages)

#Leverage the output of pycodestyle to edit the code to be compliant with PEP 8.
# Assign data to x
x=[8, 3, 4]

# Print the data
print(x)

#Leverage the output of pycodestyle to edit the code's comments to be compliant with PEP 8.
def print_phrase(phrase, polite=True, shout=False):
    if polite:
        # It's generally polite to say please
        phrase = 'Please ' + phrase

    if shout:
        # All caps looks like a written shout
        phrase = phrase.upper() + '!!'

    print(phrase)


# Politely ask for help
print_phrase('help me', polite=True)

# Shout about a discovery
print_phrase('eureka', shout=True)

# Chapter 2
# Writing a Python Module

#The possible package names to import are the following: text_analyzer, textAnalyzer, TextAnalyzer, & __text_analyzer__.
#import the package from the list above that follows the PEP 8 naming conventions.

# Import the package with a name that follows PEP 8
import text_analyzer

#Use the information from the context to identify the packages in the directory that follow the minimal structure.
#import the two packages that follow the minimal package requirements.
#Use help() to print information about each imported package.

# Import local packages
import package
import py_package

# View the help for each package
help(package)
help(py_package)

#Define top_items using plot_counter's inputs.
# Import needed functionality
from collections import Counter

def plot_counter(counter, n_most_common=5):
  # Subset the n_most_common items from the input counter
  top_items = counter.most_common(n_most_common)
  # Plot `top_items`
  plot_counter_most_common(top_items)

#Return the correct output from sum_counters
# Import needed functionality
from collections import Counter

def sum_counters(counters):
  # Sum the inputted counters
  return sum(counters, Counter())


#import your text_analyzer at the top of the script.
#Use the sum_counters() function from text_analyzer to aggregate all the Counters in word_counts.
#Use the plot_counter() function from text_analyzer to visualize the tweet's most used words while tweeting.
# Import local package
import text_analyzer

# Sum word_counts using sum_counters from text_analyzer
word_count_totals = text_analyzer.sum_counters(word_counts)

# Plot word_count_totals using plot_counter from text_analyzer
text_analyzer.plot_counter(word_count_totals)

''''
Write the requirement for matplotlib with at least version 3.0.0 or above.
Write the requirement for numpy version 1.15.4 exactly.
Write the requirement for pandas with at most version 0.22.0.
Write a non-version specific requirement for pycodestyle
'''

requirements = """
matplotlib>=3.0.0
numpy==1.15.4
pandas<=0.22.0
pycodestyle
"""

''''
import the needed function, setup, from the setuptools package.
Complete the name & packages arguments; keep in mind your package is located in a directory named text_analyzer.
List yourself as the author.
'''
# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text anaylsis.',
      author='Mikiko',
      packages=['text_analyzer'])

''''
import the needed function, setup, from the setuptools package.
List yourself as the author.
Specify your install_requires to require matplotlib version 3.0.0 or above.
'''
# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text anaylsis.',
      author='Mikiko',
      packages=['text_analyzer'],
      install_requires=['matplotlib>=3.0.0'])

# Chapter 3
# Utilizing Classes

''''
You are working in document.py.
Finish the def statement that will create a new Document instance when a user calls Document().
Use your knowledge of PEP 8 conventions to complete the definition of the newly named class method.
'''
# Define Document class
class Document:
    """A class for text analysis
    
    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed; set by `text` parameter
    """
    # Method to create a new instance of MyClass
    def __init__(self, text):
        # Store text parameter to the text attribute
        self.text = text

#Import your text_analyzer package.
#Create an instance of Document with the datacamp_tweet variable that's been loaded into your session.
#Print the contents of the text attribute of your newly created Document instance

# Import custom text_analyzer package
import text_analyzer

# Create an instance of Document with datacamp_tweet
my_document = text_analyzer.Document(text=datacamp_tweet)

# Print the text attribute of the Document instance
print(my_document.text)

''''
Counter from collections has been loaded into your environment, as well as the function tokenize().
Add a method named count_words as a non-public method.
Give your non-public method the functionality to count the contents tokens attribute using Counter().
Utilize your new function in the __init__ method.
'''
class Document:
  def __init__(self, text):
    self.text = text
    # Tokenize the document with non-public tokenize method
    self.tokens = self._tokenize()
    # Perform word count with non-public count_words method
    self.word_counts = self._count_words()

  def _tokenize(self):
    return tokenize(self.text)
	
  # non-public method to tally document's word counts with Counter
  def _count_words(self):
    return Counter(self.tokens)

''''
Create a new Document instance from the datacamp_tweets data set loaded into your environment. The datacamp_tweets object is a single string containing hundreds of tweets written by DataCamp & DataCamp users.
Print the first 5 tokens from datacamp_doc.
Print the top 5 most common words that were calculated by the non-public _count_words() method automatically in the Document.__init__ method.
'''
# create a new document instance from datacamp_tweets
datacamp_doc = Document(datacamp_tweets)

# print the first 5 tokens from datacamp_doc
print(datacamp_doc.tokens[:5])

# print the top 5 most used words in datacamp_doc
print(datacamp_doc._count_words().most_common(5))

''''
Document has been preloaded in the session.
Complete the class statement to create a SocialMedia class that inherits from Document.
Define SocialMedia's __init__() method that initializes a Document.
'''
# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
''''
The function filter_word_counts() has been loaded in your session. Use help() to see its proper usage.
Finish the _count_hashtags method using filter_word_counts() so that only words_counts starting with # remain.
'''
# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        
    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts,'#')

''''
Fill in the first line ofSocialMedia's __init__ method using the parent class to properly utilize inheritance.
Properly call the _count_mentions method in __init__ to add a new feature to SocialMedia.
'''
# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self,text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()
        
    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts, first_char='#')      
    
    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return filter_word_counts(self.word_counts, first_char='@')

''''
import your text_analyzer custom package.
Define dc_tweets as an instance of SocialMedia with the preloaded datacamp_tweets object as the text.
print the 5 most_common mentioned users in the data using the appropriate dc_tweets attribute.
Use text_analyzer's plot_counter() method to plot the most used hashtags in the data using the appropriate dc_tweets attribute.
'''
# Import custom text_analyzer package
import text_analyzer

# Create a SocialMedia instance with datacamp_tweets
dc_tweets = text_analyzer.SocialMedia(text=datacamp_tweets)

# Print the top five most most mentioned users
print(dc_tweets.mention_counts.most_common(5))

# Plot the most used hashtags
text_analyzer.plot_counter(dc_tweets.hashtag_counts)

# Import the text_analyzer package.
# Define my_doc as an instance of Document with the text stored in datacamp_tweets. datacamp_tweets has been pre-loaded in your environment.

# Import needed package
import text_analyzer

# Create instance of document
my_doc = text_analyzer.Document(datacamp_tweets)

# Run help() on the plot method you discovered with dir() to see how to properly use the functionality.
# Plot my_doc's word counts using the new plot method.

# Import needed package
import text_analyzer

# Create instance of document
my_doc = text_analyzer.Document(datacamp_tweets)

# Run help on my_doc's plot method
help(my_doc.plot_counts)

# Plot the word_counts of my_doc
my_doc.plot_counts()

''''
Complete the class statement so that Tweets inherits from SocialMedia. SocialMedia has already been loaded in your environment.
Use super() to call the __init__ method of the parent class.
Define retweet_text. Use help() to complete the call to filter_lines with the correct parameter name. filter_lines has already been loaded in your environment.
return retweet_text from _process_retweets as an instance of SocialMedia.
'''
# Define a Tweet class that inherits from SocialMedia
class Tweets(SocialMedia):
    def __init__(self, text):
        # Call parent's __init__ with super()
        super().__init__(text)
        # Define retweets attribute with non-public method
        self.retweets = self._process_retweets()

    def _process_retweets(self):
        # Filter tweet text to only include retweets
        retweet_text = filter_lines(self.text, first_chars='RT')
        # Return retweet_text as a SocialMedia object
        return SocialMedia(retweet_text)

# Import your text_analyzer package.
# Define my_tweets as an instance of Tweets using the datacamp_tweets data that has been pre-loaded into your environment.

# Import needed package
import text_analyzer

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets)

# Use the plot_counts() method to plot the top 'hashtag_counts'.
# Make sure to check the documentation for my_tweets.plot_counts.
# Import needed package
import text_analyzer

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets)

# Plot the most used hashtags in the tweets
my_tweets.plot_counts('hashtag_counts')

#Use the plot_counts() method of the retweets attribute to plot the most used hashtags in the retweets subset of the data.
# Import needed package
import text_analyzer

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets)

# Plot the most used hashtags in the retweets
my_tweets.retweets.plot_counts('hashtag_counts')

# Chapter 4
# Maintainability

# Print the text variable that has been pre-loaded into your environment.
# Print the result of calling the function with more useful commenting on text.
import re

def extract_0(text):
    # match and extract dollar amounts from the text
    return re.findall(r'\$\d+\.\d\d', text)

def extract_1(text):
    # return all matches to regex pattern
    return re.findall(r'\$\d+\.\d\d', text)

# Print the text
print(text)

# Print the results of the function with better commenting
print(extract_0(text))

#Run help() on each of the 4 functions to view their docstrings.

# Run the help on all 4 functions
help(goldilocks)
help(rapunzel)
help(mary)
help(sleeping_beauty)

# Define result using the function that has the most complete docstring; only 1 of the 4 contains all the sections we covered. Call the function without any parameters.
# Print the result of the most well documented function.

# Run the help on all 4 functions
help(goldilocks)
help(rapunzel)
help(mary)
help(sleeping_beauty)

# Execute the function with most complete docstring
result = rapunzel()

# Print the result
print(result)

''''
Complete the portions of the docstring that document the parameters.
Complete the portion of the docstring describing the return value.
Complete the example function usage in the docstring.
'''
# Complete the function's docstring
def tokenize(text, regex=r'[a-zA-z]+'):
  """Split text into tokens using a regular expression

  :param text: text to be tokenized
  :param regex: regular expression used to match tokens using re.findall 
  :return: a list of resulting tokens

  >>> tokenize('the rain in spain')
  ['the', 'rain', 'in', 'spain']
  """
  return re.findall(regex, text, flags=re.IGNORECASE)

# Print the docstring
help(tokenize)

''''
The math module has been pre-loaded into your environment to be able to use its sqrt function.
Give function the best possible name from the following options: do_stuff, hypotenuse_length, square_root_of_leg_a_squared_plus_leg_b_squared, pythagorean_theorem.
Complete the docstring's example with the function's name.
Print the result of using the newly named function to find the length of the hypotenuse for a right triangle with legs of length 6 & 8.
'''
def hypotenuse_length(leg_a, leg_b):
    """Find the length of a right triangle's hypotenuse

    :param leg_a: length of one leg of triangle
    :param leg_b: length of other leg of triangle
    :return: length of hypotenuse
    
    >>> hypotenuse_length(3, 4)
    5
    """
    return math.sqrt(leg_a**2 + leg_b**2)


# Print the length of the hypotenuse with legs 6 & 8
print(hypotenuse_length(6,8))


''''
Choose the best variable name to hold the sample of pupil diameter measurements in millimeters from the following choices: d, diameter, pupil_diameter, or pupil_diameter_in_millimeters.
Take the mean of the measurements and assign it to a variable. Choose the best variable name to hold this mean from the following options: m, mean, mean_diameter, or mean_pupil_diameter_in_millimeters.
Print the resulting average pupil diameter.
'''
from statistics import mean

# Sample measurements of pupil diameter in mm
pupil_diameter = [3.3, 6.8, 7.0, 5.4, 2.7]

# Average pupil diameter from sample
mean_diameter = mean(pupil_diameter)

print(mean_diameter)

''''
Move the logic for calculating the perimeter into the polygon_perimeter function.
Complete the definition of the polygon_apothem function, by moving the logic seen in the context. The math module has already been imported for you.
Utilize the new unit functions to complete the definition of polygon_area.
Use the more unitized polygon_area to calculate the area of a regular hexagon with legs of size 10.
'''
def polygon_perimeter(n_sides, side_len):
    return n_sides * side_len

def polygon_apothem(n_sides, side_len):
    denominator = 2 * math.tan(math.pi / n_sides)
    return side_len / denominator

def polygon_area(n_sides, side_len):
    perimeter = polygon_perimeter(n_sides,side_len)
    apothem = polygon_apothem(n_sides, side_len)

    return perimeter * apothem / 2

# Print the area of a hexagon with legs of size 10
print(polygon_area(n_sides=6, side_len=10))

''''
Complete the input code of the example in the docstring for sum_counters.
Complete the docstring example by filling in the expected output.
Run the testmod function from doctest to test your function's example code.
'''
def sum_counters(counters):
    """Aggregate collections.Counter objects by summing counts

    :param counters: list/tuple of counters to sum
    :return: aggregated counters with counts summed

    >>> d1 = text_analyzer.Document('1 2 fizz 4 buzz fizz 7 8')
    >>> d2 = text_analyzer.Document('fizz buzz 11 fizz 13 14')
    >>> sum_counters([d1.word_counts, d2.word_counts])
    Counter({'fizz': 4, 'buzz': 2})
    """
    return sum(counters, Counter())

doctest.testmod()

''''
Import the SocialMedia class.
Complete the name of the test function so it is run by pytest.
Use the appropriate keyword to test that the hashtag_counts are as expected.
'''
from collections import Counter
from text_analyzer import SocialMedia

# Create an instance of SocialMedia for testing
test_post = 'learning #python & #rstats is awesome! thanks @datacamp!'
sm_post = SocialMedia(test_post)

# Test hashtag counts are created properly
def test_social_media_hashtags():
    expected_hashtag_counts = Counter({'#python': 1, '#rstats': 1})
    assert sm_post.hashtag_counts == expected_hashtag_counts

''''
Import the Document class from the text_analyzer package for use in the class definition.
Complete the line of the docstring dealing with the parameters of the __init__ method.
Complete the docstring by filling out the documentation for the attributes or 'instance variables' of the SocialMedia class.
'''
from text_analyzer import Document

class SocialMedia(Document):
    """Analyze text data from social media
    
    :param text: social media text to analyze

    :ivar hashtag_counts: Counter object containing counts of hashtags used in text
    :ivar mention_counts: Counter object containing counts of @mentions used in text
    """
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()

