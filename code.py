import math
import re

class Bayes_Classifier:
    def __init__(self):
        self.pos_dic = {}
        self.neg_dic = {}
        self.pos_words_sum = 0
        self.neg_words_sum = 0
        self.words_count = 0
        self.prob_p = 0.0
        self.prob_n = 0.0

    def pos_prop(self, word_list):
        result = 0.0
        for word in word_list:
            if word in self.pos_dic.keys():
                result = result + math.log(self.pos_dic[word] + 1)
        return result + math.log(self.prob_p) - len(word_list) * math.log(self.pos_words_sum + self.words_count)

    def neg_prop(self, word_list):
        result = 0.0
        for word in word_list:
            if word in self.neg_dic.keys():
                result = result + math.log(self.neg_dic[word] + 1)
        return result + math.log(self.prob_n) - len(word_list) * math.log(self.neg_words_sum + self.words_count)

    def train(self, lines):
        pos_count = 0
        neg_count = 0
        self.vocals = {}
        for line in lines:
            line_list = line.split('|')
            if line_list[0] == '5':
                pos_count += 1
            else:
                neg_count += 1
            word_list = SentenceParser(line_list[2]).parse()
            for word in word_list:
                self.vocals[word] = 0
                if line_list[0] == '5':
                    self.pos_words_sum += 1
                    if word in self.pos_dic.keys():
                        self.pos_dic[word] += 1
                    else:
                        self.pos_dic[word] = 1
                else:
                    self.neg_words_sum += 1
                    if word in self.neg_dic.keys():
                        self.neg_dic[word] += 1
                    else:
                        self.neg_dic[word] = 1
        self.words_count = len(self.vocals)
        self.prob_p = float(pos_count)/len(lines)
        self.prob_n = float(neg_count)/len(lines)

    def classify(self, lines):
        predictions = []
        for line in lines:
            line_list = line.split('|')
            word_list = SentenceParser(line_list[2]).parse()
            p1 = self.pos_prop(word_list)
            p2 = self.neg_prop(word_list)
            if p1 >= p2:
                predictions.append('5')
            else:
                predictions.append('1')
        return predictions

class SentenceParser:
    def __init__(self, sentence):
        self.sentence = sentence
        self.stop_words = ["", "I", "i", "me", "myself", "you", "youself",
        "he", "him", "his", "himself", "she", "her", "herself", "they", "them",
        "themselves", "this"," that", "those", "it", "its", "it's", "itself",
        "with", "am", "was", "are", "were", "is", "to", "a", "an", "the", "about",
        "after", "and", "or", "as", "at", "on", "in", "be", "been", "before", "being",
        "by", "do", "doing", "during", "each", "for", "from", "have", "had", "has",
        "having", "here", "there", "due", "because", "where", "when", "who", "which",
        "let", "make", "get", "still", "out", "my", "your", "that's"]
        self.word_list = None

    def parse(self):
        self.word_list = self.parse_punctuation()
        self.word_list = self.parse_stop_word(self.word_list)
        self.word_list = self.parse_stemming(self.word_list)
        return self.word_list

    def parse_punctuation(self):
        return re.split(r'[;,!\.\?\s]+\s*', self.sentence.lower()) #removing capitalization

    def parse_stop_word(self, word_list):
        result = []
        for word in word_list:
            if word not in self.stop_words:
                result.append(word)
        return result

    def parse_stemming(self, word_list):
        result = []
        for i in range(len(word_list)):
            word = word_list[i]
            if word.endswith("sses"):
                result.append(word[:-2])
            elif word.endswith("ing"):
                result.append(word[:-3])
            elif word.endswith("ies"):
                result.append(word[:-2])
            elif word.endswith("ss"):
                result.append(word[:-2])
            elif word.endswith("ment"):
                result.append(word[:-4])
            elif word.endswith("s"):
                result.append(word[:-1])
            else:
                result.append(word)
        return result
