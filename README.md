# Homework 3
## Group 12
In this repository there are the solutions for the Homework 3:  
Gianluca Procopio - 1942103  
Andrea Polidori - 2143429  
Lorenzo Incoronato - 1916863  
Riccardo Violano - 2148833

In the folder _hw3_ you can find:
- `HW3_def.ipynb` is the main file that contains all the answers to all the questions;
- In the **es1** folder there are all the modules we used in order to solve the excercise one. The moduke `scraping_link.py` allows us retrieve all the links, the module `crawl.py` allows us to collect all the pages' HTML code. In the end, through module `parser.py` we extracted all the infos we needed and we created the final _.csv_. Notice that in the notebook you will find only the comments to our solutions, but there isn't any line of code;
- In the **Command Line** folder there is the `.sh` file containg our solution and a screenshot with the result;
- In the folder **important_output** we stored some important output we got when solving the excercise 2 and 4. In `vocabulary.txt`we have the list of all the words that you can find in the 'description' colum after the pre-processing part (stemming, punctuations remove, typing error) with a `term_id` for each one that we will use to indentify each term; in `inverted_index.txt` for each `term_id` we have a list that contains all the `doc_id` where that term is located; instead, `inverted_index_tfidf.txt` is a better version of the previous file where we added, for each `doc_id`, the _tf-idf_; 
