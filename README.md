# Simple Search System

## Abstract
This project develops a simple text search system using Flask, integrating web crawling, data indexing, and query processing capabilities. The objective is to provide a robust and efficient search tool for Wikipedia articles. The next steps involve implementing advanced text processing features, enhancing the user interface, and optimizing the system for scalability and security.

## Overview
The Flask-Based Wikipedia Text Search System leverages the power of Scrapy for dynamic web crawling, Scikit-Learn for advanced text processing, and Flask to manage web interactions, aiming to provide an efficient search platform. This project addresses the challenge of quickly accessing updated and relevant information from Wikipedia's vast repository. By integrating a custom crawler with a TF-IDF indexer, the system ensures real-time data accuracy and relevancy, enhancing user experience through a responsive search interface. This solution is designed to serve as a scalable model for real-time information retrieval, showcasing a practical application of machine learning techniques in processing and delivering structured information from unstructured data sources like Wikipedia.

## Design
The system design integrates three key functionalities: data collection, indexing, and user interaction, ensuring a seamless search experience. Utilizing Scrapy, the system efficiently crawls and extracts data from specified Wikipedia sections, capturing rich content along with metadata such as article summaries and categories. This data is stored in json file as 'output.json' then processed using the TF-IDF vectorization provided by Scikit-Learn to create a searchable index that supports quick retrieval of information based on query relevance(in index.py). The Flask framework underpins the user interface, enabling both direct web interactions and API access for submitting queries and receiving responses. This design not only maximizes efficiency and scalability but also maintains simplicity, making it adaptable for future enhancements such as integrating more complex natural language processing tools or expanding the user interface.

## Architecture
The architecture of the Flask-Based Wikipedia Text Search System is structured around modular, interconnected components that facilitate efficient data handling and user interaction. At its core, the architecture consists of the Scrapy crawler for automated data extraction from Wikipedia, which outputs structured JSON files containing detailed article metadata and content. These files serve as input for the TF-IDF indexing module, implemented using Scikit-Learn, which processes the text to create a dense matrix that quantifies term significance across documents. The indexed data is stored locally, allowing the Flask application to perform rapid searches by computing cosine similarities between query vectors and the document matrix. The Flask server, acting as both a web server and an API endpoint, manages user requests and delivers search results through a clean, responsive web interface or JSON responses for API consumers. This design ensures robust performance and scalability, with clear separation of concerns between data collection, processing, and user service delivery, facilitating maintenance and future upgrades.

## Operation
To begin, clone the repository from GitHub using the command:
```
git clone https://github.com/KaungMyatNaing9/NewsSearch.git
```
Then in your terminal or command prompt cd to the file that you have already cloned by:
```
cd NewsSearch
or search for the file that you have clone and write the file address
cd file address
```
