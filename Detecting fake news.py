{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8c8106bf",
   "metadata": {},
   "source": [
    "### Steps\n",
    "#### 1- Import necessary libraries\n",
    "#### 2- Read and explore the dataset\n",
    "#### 3- Build a model using PassiveAggressiveClassifier\n",
    "#### 4- Evaluate the model's accuracy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc852b8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: numpy in c:\\users\\sss-a\\anaconda3\\lib\\site-packages (1.20.1)\n",
      "Requirement already satisfied: pandas in c:\\users\\sss-a\\anaconda3\\lib\\site-packages (1.2.4)\n",
      "Requirement already satisfied: sklearn in c:\\users\\sss-a\\anaconda3\\lib\\site-packages (0.0)\n",
      "Requirement already satisfied: python-dateutil>=2.7.3 in c:\\users\\sss-a\\anaconda3\\lib\\site-packages (from pandas) (2.8.1)\n",
      "Requirement already satisfied: pytz>=2017.3 in c:\\users\\sss-a\\anaconda3\\lib\\site-packages (from pandas) (2021.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\sss-a\\anaconda3\\lib\\site-packages (from python-dateutil>=2.7.3->pandas) (1.15.0)\n",
      "Requirement already satisfied: scikit-learn in c:\\users\\sss-a\\anaconda3\\lib\\site-packages (from sklearn) (0.24.1)\n",
      "Requirement already satisfied: threadpoolctl>=2.0.0 in c:\\users\\sss-a\\anaconda3\\lib\\site-packages (from scikit-learn->sklearn) (2.1.0)\n",
      "Requirement already satisfied: scipy>=0.19.1 in c:\\users\\sss-a\\anaconda3\\lib\\site-packages (from scikit-learn->sklearn) (1.6.2)\n",
      "Requirement already satisfied: joblib>=0.11 in c:\\users\\sss-a\\anaconda3\\lib\\site-packages (from scikit-learn->sklearn) (1.0.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "082ddbc4",
   "metadata": {},
   "source": [
    "#### 1- Import necessary libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0807b7e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import PassiveAggressiveClassifier\n",
    "from sklearn.metrics import accuracy_score, confusion_matrix, classification_report\n",
    "import itertools\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4786a2af",
   "metadata": {},
   "source": [
    "#### 2- Read and explore the dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7cf9c4e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>title</th>\n",
       "      <th>text</th>\n",
       "      <th>label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>8476</td>\n",
       "      <td>You Can Smell Hillary’s Fear</td>\n",
       "      <td>Daniel Greenfield, a Shillman Journalism Fello...</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10294</td>\n",
       "      <td>Watch The Exact Moment Paul Ryan Committed Pol...</td>\n",
       "      <td>Google Pinterest Digg Linkedin Reddit Stumbleu...</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3608</td>\n",
       "      <td>Kerry to go to Paris in gesture of sympathy</td>\n",
       "      <td>U.S. Secretary of State John F. Kerry said Mon...</td>\n",
       "      <td>REAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>10142</td>\n",
       "      <td>Bernie supporters on Twitter erupt in anger ag...</td>\n",
       "      <td>— Kaydee King (@KaydeeKing) November 9, 2016 T...</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>875</td>\n",
       "      <td>The Battle of New York: Why This Primary Matters</td>\n",
       "      <td>It's primary day in New York and front-runners...</td>\n",
       "      <td>REAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6903</td>\n",
       "      <td>Tehran, USA</td>\n",
       "      <td>\\nI’m not an immigrant, but my grandparents ...</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>7341</td>\n",
       "      <td>Girl Horrified At What She Watches Boyfriend D...</td>\n",
       "      <td>Share This Baylee Luciani (left), Screenshot o...</td>\n",
       "      <td>FAKE</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>95</td>\n",
       "      <td>‘Britain’s Schindler’ Dies at 106</td>\n",
       "      <td>A Czech stockbroker who saved more than 650 Je...</td>\n",
       "      <td>REAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>4869</td>\n",
       "      <td>Fact check: Trump and Clinton at the 'commande...</td>\n",
       "      <td>Hillary Clinton and Donald Trump made some ina...</td>\n",
       "      <td>REAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2909</td>\n",
       "      <td>Iran reportedly makes new push for uranium con...</td>\n",
       "      <td>Iranian negotiators reportedly have made a las...</td>\n",
       "      <td>REAL</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0                                              title  \\\n",
       "0        8476                       You Can Smell Hillary’s Fear   \n",
       "1       10294  Watch The Exact Moment Paul Ryan Committed Pol...   \n",
       "2        3608        Kerry to go to Paris in gesture of sympathy   \n",
       "3       10142  Bernie supporters on Twitter erupt in anger ag...   \n",
       "4         875   The Battle of New York: Why This Primary Matters   \n",
       "5        6903                                        Tehran, USA   \n",
       "6        7341  Girl Horrified At What She Watches Boyfriend D...   \n",
       "7          95                  ‘Britain’s Schindler’ Dies at 106   \n",
       "8        4869  Fact check: Trump and Clinton at the 'commande...   \n",
       "9        2909  Iran reportedly makes new push for uranium con...   \n",
       "\n",
       "                                                text label  \n",
       "0  Daniel Greenfield, a Shillman Journalism Fello...  FAKE  \n",
       "1  Google Pinterest Digg Linkedin Reddit Stumbleu...  FAKE  \n",
       "2  U.S. Secretary of State John F. Kerry said Mon...  REAL  \n",
       "3  — Kaydee King (@KaydeeKing) November 9, 2016 T...  FAKE  \n",
       "4  It's primary day in New York and front-runners...  REAL  \n",
       "5    \\nI’m not an immigrant, but my grandparents ...  FAKE  \n",
       "6  Share This Baylee Luciani (left), Screenshot o...  FAKE  \n",
       "7  A Czech stockbroker who saved more than 650 Je...  REAL  \n",
       "8  Hillary Clinton and Donald Trump made some ina...  REAL  \n",
       "9  Iranian negotiators reportedly have made a las...  REAL  "
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "news_data= pd.read_csv(\"news.csv\")\n",
    "news_data.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6981ab7d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 6335 entries, 0 to 6334\n",
      "Data columns (total 4 columns):\n",
      " #   Column      Non-Null Count  Dtype \n",
      "---  ------      --------------  ----- \n",
      " 0   Unnamed: 0  6335 non-null   int64 \n",
      " 1   title       6335 non-null   object\n",
      " 2   text        6335 non-null   object\n",
      " 3   label       6335 non-null   object\n",
      "dtypes: int64(1), object(3)\n",
      "memory usage: 198.1+ KB\n"
     ]
    }
   ],
   "source": [
    "news_data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fcb92843",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(6335, 4)"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "news_data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37abe593",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "REAL    3171\n",
       "FAKE    3164\n",
       "Name: label, dtype: int64"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "news_data[\"label\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "61fd2236",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    FAKE\n",
       "1    FAKE\n",
       "2    REAL\n",
       "3    FAKE\n",
       "4    REAL\n",
       "5    FAKE\n",
       "6    FAKE\n",
       "7    REAL\n",
       "8    REAL\n",
       "9    REAL\n",
       "Name: label, dtype: object"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "labels= news_data.label\n",
    "labels.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ff2c2fa1",
   "metadata": {},
   "source": [
    "#### 3- Build the model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e76f93ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "#First, we split the dataset into train & test samples:\n",
    "x_train, x_test, y_train, y_test= train_test_split(news_data[\"text\"], labels, test_size= 0.4, random_state= 7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb91f62d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Then we’ll initialize TfidfVectorizer with English stop words\n",
    "vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)\n",
    "tfidf_train=vectorizer.fit_transform(x_train) \n",
    "tfidf_test=vectorizer.transform(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "56cc526d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create a PassiveAggressiveClassifier\n",
    "passive=PassiveAggressiveClassifier(max_iter=50)\n",
    "passive.fit(tfidf_train,y_train)\n",
    "\n",
    "y_pred=passive.predict(tfidf_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "45b34d86",
   "metadata": {},
   "source": [
    "#### 4- Evaluate the model's accuracy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e09416c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1188,   82],\n",
       "       [  89, 1175]], dtype=int64)"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Create a confusion matrix\n",
    "matrix= confusion_matrix(y_test,y_pred, labels=['FAKE','REAL'])\n",
    "matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f04a52f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Visualize the confusion matrix\n",
    "sns.heatmap(matrix, annot=True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d32cfaf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "93.25177584846092"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Calculate the model's accuracy\n",
    "Accuracy=accuracy_score(y_test,y_pred)\n",
    "Accuracy*100"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cc8eecf4",
   "metadata": {},
   "source": [
    "#### The model's accuracy is 93%"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6cb198db",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "        FAKE       0.93      0.94      0.93      1270\n",
      "        REAL       0.93      0.93      0.93      1264\n",
      "\n",
      "    accuracy                           0.93      2534\n",
      "   macro avg       0.93      0.93      0.93      2534\n",
      "weighted avg       0.93      0.93      0.93      2534\n",
      "\n"
     ]
    }
   ],
   "source": [
    "Report= classification_report(y_test, y_pred)\n",
    "print(Report)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf00efa8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
