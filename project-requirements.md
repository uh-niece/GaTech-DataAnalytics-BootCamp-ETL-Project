## you will scrape the following information from http://quotes.toscrape.com/

- quote text
- tags
- Author name
- Author Details
  - born
  - description

## Store the collected information into MongoDB( you can use Mongo atlas for this)

## Design the following three tables, Extract the data from mongoDB and load it into postgres

- one table for quotes, this table can have the quote and author relationship
- one table for author information
- one table to store quote and tag relation

## Create a FLASK API with the following endpoints

<details>
    <summary><strong>/quotes </strong></summary>

```
{
    total: <total number quotes scraped >,
    quotes : [
                {
                    text: <quote text >,
                    author name: <author name >,
                    tags: []
                },
	            ...
	        ]
}

```

</details>

<details>
    <summary><strong>/authors </strong></summary>

```
{
    total: <total number of authors>,
    details:[
            	{
            		name : <author name >,
            		description : <author description>,
            		born : <date of birth etc. >,
            		count : <total number of quotes by this author >,
            		quotes : [
                				{
                    				text: <quote text>,
                    				tags: []
                				},
            		...
            		]
            	},
        	...
    	]
}
```

</details>

<details>
    <summary><strong>/authors/< author name > </strong></summary>

```
{
    name: <Author name>,
    description: <author description>,
    born: <date of birth etc>
    number_of_quotes :  <total quotes by the author>
    quotes : [
    		{
    			text: <quote text>,
    			tags: []
    		},
            ...
    	]
}
```

</details>

<details>
    <summary><strong>/tags </strong></summary>

```
{
	count: <total tags>,
	details:[
        		{
        			name: < tag>,
        			number_of_quotes :  <total quotes this tag appears in >
        			quotes : [
                				{
                					text: <quote text>,
                					tags: []
                				},
                                ...
    				        ]
        		},
            ...
	]
}

```

</details>

<details>	
    <summary><strong>/tags/< tag > </strong></summary>

```
{
	tag : <tag name>,
	count : <number of quotes this tag appears in >,
	quotes : [
			{
    			quote : <quote text >,
    			tags : []
			},
		...
		]

}

```

</details>

<details>
   <summary><strong>/top10tags </strong></summary>

```
	[
		{
		tag: < tag name > ,
		quote count: < number of quotes this tag appears in >
		},
		...
	]

```

</details>
