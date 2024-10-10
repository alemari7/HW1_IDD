# Homework 1 - Data Engineering Course

This repository contains the source code for the first homework assignment of the Data Engineering course. The project was carried out by **Alessio Marinucci** and **Riccardo Felici**.

## Project Objective

The objective of this project is to extract specific data from HTML web pages using **XPath expressions**. The topic is related to **Data Science**, and the data is extracted from research papers available on the website [arXiv.org](https://arxiv.org/).

## Topic Selection

We have chosen the topic of **Artificial Intelligence (AI)** for this project. A total of 300 HTML files have been downloaded from arXiv, focusing on AI-related papers.

## Data to be Extracted

For each research paper, the following elements are extracted using **XPath**:

- **Tables**: All the tables present in the paper.
- **Captions**: The captions associated with each table.
- **Footnotes**: Any footnotes present for the tables (if available).
- **Referenced Paragraphs**: Paragraphs that reference the specific table.

### Output Format

The extracted data is stored in a **JSON** file, ensuring that all relevant information for each paper is neatly organized and easily accessible.

---

## Example of JSON Structure

```json
{
  "paper_1": {
    "title": "Artificial Intelligence Research Paper Title",
    "tables": [
      {
        "table_id": 1,
        "caption": "Table 1: Sample Data",
        "footnotes": "Footnote explaining the table",
        "referenced_paragraphs": [
          "This table highlights the key metrics used in AI research..."
        ]
      },
      {
        "table_id": 2,
        "caption": "Table 2: Model Performance",
        "footnotes": null,
        "referenced_paragraphs": [
          "In Table 2, we compare the performance of various models..."
        ]
      }
    ]
  }
}
```

## Code Overview

This project involves the following steps:

1. **Scraping HTML Files**:
   The script downloads recent AI-related research papers in HTML format from [arXiv](https://arxiv.org/). The files are stored in a folder called `sources` for further analysis. The scraping process uses **BeautifulSoup** to parse the page and filter the links to the desired HTML files based on specific criteria.

2. **XPath Extraction**:
   Once the HTML files are downloaded, the next phase involves extracting specific data using **XPath** expressions. The goal is to extract:
   - **Tables**
   - **Captions** associated with the tables
   - **Footnotes** (if any)
   - **Referenced paragraphs** that mention the tables.

3. **Saving Data**:
   The extracted information is saved in a structured **JSON** file, ensuring easy access and further processing of the data.

5. **Automation**:
   The code is designed to automate the entire workflow, from downloading HTML files to extracting and storing relevant data. The script can handle multiple HTML files and be customized to adjust the number of files or different extraction needs.

## URL List

