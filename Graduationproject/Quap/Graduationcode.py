import re, math
from collections import Counter
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import functools
from itertools import chain
import nltk






#calculate similar by cosine funcation
def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator



WORD = re.compile(r'\w+')
def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


#Root of word & steeming of word
def process(Ques):
 tokens=word_tokenize(Ques)
 words=[w.lower() for w in tokens]
 porter=nltk.PorterStemmer()
 stemmed_tokens=[porter.stem(t) for t in words]
 stop_words=set(stopwords.words('english'))
 filtered_tokens=[w for w in stemmed_tokens if not w in stop_words ]
 return filtered_tokens



CS141=["Code Object Oriented Computer Programs",
     "Ability to document programs through comments.",
     "Work in a team to implement a computer program",
     "Be able to engineer a class to separate its interface from its implementation for maintainability, reusability.",
     "Apply the concepts of data encapsulation, inheritance, and polymorphism .",
     "Understand what operator overloading is and how it makes programs more readable and programming more convenient",
     "Use class templates and functions templates and bind them to the other OO concepts."
     ]

CS242=["Understanding of Abstraction and Encapsulation through Abstract Data Types(ADT)",
       "Analyse problem space especially for time and space complexities (i.e. Asymptotic analysis of worst and average complexity bounds)",
       "Understanding of basic and advanced data structures such as Linked Lists, Stacks,Queues, Trees, etc.",
       "Analysis, design, and implementation of proper data structures for certain problems",
       "Differentiating between various sorting and searching algorithms and being able to choose the most suitable one in a certain problem context."
      ]


CS140=[' Edit compile and execute computer programs.',
     'Trace computer programs.',
     'Debug computer programs.',
     'Write readable programs using coding conventions such as comments, indentation, and naming.',
     'Solve problems by using structured programming techniques: sequence, selection, and repetition.',
     'Solve problems by writing and using functions.',
     'Solve problems by using appropriate fundamental data types and data structures (arrays and pointers).'
     ]


#for Cl in CS141:
  #  Root_fun(Cl)

'''input_course=input("Select course name ")
if input_course=="CS141":

 for x in range(3):
  input_string = input("Enter Questions ")
  t1=process(input_string)
  Join_words1=(' '.join(t1))
  text1=str(Join_words1).strip('[]')
  vector1=text_to_vector(text1)
  for Cl in CS141:
    t2=process(Cl)
    Join_words2 = (' '.join(t2))
    text2 = str(Join_words2).strip('[]')
    vector2=text_to_vector(text2)
    #print(vector2)
    print('Cosine is between first questions and Clos141:',get_cosine(vector1,vector2))
elif input_course=="CS140":
    for x in range(3):
        input_string = input("Enter Questions ")
        t1 = process(input_string)
        Join_words1 = (' '.join(t1))
        text1 = str(Join_words1).strip('[]')
        vector1 = text_to_vector(text1)
        for Cl in CS140:
            t2 = process(Cl)
            Join_words2 = (' '.join(t2))
            text2 = str(Join_words2).strip('[]')
            vector2 = text_to_vector(text2)
            print(vector2)
            print('Cosine is between first questions and Clos140:', get_cosine(vector1, vector2))
elif input_course=="CS242":
    for x in range(3):
        input_string = input("Enter Questions ")
        t1 = process(input_string)
        Join_words1 = (' '.join(t1))
        text1 = str(Join_words1).strip('[]')
        vector1 = text_to_vector(text1)
        for Cl in CS242:
            t2 = process(Cl)
            Join_words2 = (' '.join(t2))
            text2 = str(Join_words2).strip('[]')
            vector2 = text_to_vector(text2)
            print(vector2)
            print('Cosine is between first questions and Clos242:', get_cosine(vector1, vector2))'''''


def Best_Match(L):
    temp = 0
    index = 0
    for i, v in enumerate(L):
        last_value = v[-1]
        if last_value > temp:
            temp = last_value
            index = i

    Result(L[index])


def Result(LastResult):
    print(LastResult)

def Synset_word(SteemQuesins):
    Sys = wordnet.synsets(SteemQuesins)
    return Sys

def Enter_Questions():
    stack=[]
    for x in range(3):
     Qu = input("Enter Your Qustions:")
     steem = process(Qu)
     for word in steem:
         stack.append(word)
     return stack


def Relate_fun(DicOfQu):
    stack=[]
    for key in DicOfQu.keys():
        stack.append(key)
    Join_Qu=' '.join(stack)
    Space_Qu=str(Join_Qu).strip('[]')
    vector1 = text_to_vector(Space_Qu)
    input_course = input("Select course name ")
    if input_course=="CS141":
        Cosine = []
        C = []
        for Cl in CS141:
            t2 = process(Cl)
            Join_words2 = (' '.join(t2))
            Space_Clo = str(Join_words2).strip('[]')
            vector2 = text_to_vector(Space_Clo)
            Cosine.append(get_cosine(vector1, vector2))
            # Cosine=get_cosine(vector1, vector2)
        for x in range(6):
         C.append([Space_Qu, CS140[x], Cosine[x]])
         Best_Match(C)

    elif input_course=="CS140":
        Cosine=[]
        C=[]
        for Cl in CS140:
            t2 = process(Cl)
            Join_words2 = (' '.join(t2))
            Space_Clo = str(Join_words2).strip('[]')
            vector2 = text_to_vector(Space_Clo)
            Cosine.append(get_cosine(vector1, vector2))
            #Cosine=get_cosine(vector1, vector2)
        for x in range(6):
         C.append([Space_Qu,CS140[x],Cosine[x]])
        Best_Match(C)

    elif input_course=="CS242":
        Cosine = []
        C = []
        for Cl in CS242:
            t2 = process(Cl)
            Join_words2 = (' '.join(t2))
            Space_Clo = str(Join_words2).strip('[]')
            vector2 = text_to_vector(Space_Clo)
            Cosine.append(get_cosine(vector1, vector2))
            # Cosine=get_cosine(vector1, vector2)
        for x in range(6):
          C.append([Space_Qu, CS140[x], Cosine[x]])
          Best_Match(C)

word_list= Enter_Questions()
word_dict={}
for word in word_list:
  meaning=Synset_word(word)
  word_dict[word]=meaning
Relate_fun(word_dict)






'''def Matrix_Fun():
    m=int(input("Enter row"))
    n=int(input("Enter colom"))
    Mat=[]
    Qu_steem=Enter_Questions()
    for x in range(len(Qu_steem)):
      s1 = Synset_word(Qu_steem[x])
    for i in range(0,n):
        Mat.append([])
    for i in range(0,m):
        for j in range(0,n):
           Mat[i].append(j)
           Mat[i][j]=0
    for i in range(0,m):
        for j in range(0,n):
                if j==0:
                    Mat[i][j]=Qu_steem[i]
                elif j==1:
                    Mat[i][j]=s1'''
                    #print(Mat)







