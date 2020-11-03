# naive_bayesian_classification_for_sentiment_analysis
Implementation of a Naive Bayes Classifier that can categorize movie reviews as positive or negative based on the text in the review. 



The starter code in `code.py` contains the definition of a class for the Naive Bayes Classifier.
The `train` function of the classifier class a list of lines from the data set (format of each line is desribed below). 
The `classify` function takes another list of lines to be classified and returns a python list of strings indicating the predicted class (1 or 5).



Ways to improve the classifer are included:
* add-one smoothing
* removing capitalization
* removing punctuation
* removing stop words
* stemming
* TF-IDF
* bigrams


### The Naive Bayes Algorithm

The probability of a review being positive given a set of features $f$ can be calculated as:

$$P(positive \ | \ f) = P(positive) * \prod^n_{i=1} P(f_i \ | \ positive)$$

Since probabilities can become very small, the product of these numbers can result in underflow. To get around this, use *log-probabilities* (in which case products become sums).


## Data 


The file, `alldata.txt`, which contains about 13,000 reviews, each on its own line. 

Each line of data is of the form:

```
NUMBER OF STARS|ID|TEXT
```

- The number of stars is 1 or 5. 

- The text goes until a newline (`\n`). 

- The text won't contain a '|', so you can safely invoke `split('|')`.


The `f_score` function has code that shows one method of reading each line of the data.




## F Score

We provide a calculate of F1, an f-score that takes into account the precision and recall of the classifier for a given class. 

$f1_c = \frac{2 * p_c * r_c}{p_c + r_c}$

 All tests will check the f-score for both the positive and negative classes.
 

## Additional resources

http://facweb.cs.depaul.edu/mobasher/classes/csc575/papers/porter-algorithm.html

https://nlp.stanford.edu/IR-book/html/htmledition/dropping-common-terms-stop-words-1.html

https://nlp.stanford.edu/IR-book/html/htmledition/tf-idf-weighting-1.html

