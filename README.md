# There is no plan Bee without them 🐝
A new project proposal about bees and honey

## Abstract
Pollinators around the world play a central role in our agriculture with an estimated economic benefit of €235bn per year. Up to 75% of our crops are dependent on pollination and honeybees account for most of it. Yet, in Europe and the USA the bee population has been declining at an alarming rate during the last decades. As by-hand pollination is not an alternative, it is impossible to imagine a world without them. [1]

With this project, we first aim at giving insights about the state of bee health and honey produced and traded using the [FAO datasets](http://www.fao.org/faostat/en/#data). Secondly, we focus on the USA using results from [US Departement of Agriculture](https://quickstats.nass.usda.gov/) in order to identify and present the main factors of bee decline. Finally, we propose a case study about almonds in California to show the consequences of a lack of bees.

[[1](http://sos-bees.org/wp-content/uploads/2014/04/BeesInDecline.pdf)] *Bees in Decline*, Greenpeace, 2013


## Research questions

- How do the continents compare in terms of bee decline from 1961 to these days?
- How do changes in honey production relate to number of beehives in Europe and the USA?
- What are the consequences of bee decline on the patterns of honey import/export around the world?
- What is the relation between US cases of Colony Collapse Disorder and the main factors of CCD?
- California accounts for 80% of the world almond production, what is the impact of bees on this industry in the 21st century?

## Datasets

### Primary
- [USDA NASS](https://quickstats.nass.usda.gov/)
    - Datasets of the US departement of agriculture
    - Search criterions:
        - Sector: Animal & Products
        - Commodity: Honey
        - Data item: Honey, Bee colonies
        - Geographic Level: State (or National)
    - Available interesting datasets:
        - Inventory (number of colonies), county / state / national level
        - Losses, (CCD, deadout) from 2015-2019
        - Affected by (Varroa, pesticides)
    - Date range: 21st century
- [Live Stock FAO](http://www.fao.org/faostat/en/#data/QA)
    - Amount of beehives per country per year (1961-2017)
- [Livestock Primary FAO](http://www.fao.org/faostat/en/#data/QL)
    - Amount of produced honey per country per year (1961-2017)
- [Crops FAO](http://www.fao.org/faostat/en/#data/QC)
    - Amount of produced crops per country per year (1961-2017)
    - Interesting for the case study about almond
- [Trade Matrix FAO](http://www.fao.org/faostat/en/#data/TM)
    - Import/Export honey quantities (tons) (and value ($)) for pairs of countries (1986-2017)

### Secondary (if we find something interesting)
- [Bee Colony Statistical Data from 1987-2017](https://data.world/finley/bee-colony-statistical-data-from-1987-2017)
    - Cleaned dataset from the USDA available on data.world
    - USA Average loss per state per year (2010-2017)
        - Note: would still be interesting to use this one
    - USA Bee Colony survey data per state per year (1987-2017)
    - USA Bee Colony census per county per year (2002-2012)
- [Food Balance Sheet FAO](http://www.fao.org/faostat/en/#data/FBS)
    - Domestic supply quantities
- [Pesticide use](http://www.fao.org/faostat/en/#data/RP)
    - Pesticide use around the world
    - (As of now, I didn't find something relevant with that dataset, and neonicotinoids aren't reported)
- [Value of Agricultural Production FAO](http://www.fao.org/faostat/en/#data/QV)
    - Gross / Net production value of honey per country per year (1961-2016)
- [Honey production in the US by state](https://github.com/TarHeel45/Honey-Production-Dashboard)


## Ressources

- [Colony Collapse Disorder](https://en.wikipedia.org/wiki/Colony_collapse_disorder)
    - Varroa
        - APHIS report [visualization](https://bip2.beeinformed.org/state_reports/)
            - data can be found [here](https://quickstats.nass.usda.gov/)
        - [EPFL: AI to save the bees](https://actu.epfl.ch/news/de-l-intelligence-artificielle-pour-sauver-les-abe/)
    - Pesticide
        - Neonicotinoids 
        - Imidacloprid, thiamethoxam, clothianidin, fipronil, chlorpyriphos, cypermethrin and deltamethrin. (Greenpeace, *Bees in decline*, p. 7)
    - Climate change
- [Information website Bee Informed](https://bip2.beeinformed.org/)
    - Multiple data visualization of USA datasets
- [Honey Bee research association COLOSS](https://coloss.org/)
    - [Guidelines](https://coloss.org/statistical-guidelines-for-apis-mellifera-research/): research about bees
    - Lots of pdf reports with some data that we could scrap about EU / CH data 
- [Data story example about bees](https://towardsdatascience.com/whats-buzzing-with-the-bees-99f9be0bc4c6)
    - An Exploratory Data Analytics Project Investigating Honey Bee Populations in the USA
- [SOS-bee (Greenpeace)](http://sos-bees.org/)
    - Situation, causes and solution to solve the bee problem
    - Report *Bees in decline* [pdf](http://sos-bees.org/wp-content/uploads/2014/04/BeesInDecline.pdf) (48 pages but you just need to read the executive summary)


## Ideas

- **Case study**: California needs a huge amount of bee every spring to pollinate its almond trees, is there a correlation between almond production and bees ? (i.e. 2006/7 was a rough winter for bees in the States and the yield for 2007 is lower)
    - When did California start to need bees from the rest of the USA?
    - [Dataset for almond production FAO](http://www.fao.org/faostat/en/#data/QC) There could actually be a correlation (yield in 2007 is much lower)
    - Has the price of almond risen?
    - What are the insights we gain from this example?


## Technologies
- [Chord diagram](https://plot.ly/python/v3/filled-chord-diagram/)
- [Plotly](https://plot.ly/): interactive web visualization library
- [Bokeh](http://bokeh.org/): interactive visualization library
- [Folium](https://python-visualization.github.io/folium/): plot on geo data
- Leaflet.js: technology behind Folium

