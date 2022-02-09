# Indonesian Adjective Words Sentiment Dataset

Indonesian adjective sentiment dataset with scrapper tools

## Scrapper

In this repository there is a Scrapper tool that can be used

```py
# app.py
import Scrapper

app = Scrapper
app.Start()
```

## Dataset

There are two file for dataset on this project

- `Dataset\indonesian-adjective-sentiment-raw.csv` contain raw information about Indonesian Adjective
- `Dataset\indonesian-adjective-sentiment-score.csv` contain sentiment labels

## Data Table

### Table from `indonesian-adjective-sentiment-raw.csv`

| ID | Word | URL | Spelling | Explanation |
| --- | --- | --- | -------- | ----------- |
| 1 | abadi | <https://kbbi.kata.web.id/abadi/> | aba.di | kekal; tidak berkesudahan: di dunia ini tidak ada yang abadi |
| 2 | abaktinal | <https://kbbi.kata.web.id/abaktinal/> | abak.ti.nal | istilah biologi berkenaan dengan sisi tubuh yang tidak mengandung mulut, seperti pada binatang laut |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

```text
Description for each column:

ID = Primary key (UID)
Word = Word in Indonesian Language
URL = URL from kbbi <https://kbbi.kata.web.id>
Spelling = How to pronounce the word
Explanation = Detail and explanation
```

### Table from `indonesian-adjective-sentiment-score.csv`

| ID | Score |
| --- | --- |
| 1 | 2 |
| 2 | 0 |
| ... | ... |
| ... | ... |

```text
ID = Foreign key (UID) from indonesian-adjective-sentiment-raw.csv
Score = Sentiment label
```

## Sentiment

There are 5 types of sentiment

| Code | Sentiment |
| ---- | --------- |
| -2 | Very Negative |
| -1 | Negative |
| 0 | Neutral |
| 1 | Positive |
| 2 | Very Positive |

## License

```text
MIT License

Copyright (c) 2021 Muhammad Razif Rizqullah

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
