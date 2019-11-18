# Environmental impact of Agriculture

## Abstract

Enviromental concerns have drastically increased in the past years and agriculture's role in polluting the soils, air and water is a topic of choice. The *Global Food & Agriculture Statistics* provides global informations on agriculture  amplitude and impact. Leveraging those data, we would like to find out if countries around the world have grasped the full extent of situation: are behaviors changing for the better ?

On the other hand, we want to find countries that have a worse impact. In a globalised world, however, the producer and the consumer rarely are the same. Using data from FAO's *Detailed trade matrix*, we would also like to track the impact of consumption back, so that high-producing, low-consumming countries get a fair comparison.

Data visualization would greatly benefit from dynamic maps, where impact per year, category and/or countries can be tuned and selected.

## Research questions

+ What is the environmental impact of agriculture in each country in the past year ? 
+ How did agricultural habits change over the year: are polluting practice in decline ?
+ Are some countries more respectful than others and what can we learn from them ?
+ Is it possible to find the consumer environmental impact, taking trades into account ?

## Dataset

+ [Global Food & Agriculture Statistics](https://www.kaggle.com/unitednations/global-food-agriculture-statistics)
+ [Detailed trade matrix](http://www.fao.org/faostat/en/#data/TM)

While the *Global Food & Agriculture Statistics* is a fairly large dataset (7 GB), it is splitted into several tables of managable size. We intend to use mainly the `Environment_X`, `Emissions_X`, `Production_X` and `Trade_X` datasets for our purposes. The *detailed trade matrix* will assist in taking detailed trade informations into account, so that the actual consumption of countries is estimated.

## A list of internal milestones up until project milestone 2

+ 1st week & 2nd week
    + Impact of Production (*Global Food & Agriculture Statistics* dataset)
        + Select the most relevant tables and indicators
        + Clean the data and assess the amount of missing data
+ 2nd week & 3rd week
    + Production
        + compute indicators for countries
+ 3rd week
    + Production
        + Verify data needs are met, go back to previous tasks if missing data / analysis
    + Consumption (*Detailed trade matrix* dataset)
        + Clean the trade data
+ 4th week
    + Consumption
        + verify coherence between trade data of both datasets
    + Both
        + visualization


## Questions for TAa
+ Has the project a suitable workload ?
+ What does the FLAG columns mean in the dataset ?
+ Are milestones meant to ensure that the project progresses, or are they strict deadlines for the different parts ?
e.g. Can we do additional data analysis between Milestone 2 and Report, or *must* all used data & computations be present in the Milestone 2 notebook ?