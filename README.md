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
I’m uploading the code of the visualisations I created on the immigration to Italy, the country where I... migrated from!🇮🇹✈️🇬🇧

The goal was to explore immigration and migration data to see if we could find any interesting patterns. I extracted the data from a dataset found on [Kaggle](https://www.kaggle.com/datasets/luigigno/italy-immigration-data-by-the-un/data?select=Italy.xlsx), constructed a data frame (made up of 383 data points), and built an interactive dashboard!📈

## Setup
First off, make sure you have conda🐍👀:

`conda create -n <replace-with-name-you-want> python=3.11`

`conda activate <replace-with-name-you-want>`

`pip install -r requirements.txt`

## Usage
Check out `italy_dashboard.py` in my repo to see how I've extracted, cleansed, explored, analysed the data, and created the interactive dashboard!

To run the dashboard, type `python italy_dashboard.py` in your terminal. A weblink will pop up. Click on it to visualize the dashboard and play around with it!

## Challenges
One of the biggest challenges was designing the skeleton of the dashboard. I had to create a conditional logic to make sure that the skeleton displays the right graphs.

## Project Results
Here are the main conclusions we reached so far:

- The most represented nationality among immigrants to Italy is Romania, followed by Albania and Morocco. 

- The most represented nationality among emigrants from Italy is Germany, followed by Morocco and Romania. 

## Future Data Exploration Ideas
We could use alternative columns of this dataset to explore the data differently. For instance, we could filter the dataset by regions and plot graphs to find interesting patterns through this filter!

## Acknowledgements 
A massive thank you to [Ward Haddadin](https://github.com/wardhaddadin1) for the help in structuring the dashboard skeleton! As always, I wouldn't have made it without you!

## Contact
For any question, drop me a line at giorgiadt14@gmail.com and I'll be happy to help you out! Feel free to message me on [LinkedIn](https://www.linkedin.com/in/giorgia-dim/) too! Happy coding!💻
