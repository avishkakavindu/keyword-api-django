import nltk
from nltk import tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from serpapi import GoogleSearch

# nltk.download('stopwords') # Comment after running for the first time
# nltk.download('punkt') # Comment after running for the first time

from operator import itemgetter
import math
import re
from decouple import config

stop_words = set(stopwords.words('English'))

search_api_key = config('SEARCH_API_KEY')


def calculate_tf(words, total_words_count):
    """
    
    Calculates tf scores for words.
    :param words: List of words
    :param total_words_count: Number of total words
    :return: TF Scores for words as a dictionary
    """

    tf_score = {}

    for word in words:
        word = word.replace('.', '')
        # Take words that are not considered stop words
        if word not in stop_words:
            if word in tf_score:
                tf_score[word] += 1
            else:
                tf_score[word] = 1

    tf_score.update((x, y / int(total_words_count)) for x, y in tf_score.items())
    return tf_score


def check_in_sentence(word, sentences):
    """

    Checks whether a given word is present in a given sentence list.
    :param word: Specific word to be cheked
    :param sentences: List of sentences the word should be searched in
    :return: number of sentences the given word is in as an integer
    """

    final = [all([w in x for w in word]) for x in sentences]
    sentence_length = [sentences[i] for i in range(0, len(final)) if final[i]]
    return int(len(sentence_length))


def calculate_idf(words, sentences, total_sentences_count):
    """
    
    Calculates idf score for words.
    :param words: List of words
    :param sentences: List of sentences
    :param total_sentences_count: Total number of sentences
    :return: IDF Scores for words as a dictionary
    """

    idf_score = {}

    for word in words:
        word = word.replace('.', '')
        if word not in stop_words:
            if word in idf_score:
                idf_score[word] = check_in_sentence(word, sentences)
            else:
                idf_score[word] = 1

    idf_score.update((x, math.log(int(total_sentences_count) / y)) for x, y in idf_score.items())
    return idf_score


def extract_keywords(doc, num_keywords):
    """
    
    Extracts keywords from a set of sentences using TF-IDF Score.
    :param doc: Document/set of sentences
    :param num_keywords: Number of keywords to be returned
    :return: <num_keywords> number of extracted keywords
    """

    # Number of words in the doc - later will be used to calculate TF
    words = doc.strip().split()
    total_words_count = len(words)

    # Number of sentences in the doc - later will be used to calculate IDF
    sentences = tokenize.sent_tokenize(doc.strip())
    total_sentences_count = len(sentences)

    tf_scores = calculate_idf(words, sentences, total_sentences_count)

    idf_scores = calculate_idf(words, sentences, total_sentences_count)

    tf_idf_scores = {key: tf_scores[key] * idf_scores.get(key, 0) for key in tf_scores.keys()}

    return dict(sorted(tf_idf_scores.items(), key=itemgetter(1), reverse=True)[:num_keywords])


def get_link_sugessions(doc, num_keywords=5, num_links=5):
    """
    
    Returns referance link suggestions for a given document/set of sentences.
    :param doc: Document/set of sentences
    :param num_keywords: Number of keywords to be extracted from the document
    :param num_links: Number of link suggestions to be returned
    :return: <num_links> number of suggested links as a list
    """

    # Get keywords
    keywords = extract_keywords(doc, num_keywords=num_keywords)

    # Search String
    search_string = ' '.join(x for x in keywords.keys())
    # Remove punctuation marks
    search_string = re.sub(r'[^\w\s]', '', search_string)
    # Replacing spaces with '+' to create the search string for DuckDuckgo
    search_string = search_string.replace(' ', '+')

    search_params = {
        "engine": "duckduckgo",
        "q": search_string,
        "api_key": search_api_key
    }

    # Search results from DuckDuckGo search
    search = GoogleSearch(search_params)
    results = search.get_dict()

    links, count = [], 0

    for result in results['organic_results']:
        if count >= num_links:
            break
        links.append(result['link'])
        count += 1

    return links
