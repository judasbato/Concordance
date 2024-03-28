# Text Concordance Generator

This Python script generates a concordance for a given textual material. A concordance is a list of all the words in a text, along with the line numbers where each word occurs and a small context of the text around each occurrence.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)

## Introduction

Concordance generation is a useful tool in text analysis and computational linguistics. This script takes a textual material as input, cleans it by converting to lowercase and removing punctuation, then generates a concordance excluding common stop words.

## Features

- Cleans the input text by converting to lowercase and removing punctuation.
- Excludes common stop words from the concordance.
- Provides line numbers and context for each occurrence of a word in the text.

## Requirements

- Python 3.x

## Usage

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Modify the `textual_material` and `stopwords` lists in the script as per your requirement.
4. Run the script `concordance_generator.py`.
5. View the generated concordance.

## Example

Consider the following input:

```python
textual_material = ["The Itsy Bitsy spider crawled up the water spout",
          "Down came the rain and washed the spider out",
          "Out came the sun and dried up all the rain",
          "and the Itsy Bitsy spider went up the spout again!"]

stopwords = ["a", "the", "of", "for", "any", "up", "out", "and", "not", "is", "say"]

Output:

itsy : Total Number: 2
Line : 1 The ITSY Bitsy spider crawled up the water spout 
Line : 4 and the ITSY Bitsy spider went up the spout again! 

bitsy : Total Number: 2
Line : 1 The Itsy BITSY spider crawled up the water spout 
Line : 4 and the Itsy BITSY spider went up the spout again! 

spider : Total Number: 3
Line : 1 The Itsy Bitsy SPIDER crawled up the water spout 
Line : 2 Down came the rain and washed the SPIDER out 
Line : 4 and the Itsy Bitsy SPIDER went up the spout again! 

crawled : Total Number: 1
Line : 1 The Itsy Bitsy spider CRAWLED up the water spout 

water : Total Number: 1
Line : 1 The Itsy Bitsy spider crawled up the WATER spout 

spout : Total Number: 2
Line : 1 The Itsy Bitsy spider crawled up the water SPOUT 
Line : 4 and the Itsy Bitsy spider went up the SPOUT again! 

down : Total Number: 1
Line : 2 DOWN came the rain and washed the spider out 

came : Total Number: 2
Line : 2 Down CAME the rain and washed the spider out 
Line : 3 Out CAME the sun and dried up all the rain 

rain : Total Number: 2
Line : 2 Down came the RAIN and washed the spider out 
Line : 3 Out came the sun and dried up all the RAIN 

washed : Total Number: 1
Line : 2 Down came the rain and WASHED the spider out 

sun : Total Number: 1
Line : 3 Out came the SUN and dried up all the rain 

dried : Total Number: 1
Line : 3 Out came the sun and DRIED up all the rain 

all : Total Number: 1
Line : 3 Out came the sun and dried up ALL the rain 

went : Total Number: 1
Line : 4 and the Itsy Bitsy spider WENT up the spout again! 

again : Total Number: 1
Line : 4 and the Itsy Bitsy spider went up the spout AGAIN!
