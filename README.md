# italy_immigration_trends
Exploring immigration to and migration from Italy data with Dash.

## Table of Contents
- General Information
- Setup
- Usage
- Challenges
- Project Results
- Future Data Exploration Ideas
- Acknowledgements
- Contact

## General Information
I’m uploading the code of the data I explored on the immigration to Italy, the country where I... migrated from!🇮🇹✈️🇬🇧

The goal was to explore immigration and migration data to see if we could find any interesting pattern. I extracted the data from a dataset found on [Kaggle](https://www.kaggle.com/datasets/luigigno/italy-immigration-data-by-the-un/data?select=Italy.xlsx), constructed a data frame (made up of 383 data points), and built an interactive dashboard. I also want to support other coders who are interested in knowing more about their own country just like me and want to learn how to plot their own data visualisations!📈

## Setup
First off, make sure you have conda🐍👀:

`conda create -n <replace-with-name-you-want> python=3.11`

`conda activate <replace-with-name-you-want>`

`pip install -r requirements.txt`

## Usage
Check out `italy_dashboard.py` in my repo to see how I've extracted, cleansed, explored, analysed the data, and created the interactive dashboard!

## Challenges
One of the biggest challenges was designing the skeleton of the dashboard. I created a drop-down menu for the category (e.g., Immigrants/Emigrants), the year, and the continent to display the data at a more granular level. This helped me discover some interesting insights about immigration and migration trends. I also had to create some if statements depending on the option that the user chooses (e.g., if both category and year are selected and no continent is selected). This helped me make the skeleton of the dashboard more coherent so that it could give back the results that the user wanted.

## Project Results
Here are the main conclusions we reached so far:

- The most represented nationality among immigrants to Italy is Romania, followed by Albania and Morocco. Between 1991 and 1996, Moroccan reached Italy due to low earnings and poor living conditions. From 1997 to 2002, the Albanian diaspora was at its peak after the breakdown of the communist regime in 1990, and Italy had been a symbol of the West for many Albanians during the communist period because of its geographic proximity. From 2002 until 2013, Romania outweighs Albanian migration, making up for an astonihing 79.2% of European migrants to Italy in 2007 only. This is because Romanians were in search for jobs and better working conditions. 

- From 1991 to 2004, the most represented nationality among emigrants from Italy is Germany, then Morocco in 2005, and Romania from 2006 to 2013. This might be because lots of people from South Tyrol (which has a significant German-speaking population), emigrated to other countries when Italy experienced economic hardship and political instability.

## Future Data Exploration Ideas
Since there are some missing values (e.g., in the emigration category between 2000 and 2003), we could find a dataset with more data points. It'd also be interesting to find data about the 60s, 70s, and 80s emigration/migration trends to have a more complete overview of the trend over time. Something even more intriguing would be to discover more about which region people migrate to or emigrate from Italy! This would help us compare the patterns between North and South. 

## Acknowledgements 
A massive thank you to [Ward Haddadin](https://github.com/wardhaddadin1) for the help in structuring the dashboard skeleton! As always, I wouldn't have made it without you!

## Contact
For any question, drop me a line at giorgiadt14@gmail.com and I'll be happy to help you out! Feel free to message me on [LinkedIn](https://www.linkedin.com/in/giorgia-dim/) too! Happy coding!💻
 
