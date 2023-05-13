import pandas as pd
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt

'''
                ----------------- Rational for the approach -----------------
To compare the distribution of sentiment labels for high/low-performance restaurants, we can first define 
what is meant by high/low-performance restaurants. One possible approach is to use the average star rating 
of each restaurant as a proxy for its performance. For example, we can define high-performance restaurants 
as those with an average star rating of 4.5 or higher, and low-performance restaurants as those with an 
average star rating of less than 3.5. We can then compare the sentiment labels for the reviews of these 
two groups of restaurants.

Here's an approach to answer the question
'''


# Load the Yelp review dataset into a Pandas DataFrame.
yelp_review_1000 = pd.read_csv('yelp_review_1000.csv')

# Calculate the average star rating for each restaurant.
restaurant_ratings = yelp_review_1000.groupby('business_id')['stars'].mean()

# Divide the restaurants into two groups based on their average star rating.
high_performers = restaurant_ratings[restaurant_ratings >= 4.5].index
low_performers = restaurant_ratings[restaurant_ratings < 3.5].index

# Filter the reviews to only include those for high and low-performing restaurants.
high_performer_reviews = yelp_review_1000[yelp_review_1000['business_id'].isin(high_performers)]
low_performer_reviews = yelp_review_1000[yelp_review_1000['business_id'].isin(low_performers)]

# Calculate the sentiment labels for each review.
high_performer_reviews['sentiment'] = high_performer_reviews['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
low_performer_reviews['sentiment'] = low_performer_reviews['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
# low_performer_reviews.loc[:, 'sentiment'] = low_performer_reviews['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
# yelp_review_1000.loc[yelp_review_1000['business_id'].isin(low_performer_reviews), 'sentiment'] = yelp_review_1000.loc[yelp_review_1000['business_id'].isin(low_performer_reviews), 'text'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Visualize the sentiment label distribution for each group using a histogram or density plot.

# plt.hist(high_performer_reviews['sentiment'], alpha=0.5, label='High-performing restaurants')
# plt.hist(low_performer_reviews['sentiment'], alpha=0.5, label='Low-performing restaurants')
# plt.legend()
# plt.title('Sentiment Label Distribution by Restaurant Performance')
# plt.xlabel('Sentiment Label')
# plt.ylabel('Frequency')
# plt.show()



# born as sns

sns.set_style('whitegrid')

# High performer reviews
high_performer_reviews = yelp_review_1000[yelp_review_1000['stars'] >= 4]
high_performer_reviews['sentiment'] = high_performer_reviews['text'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Low performer reviews
low_performer_reviews = yelp_review_1000[yelp_review_1000['stars'] < 4].copy()
low_performer_reviews['sentiment'] = low_performer_reviews['text'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Sentiment polarity is a measure of the positivity or negativity of a text. It is usually measured on a
# scale ranging from -1 to +1, where -1 represents a completely negative sentiment, +1 represents a
# completely positive sentiment, and 0 represents a neutral sentiment.

# Distribution of sentiment labels for high performer reviews
plt.figure(figsize=(8, 6))
sns.histplot(data=high_performer_reviews, x='sentiment', hue='stars', multiple='stack', bins=50)
plt.title('Distribution of Sentiment Labels for High-Performance Restaurants')
plt.xlabel('Sentiment Polarity')
plt.ylabel('Frequency')
plt.legend(title='Stars', loc='upper left')
plt.show()
#  Conclusion: In this case, a sentiment polarity range of -0.2 - 1.0 for high-performance restaurants would indicate that the sentiment expressed in the reviews for those restaurants tends to be relatively positive, with scores falling somewhere between slightly positive (0.1) to very positive (0.7).


# Distribution of sentiment labels for low performer reviews
plt.figure(figsize=(8, 6))
sns.histplot(data=low_performer_reviews, x='sentiment', hue='stars', multiple='stack', bins=50)
plt.title('Distribution of Sentiment Labels for Low-Performance Restaurants')
plt.xlabel('Sentiment Polarity')
plt.ylabel('Frequency')
plt.legend(title='Stars', loc='upper left')
plt.show()
#  Conclusion: In this case, a sentiment polarity score of -1.0 to 0.3 for low-performance restaurants means that the sentiment expressed in the reviews for these restaurants is mostly negative, with some reviews having a slightly positive sentiment.
