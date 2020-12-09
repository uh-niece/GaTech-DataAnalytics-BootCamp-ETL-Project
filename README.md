In this project, the analysts are asked to introduce ETL to perform ETL on real datasets. We are asked to scrape data from quotes.toscrape.com to gather quotes, tags, author name, and author details. Once the data was collected, we will store the data into MongoDB to create the predetermined tables.
    1. One table for quotes, this table can have the quote and author relationship 
    2. One table for author information
    3. One table to store quote and tag relation

Once completed, the analysts will create a FLASK API for the following endpoints:

- /quotes
- /authors
- /top10tags
