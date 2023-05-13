import pandas as pd
import sys

sys.path.append('Microsoft_Azure_Assignment')
from credential import client

client = client()

"""
Sentiment analysis
"""

for idx, chunk in enumerate(pd.read_csv('yelp_review-100.csv', chunksize=10)):

    document_list = [doc for doc in chunk['text'] if isinstance(doc, str)]

    response = client.analyze_sentiment(
        documents=document_list,
        language='en-US',
        show_opinion_mining=True
    )

    positive_reviews = [doc for doc in response if doc.sentiment == "positive"]
    mixed_reviews = [doc for doc in response if doc.sentiment == "mixed"]
    negative_reviews = [doc for doc in response if doc.sentiment == "negative"]

    # Result
    # Predicted sentiment for document

    for indx, doc in enumerate(response):
        print('--------------------------------------------------------------------------')
        if idx == 0:
            print('Review #{0}'.format(indx + 1))
        elif idx == 1:
            print('Review #{0}'.format(indx + 11))
        elif idx == 2:
            print('Review #{0}'.format(indx + 21))
        elif idx == 3:
            print('Review #{0}'.format(indx + 31))
        elif idx == 4:
            print('Review #{0}'.format(indx + 41))
        elif idx == 5:
            print('Review #{0}'.format(indx + 51))
        elif idx == 6:
            print('Review #{0}'.format(indx + 61))
        elif idx == 7:
            print('Review #{0}'.format(indx + 71))
        elif idx == 8:
            print('Review #{0}'.format(indx + 81))
        elif idx == 9:
            print('Review #{0}'.format(indx + 91))
        else:
            print('Review #{0}'.format(indx + 101))

        print('Sentiment Analysis Outcome: {0}'.format(doc.sentiment))

        # document level sentiment confidence scores between 0 and 1 for each sentiment label.
        print('Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f}'.format(
            doc.confidence_scores.positive,
            doc.confidence_scores.neutral,
            doc.confidence_scores.negative
        ))
        print('-' * 75)

        # to break down the analysis by each sentence, we can reference the sentences attribute
        sentences = doc.sentences
        for indx, sentence in enumerate(sentences):
            print('Sentence #{0}'.format(indx + 1))
            print('Sentence Text: {0}'.format(sentence.text))
            print('Sentence scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f}'.format(
                sentence.confidence_scores.positive,
                sentence.confidence_scores.neutral,
                sentence.confidence_scores.negative
            ))

            # opinion analysi
            for mined_opinion in sentence.mined_opinions:
                target = mined_opinion.target
                print("......'{}' target '{}'".format(target.sentiment, target.text))
                print("......Target score:\n......Positive={0:.2f}\n......Negative={1:.2f}\n".format(
                    target.confidence_scores.positive,
                    target.confidence_scores.negative,
                ))
                for assessment in mined_opinion.assessments:
                    print("......'{}' assessment '{}'".format(assessment.sentiment, assessment.text))
                    print("......Assessment score:\n......Positive={0:.2f}\n......Negative={1:.2f}\n".format(
                        assessment.confidence_scores.positive,
                        assessment.confidence_scores.negative,
                    ))
            print()
    print('--------------------------------------------------------------------------------')