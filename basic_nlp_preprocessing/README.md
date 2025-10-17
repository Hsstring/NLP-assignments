#Assignment 1 — Basic NLP Preprocessing

## Objective
This assignment focuses on implementing **basic Natural Language Processing (NLP) preprocessing** tasks *from scratch* using **Regular Expressions (RegEx)** and **Python** — without relying on external libraries such as `nltk` for tokenization, stemming, or normalization.

---

## Tasks

### 1. Tokenization (English and Persian)
- Use **regular expressions** to split the given English and Persian texts into tokens.
- Consider delimiters such as **spaces**, **punctuation marks**, and **special characters**.
- Use `re.findall()` to extract and print all tokens.

### 2. Stemming (Porter Algorithm)
- Research and extract the **Porter stemming rules** from online resources.
- Implement these rules as **regular expression substitutions**.
- Use `re.sub()` to replace words with their stemmed forms.
- Print the final list of stemmed words.

### 3. Normalization
- Define normalization rules using regular expressions:
  - Remove or replace unwanted characters (extra spaces, punctuation).
  - Convert text to lowercase.
  - Handle accented or variant characters.
- Apply the rules using `re.sub()` and print the normalized output.

---

## Input Texts
### English Text
> After World War II, the British greatly reduced the use of the full stop and other punctuation points after abbreviations in at least semi-formal writing, while the Americans more readily kept such use until more recently, and still maintain it more than Britons. The classic example, considered by their American counterparts quite curious, was the maintenance of the internal comma in a British organisation of secret agents called the "Special Operations, Executive", "S.O., E", which is not found in histories written after about 1960.
>
> ... *(continues as provided in the assignment document)*

### Persian Text
> در شکل 2-1 نرخ اطلاعات اصلی سیگنال (یا کنترل) در مراحل مختلف فرایند نیز آمده است. نرخ اطلاعات در متن اولیه و خام پیام، نسبتاً پایین است (حدود bps 50 ...  
> *(continues as in the Persian section of the assignment)*

---

## Constraints
- You **must not** use `nltk.tokenize`, `nltk.stem`, or `nltk.normalize`.
- Only the **Python built-in `re` module** is allowed.
- Clearly mention and comment on any errors or limitations in your approach.

---

## Expected Output
1. List of English tokens  
2. List of Persian tokens  
3. Stemmed version of the English text  
4. Normalized version of both texts  
5. Brief note on observed errors or challenges



## 🧾 File Structure
