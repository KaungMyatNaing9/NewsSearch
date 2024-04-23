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
Step 1: To begin, clone the repository from GitHub using the command:
```
git clone https://github.com/KaungMyatNaing9/NewsSearch.git
```
Step 2: Then in your terminal or command prompt cd to the file that you have already cloned by:
```
cd NewsSearch
or search for the file that you have clone and write the file address
cd file address
```
Step 3: When you are in NewsSearch you can run the code by:
```
python index.py
```
Step 4: If the code runs it will appear in your terminal:
```
 * Serving Flask app 'index'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 766-799-751
```
Step 5: If this appear go to the website it said which is:
```
http://127.0.0.1:5000
```
You will see the search bar there and you can try to test it. After you type something and click search it will give you 10 closest wikipedia pages with their index,score and url. Copy paste the url and it will go to the page you want to search. <br/>
<br/>
Error Step 1: If the above doesnt work for you,lets try using virtual environment, type in terminal:
```
For window:
.\venv\Scripts\activate
For Mac/Linux:
source venv/bin/activate
```
Error Step 2 : Then try:
```
python index.py
```
Then follow Step 4 from above if it works for you now! <br/>
<br/>
The above steps just used already generated wiki crawl data and process the indexing and flask, if you want different data or more data the you need to modify the crafting code a bit and train it by:
```
cd wiki_crawler
cd wiki_crawler
scrapy crawl wiki -o output2.json
```
This will give you a output2.json file in spyder directory, you can copy or cut this file and paste it in the same page or directory with index.py . Then run the index.py and you will get something different!

## Conclusion
The Flask-Based Wikipedia Text Search System has been successfully implemented and operates effectively under current conditions. The system reliably crawls Wikipedia, indexes the content using TF-IDF, and serves this content through a responsive Flask application. However, while the backend operations run smoothly, the frontend user interface requires further development to enhance user engagement and usability.<br/>
<br/>
Current search functionality, while operational, shows limitations in data accuracy and retrieval precision. This stems partly from the inherent challenges in the depth and breadth of data collected during the crawling process, which affects the comprehensiveness of the search results. Additionally, the search algorithm's effectiveness is occasionally hindered by the simplistic nature of the TF-IDF approach, which may not always capture the nuances of language used in queries and documents.
### Future improvements
1. Enhancing the Frontend: A more dynamic and aesthetically pleasing interface should be developed, possibly using frameworks like React or Vue.js to provide a more interactive experience. <br/>
2. Refining Data Collection: Improving the crawler's capability to parse and filter data more effectively will help in gathering more relevant and diverse datasets. Utilizing more sophisticated natural language processing techniques could also enhance the system’s understanding of the content. <br/>
3. Upgrading Search Algorithms: Incorporating more advanced search algorithms such as BM25 or even neural network-based approaches could significantly improve search accuracy and relevance.<br/>
### Caveats and Cautions:
The current system, while functional, should be used with the understanding that the data and search results might not cover all potential Wikipedia content comprehensively. Users should also be cautious about the potential for outdated information if the crawler's schedule is not maintained rigorously.<br/>
In conclusion, the project has laid a solid foundation for a powerful educational and research tool, with ample room for enhancements that could address current shortcomings and elevate the overall effectiveness and user satisfaction.

## Data 
The primary source of data for the Flask-Based Wikipedia Text Search System is Wikipedia, specifically targeting various thematic content pages to ensure a broad yet relevant data collection. The data is sourced dynamically using a Scrapy crawler, which navigates through predefined Wikipedia content pages to gather articles, summaries, and metadata. This approach ensures that the system captures up-to-date information directly from Wikipedia, reflecting the latest content available on the site.
Some start URLs:
```
https://en.wikipedia.org/wiki/Wikipedia:Contents/People_and_self
https://en.wikipedia.org/wiki/Wikipedia:Contents/Technology_and_applied_sciences
https://en.wikipedia.org/wiki/Wikipedia:Good_articles
https://en.wikipedia.org/wiki/Wikipedia:Contents/Natural_and_physical_sciences
https://en.wikipedia.org/wiki/Wikipedia:Contents/History_and_events
```
The Max Length is set to 3 and Max page is set to 300!

## Source Code



