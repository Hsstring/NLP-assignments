import re
my_string = """After World War II, the British greatly reduced the use of the full stop and other punctuation points after abbreviations in at least semi-formal writing, while the Americans more readily kept such use until more recently, and still maintain it more than Britons. The classic example, considered by their American counterparts quite curious, was the maintenance of the internal comma in a British organisation of secret agents called the "Special Operations, Executive", "S.O., E", which is not found in histories written after about 1960.
But before that, many Britons were more scrupulous at maintaining the French form. In French, the period only follows an abbreviation if the last letter in the abbreviation is not the last letter of its antecedent: "M." is the abbreviation for "monsieur" while "Mme" is that for "madame". Like many other cross-channel linguistic acquisitions, many Britons readily took this up and followed this rule themselves, while the Americans took a simpler rule and applied it rigorously.
Over the years, however, the lack of convention in some style guides has made it difficult to determine which two-word abbreviations should be abbreviated with periods and which should not. The U.S. media tend to use periods in two-word abbreviations like United States (U.S.), but not personal computer (PC) or television (TV). Many British publications have gradually done away with the use of periods in abbreviations.
Minimization of punctuation in typewritten material became economically desirable in the 1960s and 1970s for the many users of carbon-film ribbons since a period or comma consumed the same length of non-reusable expensive ribbon as did a capital letter.
Widespread use of electronic communication through mobile phones and the Internet during the 1990s allowed for a marked rise in colloquial abbreviation. This was due largely to increasing popularity of textual communication services such as instant- and text messaging. SMS, for instance, supports message lengths of 160 characters at most (using the GSM 03.38 character set). This brevity gave rise to an informal abbreviation scheme sometimes called Textese, with which 10% or more of the words in a typical SMS message are abbreviated. More recently Twitter, a popular social networking service, began driving abbreviation use with 140 character message limits.
"""


# Porter algorithm rules using sub function and regex
def apply_porter_stemming(text):
    # Rule 1a: Plurals
    text = re.sub(r'(sses)\b', r'ss', text)
    text = re.sub(r'(ies)\b', r'i', text)
    text = re.sub(r'([^s])s\b', r'\1', text)

    # Rule 1b: Past tense and gerund forms
    text = re.sub(r'(ed|ing)\b', '', text)

    # Rule 1c: Change 'y' to 'i' when preceded by a vowel
    text = re.sub(r'([aeiou])y\b', r'\1i', text)

    # Rule 2: Double suffixes
    text = re.sub(r'ization\b', 'ize', text)
    text = re.sub(r'ational\b', 'ate', text)
    text = re.sub(r'ation\b', 'ate', text)
    text = re.sub(r'ator\b', 'ate', text)
    text = re.sub(r'alism\b', 'al', text)
    text = re.sub(r'iveness\b', 'ive', text)
    text = re.sub(r'fulness\b', 'ful', text)
    text = re.sub(r'ousness\b', 'ous', text)
    text = re.sub(r'aliti\b', 'al', text)
    text = re.sub(r'iviti\b', 'ive', text)
    text = re.sub(r'biliti\b', 'ble', text)

    # Rule 3:
    text = re.sub(r'icate\b', 'ic', text)
    text = re.sub(r'ative\b', '', text)
    text = re.sub(r'alize\b', 'al', text)
    text = re.sub(r'iciti\b', 'ic', text)
    text = re.sub(r'ical\b', 'ic', text)
    text = re.sub(r'ful\b', '', text)
    text = re.sub(r'ness\b', '', text)

    # Rule 4: adverb suffix -ly
    text = re.sub(r'ly\b', '', text)

    return text

def normalization(text):
    # Step1: Lowercase
    text = text.lower()

    # Step2: Remove punctuation
    text = re.sub(r'[^\w\s.-]', '', text)

    # Step3: Remove extra whitespace
    text = text = re.sub(r'\s+', ' ', text).strip()

    # Step4: Handle common contractions
    contractions = {
        "don't": "do not",
        "doesn't": "does not",
        "can't": "cannot",
        "won't": "will not",
        "i'm": "i am",
        "you're": "you are",
        "we're": "we are",
        "they're": "they are",
        "isn't": "is not",
        "aren't": "are not",
        "wasn't": "was not",
        "weren't": "were not",
        "it's": "it is",
        "that's": "that is",
        "there's": "there is",
    }

    for contraction, expanded_form in contractions.items():
        text = re.sub(r'\b' + contraction + r'\b', expanded_form, text)

    # Step5: Remove stop words
    tokens = text.split()
    stop_words = set(["and", "the", "is", "in", "of", "on", "an", "a"])
    tokens = [word for word in tokens if word not in stop_words]

    return text


PATTERN = r"""
    (?:[A-Z]\.)+              # Abbreviations, e.g. U.S.A., S.O.E.
    | \w+(?:-\w+)*            # Words with optional internal hyphens
    | \$?\d+(?:\.\d+)?%?      # Currency and percentages, e.g. $12.40, 82%
    | \.\.\.                  # Ellipsis
    | [.,;"’?():_‘-]          # Separate punctuation tokens
"""
# Find all tokens
tokens = re.findall(PATTERN, my_string, re.VERBOSE)

# Join tokens to form the text for stemming
text = " ".join(tokens)

# Apply stemming
stemmed_text = apply_porter_stemming(text)

# Apply normalization
normalized_text = normalization(stemmed_text)

print(normalized_text)

