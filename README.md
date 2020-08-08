# Title: "Udacity_Project_EDA"
## Author: "Edward Carter"
## date: "7/21/2020"
output: html_document
---
========================================================



```{r echo=FALSE, message=FALSE, warning=FALSE, packages}

library(dplyr)
library(ggplot2)
library(gridExtra)
# Load all of the packages that you end up using in your analysis in this code
# chunk.

# Notice that the parameter "echo" was set to FALSE for this code chunk. This
# prevents the code from displaying in the knitted HTML output. You should set
# echo=FALSE for all code chunks in your file, unless it makes sense for your
# report to show the code that generated a particular plot.

# The other parameters for "message" and "warning" should also be set to FALSE
# for other code chunks once you have verified that each plot comes out as you
# want it to. This will clean up the flow of your report.


```

```{r echo=FALSE, Load_the_Data}
California <- read.csv("Filter Pack Concentrations2.csv")

x = c('GLR468','JOT403', 'SEK430','YOS404')

years <- subset(California, California$SITE_ID == x)

years$DATEOFF <- as.Date(years$DATEOFF, format =  '%m/%d/%Y')

years$DATEON <- as.Date(years$DATEON, format = '%m/%d/%Y')

years$UPDATE_DATE <- as.Date(years$UPDATE_DATE, format = '%m/%d/%Y')

years$YEAR <- format(years[,'DATEOFF'], '%Y')

years$MONTH <-format(years[,'DATEOFF'], "%m")


str(years)

Target_data <- subset(years, years$YEAR >= '2018')

Target_data$Particulate <- ((Target_data$TSO4 + Target_data$TNH4 + Target_data$CA + Target_data$MG + Target_data$NA. + Target_data$K + Target_data$NSO4)* Target_data$FLOW_VOLUME)

Target_data$Gaseous <- ((Target_data$TOTAL_NO3 + Target_data$TOTAL_SO2)/Target_data$FLOW_VOLUME)
```

> The United States Environmental Protection Agency maintains a program known as the Clean Air Status and Network (CASTNET). This program is a long-term environmental monitoring network. This network is maintained in the United States and Canada and consists of 97 sites. Established by the 1990 Clean Air Act Amendments to provide accountability for emission reduction programs by reporting trends in pollutant concentrations and acidic deposition. The dataset utilized in this project is a measurement of the weekly ambient concentrations of Suflate (SO4), Nitrate (NO4), Ammonium (NH4), Calcium (Ca), Magnesium (Mg), Sodium (Na), Potassium (K), Chloride (Cl), Nitric Acid (NO3), and Sulfur Dioxide (NO3). 


>>Particle Pollution (PM) inlcudes: Sulfate, Nitrate, Ammonium, Magnesium, Calcium, Potassium, Sodium and Chloride. Based on the 1990 Clean Air Act these fine inhalable particulate matter (PM2.5) thresholds are (per cubic meter of air):
12.0 micrograms (Annual Mean over 3 years) 
15.0 micrograms (Annual Mean over 3 years)
35.0 micrograms (98th Percentile averaged over 3 years)

>>The gaseous pollution of Sulfur Dioxide threshold is 75ppb (196504.05 ug/m3) per hour / .5 ppm (1310.027 ug/m3) per 3 hours. 

>This dataset is an average of each week from January 2000 to June 2020.



# Univariate Plots Section
 
The following graph shows the Air Flow Volume. This shows a centralized grouping around the 30-35 m3 amount. The graph provides a baseline understanding that the identified sites should all have the same Air Flow Volume.

```{r echo=FALSE, Univariate_Plots, warning=FALSE}
qplot(x = FLOW_VOLUME, data = subset(Target_data, !is.na(FLOW_VOLUME)), 
      binwidth = 3) +
  ylab('Occurrences') +
  xlim (0, 75)

summary(Target_data$FLOW_VOLUME)
```

The next graph shows that Sulfate (SO4) is normally low with the majority of occurrences happening around the .5 micro-gram level. The outlier of above 2.0 is a likely contributor to a site's low rating on the Air Quality Rating.

```{r echo=FALSE, Univariate_Plots1, warning=FALSE}
qplot(x = TSO4, data = subset(Target_data, !is.na(TSO4)), 
      binwidth = .2) +
  ylab('Occurrences') 

summary(Target_data$TSO4)
```

This graph shows that nitrates are usually below the 1.5 micro-gram. Again an outlier is present at 4 micro-gram. 

```{r echo=FALSE, Univariate_Plots2, warning=FALSE}
qplot(x = TNO3, data = subset(Target_data, !is.na(TNO3)), 
      binwidth = .4) +
  ylab('Occurrences') 

summary(Target_data$TNO3)
```

The ammonium graph following continues with the meme the previous graphs have shown. A concentration of most occurrences happening on the low side of the chart with a rare occurrence on the high side. 

```{r echo=FALSE, Univariate_Plots3, warning=FALSE}
qplot(x = TNH4, data = subset(Target_data, !is.na(TNH4)), 
      binwidth=.1) +
  ylab('Occurrences')

summary(Target_data$TNH4)
```


Calcium's chart again shows that calcium is usually found in small amounts. However, there is 3 occurrences that can be seen on the high side. 

```{r echo=FALSE, Univariate_Plots4, warning=FALSE}
qplot(x = CA, data = subset(Target_data, !is.na(CA)), 
      binwidth =.05) +
  ylab('Occurrences')

summary(Target_data$CA)
```

Magnesium exhibits the same characteristics of low level concentrations. 

```{r echo=FALSE, Univariate_Plots5, warning=FALSE}
qplot(x = MG, data = subset(Target_data, !is.na(MG)),
      binwidth = .005) +
  ylab('Occurrences')

summary(Target_data$MG)
```

Sodium is completely below the 1 micro-gram level with most closer to the non-existent levels. 

```{r echo=FALSE, Univariate_Plots6, warning=FALSE}
qplot(x = NA. , data = subset(Target_data, !is.na(Target_data$NA.)), 
      binwidth = .05) +
  ylab('Occurrences') 

summary(Target_data$NA.)
```

Potassium's occurrences are below .5 micro-grams for all occurrences. 

```{r echo=FALSE, Univariate_Plots7, warning=FALSE}
qplot(x = K, data = subset(Target_data, !is.na(K)), 
      binwidth = .02) +
  ylab('Occurrences') 

summary(Target_data$K)
```

This sulfate graph shows the results from a nylon filter versus the teflon filter of the previous graph. Nylon provides for more refined capture of material. Becuase of this smaller pore size the sample is smaller. The graph shows that Sulfate is concentrated below the .3 micro-gram level with few outliers. 

```{r echo=FALSE, Univariate_Plots8, warning=FALSE}
qplot(x = NSO4, data = subset(Target_data, !is.na(NSO4)), 
      binwidth = .008) +
  ylab('Occurrences') 

summary(Target_data$NSO4)
```

Nitric Acid is a strong acid that causes acid rain when present in the air. The levels of Nitric Acid in the samples are concentrated below 2 micro-grams. 

```{r echo=FALSE, Univariate_Plots9, warning=FALSE}
qplot(x = NHNO3, data = subset(Target_data, !is.na(NHNO3)), 
      binwidth = .05) +
  ylab('Occurrences') 

summary(Target_data$NHNO3)
```

Another contributor to acid rain is Sulfur Dioxide. The below graph shows that Sulfur Dioxide is mainly concentrated below the 1 micro-gram level. 

```{r echo=FALSE, Univariate_Plots10, warning=FALSE}
qplot(x = WSO2, data = subset(Target_data, !is.na(WSO2)), 
      binwidth = .1) +
  ylab('Occurrences') 

summary(Target_data$WSO2)
```

Below is a snap shot of all the above graphs in one. 

```{r echo=FALSE, Univariate_Plots11, warning=FALSE}
p1 = qplot(x = TNH4, data = subset(Target_data, !is.na(TNH4)), 
           binwidth=.1) +
  ylab('Occurrences')

p2 = qplot(x = WSO2, data = subset(Target_data, !is.na(WSO2)), 
           binwidth = .1) +
  ylab('Occurrences') 

p3 = qplot(x = NHNO3, data = subset(Target_data, !is.na(NHNO3)), 
           binwidth = .05) +
  ylab('Occurrences') 

p4 = qplot(x = TNO3, data = subset(Target_data, !is.na(TNO3)), 
           binwidth = .4) +
  ylab('Occurrences')

p5 = qplot(x = NSO4, data = subset(Target_data, !is.na(NSO4)), 
           binwidth = .008) +
  ylab('Occurrences') 

p6 = qplot(x = TSO4, data = subset(Target_data, !is.na(TSO4)), 
           binwidth = .2) +
  ylab('Occurrences') 

p7 = qplot(x = CA, data = subset(Target_data, !is.na(CA)), 
           binwidth = .2) +
  ylab('Occurrences')

p8 = qplot(x = MG, data = subset(Target_data, !is.na(MG)), 
           binwidth = .2) +
  ylab('Occurrences')

p9 = qplot(x = NA., data = subset(Target_data, !is.na(NA.)), 
           binwidth = .2) +
  ylab('Occurrences')

p10 = qplot(x = K, data = subset(Target_data, !is.na(K)), 
            binwidth = .2) +
  ylab('Occurrences')

p11 = qplot(x = CL, data = subset(Target_data, !is.na(CL)),
            binwidth = .2) +
  ylab('Occurrences')

p12 = qplot(x = TOTAL_SO2, data = subset(Target_data, !is.na(TOTAL_SO2)), 
            binwidth = .2) +
  ylab('Occurrences')

p13 = qplot(x = TOTAL_NO3, data = subset(Target_data, !is.na(TOTAL_NO3)), 
            binwidth = .2) +
  ylab('Occurrences')

p14 = qplot(x = FLOW_VOLUME, data = subset(Target_data, !is.na(FLOW_VOLUME)), 
            binwidth = .2) +
  ylab('Occurrences')

grid.arrange(p1,p2, p3, p4, p5, 
             p6, p7, p8, p9, p10, 
             p11, p12, p13, p14, 
             ncol=3)
```

Glacier National Park is used as our baseline for our comparison as it experiences the best Air Quality rating in the US. 

```{r echo=FALSE, Univariate_Plots12, warning=FALSE}
qplot(x = TNH4, data = subset(Target_data, !is.na(TNH4)), 
      binwidth=.1) +
  ylab('Occurrences') +
  facet_wrap('SITE_ID')
```

This graph shows that YOS404 is the only site that experiences less Ammonium amongst the four locations. 

```{r echo=FALSE, Univariate_Plots13, warning=FALSE}
qplot(x = WSO2, data = subset(Target_data, !is.na(WSO2)), 
      binwidth = .1) +
  ylab('Occurrences')  +
  facet_wrap('SITE_ID')
```

GLR468's Sulfur Dioxide is much lower than SEK430 and YOS 404. However, the concentration for JOT403 and GLR468 are both between 0 and .5 micro-grams. 

```{r echo=FALSE, Univariate_Plots14, warning=FALSE}
qplot(x = NHNO3, data = subset(Target_data, !is.na(NHNO3)), 
      binwidth = .05) +
  ylab('Occurrences')  +
  facet_wrap('SITE_ID')
```

Nitric Acid is extremelow in GLR468. However, JOT403 and SEK430 has nitric acid measurements from .5 to 2.25 micro-grams. 

```{r echo=FALSE, Univariate_Plots15, warning=FALSE}
qplot(x = TNO3, data = subset(Target_data, !is.na(TNO3)), 
      binwidth = .4) +
  ylab('Occurrences') +
  facet_wrap('SITE_ID')
```

Nitrate is significantly lower in GLR 468 and only comparable to YOS404. 

```{r echo=FALSE, Univariate_Plots16, warning=FALSE}
qplot(x = NSO4, data = subset(Target_data, !is.na(NSO4)), 
      binwidth = .008) +
  ylab('Occurrences')  + facet_wrap('SITE_ID')
```

SEK 430 sees Sulfate measurements from 0 to .5 micro-grams. While GLR468 and JOT403 maintain levels at .1. 

```{r echo=FALSE, Univariate_Plots17, warning=FALSE}


qplot(x = TSO4, data = subset(Target_data, !is.na(TSO4)), 
      binwidth = .2) +
  ylab('Occurrences')  +
  facet_wrap('SITE_ID')
```

Sulfate through the Teflon filter shows the same as the Nylon filter. 

```{r echo=FALSE, Univariate_Plots18, warning=FALSE}
qplot(x = CA, data = subset(Target_data, !is.na(CA)), 
      binwidth = .2) +
  ylab('Occurrences')  +
  facet_wrap('SITE_ID')
```

Calcium measured in GLR468, SEK430, and YOS40 are equal and mainly below the .5 micro-gram level. 

```{r echo=FALSE, Univariate_Plots19, warning=FALSE}
qplot(x = MG, data = subset(Target_data, !is.na(MG)), 
      binwidth = .2) +
  ylab('Occurrences')  +
  facet_wrap('SITE_ID')
```

Magnesium in GLR468 adn SEK430 are the exact same while YOS404 has none. 

```{r echo=FALSE, Univariate_Plots20, warning=FALSE}
qplot(x = NA., data = subset(Target_data, !is.na(NA.)), 
      binwidth = .2) +
  ylab('Occurrences')  +
  facet_wrap('SITE_ID')
```

Sodium is not present in GLR468 but is prevalent in JOT403.

```{r echo=FALSE, Univariate_Plots21, warning=FALSE}
qplot(x = K, data = subset(Target_data, !is.na(K)), 
      binwidth = .2) +
  ylab('Occurrences')  +
  facet_wrap('SITE_ID')
```

Chloride is mostly not present in all location. However, JOT403 and SEK430 does have multiple occurrences of chloride.

```{r echo=FALSE, Univariate_Plots22, warning=FALSE}
qplot(x = CL, data = subset(Target_data, !is.na(CL)), 
      binwidth = .2) +
  ylab('Occurrences')  +
  facet_wrap('SITE_ID')
```


# Univariate Analysis


### What is the structure of your dataset?
The data-set contains 20 years of data collected from 9 different observation posts within the United States of America. While the majority (8) of the observations posts are in California the last one is located in Montana (GLR468). The number of week collected range from the newest at 251 week to the oldest at 1048 weeks. GLR468 has 1040 weeks while YOS404 (Yosemite National Park's Turtleback Dome) has 1048 weeks. 

Other Observations:

Based on "https://www.epa.gov/castnet/castnet-ozone-monitoring" website Glacier National Park's GLR468 had the lowest 8-hour daily maximum ozone concentration at 53. This 53 is tied for the lowest concentration for the United States.

Contrarily, YOS404 (Turtleback Dome - Yosemite National Park), SEK430 (Ash Mountain - Sequoia National Park), JOT403 (Joshua Tree National Park) had ratings of 77, 85, 88 respectively. These rating are the highest in the nation and are all in California. 

### What is/are the main feature(s) of interest in your dataset?
The main feature of interest is the comparison between GLR458, YOS404, SEK430, and JOT403. The initial (univariate data plots) are counter intuitive because GLR468 has the highest amount of the identified pollutants. LAV410 had the second highest amount of polluntants and also has the second lowest rating of 66. 

### What other features in the dataset do you think will help support your \
investigation into your feature(s) of interest?
A restriction of time frame will likely show a reduction in air pollutants 

### Did you create any new variables from existing variables in the dataset?

### Of the features you investigated, were there any unusual distributions? \
Did you perform any operations on the data to tidy, adjust, or change the form \
of the data? If so, why did you do this?


# Bivariate Plots Section


```{r echo=FALSE, Bivariate_Plots, warning=FALSE}
ggplot(aes(x = FLOW_VOLUME, y = WSO2), 
       data = subset(Target_data, !is.na(WSO2))) +
  geom_point(alpha = .2, position = position_jitter(h=0)) +
  facet_wrap('SITE_ID')

ggplot(aes(x = FLOW_VOLUME, y = NHNO3), 
       data = subset(Target_data, !is.na(NHNO3))) +
  geom_point(alpha = .2, position = position_jitter(h=0)) +
  facet_wrap('SITE_ID')

ggplot(aes(x = FLOW_VOLUME, y = TNH4),
       data = subset(Target_data, !is.na(TNH4))) +
  geom_point(alpha = .2, position = position_jitter(h=0)) +
  facet_wrap('SITE_ID')


ggplot(aes(x = FLOW_VOLUME, y = TNO3), 
       data = subset(Target_data, !is.na(TNO3))) +
  geom_point(alpha = .2, position = position_jitter(h=0)) +
  facet_wrap('SITE_ID')


ggplot(aes(x = FLOW_VOLUME, y = TSO4), 
       data = subset(Target_data, !is.na(TSO4))) +
  geom_point(alpha = .2, position = position_jitter(h=0)) +
  facet_wrap('SITE_ID')


ggplot(aes(x = DATEOFF, y = TOTAL_NO3), 
       data = Target_data) +
  geom_line() +
  geom_smooth() +
  facet_wrap('SITE_ID')

ggplot(aes(x = DATEOFF, y = TOTAL_SO2), 
       data = Target_data) +
  geom_line() +
  geom_smooth() +
  facet_wrap('SITE_ID')

ggplot(aes(x = DATEOFF, y = WSO2), 
       data = Target_data) +
  geom_line() +
  geom_smooth() +
  facet_wrap('SITE_ID')

ggplot(aes(x = DATEOFF, y = NHNO3), 
       data = Target_data) +
  geom_line() +
  geom_smooth() +
  facet_wrap('SITE_ID')

ggplot(aes(x = DATEOFF, y = NSO4), 
       data = Target_data) +
  geom_line() +
  geom_smooth() +
  facet_wrap('SITE_ID')

ggplot(aes(x = DATEOFF, y = CL), 
       data = Target_data) +
  geom_line() +
  geom_smooth() +
  facet_wrap('SITE_ID')

ggplot(aes(x = DATEOFF, y = K), 
       data = Target_data) +
  geom_line() +
  geom_smooth() +
  facet_wrap('SITE_ID')

ggplot(aes(x = DATEOFF, y = NA.), 
       data = Target_data) +
  geom_line() +
  geom_smooth() +
  facet_wrap('SITE_ID')

ggplot(aes(x = DATEOFF, y = MG), 
       data = Target_data) +
  geom_line() +
  geom_smooth() +
  facet_wrap('SITE_ID')

ggplot(aes(x = DATEOFF, y = CA), 
       data = Target_data) +
  geom_line() +
  geom_smooth() +
  facet_wrap('SITE_ID')

ggplot(aes(x = DATEOFF, y = TNH4), 
       data = Target_data) +
  geom_line() +
  geom_smooth() +
  facet_wrap('SITE_ID')

ggplot(aes(x = DATEOFF, y = TNO3), 
       data = Target_data) +
  geom_line() +
  geom_smooth() +
  facet_wrap('SITE_ID')

ggplot(aes(x = DATEOFF, y = TSO4), 
       data = Target_data) +
  geom_line() +
  geom_smooth() +
  facet_wrap('SITE_ID')
```

A correlation between the Flow Volume and Gaseous measurements does not exist.
```{r echo=FALSE, Bivariate_Plots2, warning=FALSE}
cor.test(Target_data$FLOW_VOLUME, Target_data$Gaseous)
```

A correlation between the Flow Volume and Particulate measurement does not exist.

```{r echo=FALSE, Bivariate_Plots3, warning=FALSE}
cor.test(Target_data$FLOW_VOLUME, Target_data$Particulate)
```

There appears to be a correlation between Particulate and Gaseous measurements. 
```{r echo=FALSE, Bivariate_Plots4, warning=FALSE}
cor.test(Target_data$Particulate, Target_data$Gaseous)
```

```{r}
ggplot(aes(x = Particulate, y= Gaseous), data = Target_data) +
  geom_point()+
  geom_smooth(method = 'lm', color = 'red')

```


# Bivariate Analysis


### Talk about some of the relationships you observed in this part of the \
investigation. How did the feature(s) of interest vary with other features in \
the dataset?

The majority of the data plots have most of their observations around the 30 m^3 air flow volume. Gaseous pollution (S02) is most prevalent in JOT403 and SEK430. SEK430 has significant concentration of pollutants in all of the graphs. JOT403 and SEK430 have the highest and second highest PPM measurements (worst and second worst air quality) within the United States. The graphs confirm that these locations receive a higher concentration of air pollutant.  

### Did you observe any interesting relationships between the other features \
(not the main feature(s) of interest)?

SEK402 which averages 20 m^3 air flow volume consistently shows the highest concentration of PM2.2 and gaseous pollution. However, This inconsistency is not explored because the data for SEK402 ends in the 2005. 

### What was the strongest relationship you found?
Since the 1990 Clean Air Act states have taken significant steps to reduce emissions of pollution. The graphs explored in this section confirm that states are continuing that effort. 

# Multivariate Plots Section


```{r echo=FALSE, Multivariate_Plots, warning=FALSE}

ggplot(aes(x = DATEOFF, y = FLOW_VOLUME), 
       data = Target_data) +
  geom_line(aes(color =SITE_ID)) 

summary(Target_data$FLOW_VOLUME)


ggplot(aes(x= DATEOFF, y= Particulate), 
       data = Target_data)+
  geom_line(aes(color = SITE_ID), 
            stat = "summary", fun = median) +
  geom_smooth(linetype= 2)

summary(Target_data$Particulate)

ggplot(aes(x = DATEOFF, y = Gaseous),
       data = Target_data) +
  geom_line(aes(color = SITE_ID),
            stat = 'summary')+
  geom_smooth( linetype=2)

summary(Target_data$Gaseous)


```

# Multivariate Analysis

### Talk about some of the relationships you observed in this part of the \
investigation. Were there features that strengthened each other in terms of \
looking at your feature(s) of interest?

When looking at the data Glacier National Park, MT has significantly less gaseous and fine particulate matter than any of the sites located in California. The closest population center to Glacier Park is Columbia falls (population 6000) at 17.5 miles to the South West. 

Meanwhile YOS404 168 miles from Sacramento, 193 miles from San Francisco. Joshua Tree (JOT403) is 131 miles from Los Angeles. SEK 430, Ash Mountain, is 60 miles from Fresno and 250 miles from San Francisco. These population centers all have over 500,000 individuals. 



### Were there any interesting or surprising interactions between features?

An interesting interaction of the features was the extreme increase in air flow volume, around January 2019, correlates with the dates of missing data for SEK430 and YOS404.

Additionally, the location where higher population centers are close by the level of pollutants are significantly higher. 

------

# Final Plots and Summary

> **Tip**: You've done a lot of exploration and have built up an understanding
of the structure of and relationships between the variables in your dataset.
Here, you will select three plots from all of your previous exploration to
present here as a summary of some of your most interesting findings. Make sure
that you have refined your selected plots for good titling, axis labels (with
units), and good aesthetic choices (e.g. color, transparency). After each plot,
make sure you justify why you chose each plot by describing what it shows.

### Plot One
```{r echo=FALSE, Plot_One}
ggplot(aes(x= DATEOFF, y= Particulate),
       data = Target_data)+
  geom_line(aes(color = SITE_ID),
            stat = "summary", fun = median) +
  geom_smooth(linetype= 2) +
  ggtitle("Particulate measurement per day")

```

### Description One
This Graph shows the mean of all four sites Particulate matter as a dashed blue line. Observing this graph you can see that GLR468's data points (orange) are consistently below this dashed line. Conversely the two locations with the worse Air Quality rating, JOT403 and SEK430, are significantly above the dashed blue line. 


### Plot Two
```{r echo=FALSE, Plot_Two}
ggplot(aes(x = DATEOFF, y = Gaseous), 
       data = Target_data) +
  geom_line(aes(color = SITE_ID), 
            stat = 'summary')+
  geom_smooth( linetype=2)+
  ggtitle("Gaseous measurement per day")

```

### Description Two

This Graph shows again the mean of all four sites Gaseous pollution as a dashed blue line. Observing this graph you can see that GLR468's data points (orange) are consistently below this dashed line. Conversely the two locations with the worse Air Quality rating, JOT403 and SEK430, are significantly above the dashed blue line. YOS404 the best rated Air Quality in California also has a significant amount of data points below the dashed blue line. 


### Plot Three
```{r echo=FALSE, Plot_Three}
ggplot(aes(x = FLOW_VOLUME, y = Gaseous), 
       data = subset(Target_data, !is.na(Gaseous))) +
  geom_point(alpha = .2, position = position_jitter(h=0)) +
  facet_wrap('SITE_ID')+
  ggtitle("Gaseous Measurements per Air Flow Volume")

```

### Description Three
Finally, this graph shows that no four locations averaged about the same ar Flow Volume (between 30-35 m^3). This eliminates the possibility that maybe the air flow volume increase could throw off the data. GLR468 maintains a low weight of gaseous material, a weight lower than JOT403 (site with worse Air Quality rating). SEK430's graph shows no consistency as the data points range from the top to the bottom of the graph. 

------

# Reflection

The contemporary thought is that anthropogenic climate warming is one of, if the not the greatest threat to the Earth. Although, this exploration of data does not discuss or delve into this question it is clear through this data that human kind greatly contributes to the Air Quality rating. Looking at GLR468, located in Glacier National Park in Montana we see what the potential Air Quality could be for the US. Located outside of the city of Los Angeles with a population of 4 million people, JOT403, has the highest concentration of all the PM25 and Gaseous pollution and the worst Air Quality rating. 

The effects of these pollutants on the environment is not explored in this project either. Nor are the potential causes for these high concentrations. New York City, NY has a population of 8.4 million and the closest monitoring location has a rating of 71, significantly lower than JOT403's 88. Factors that could affect the ratings were not discovered through data. HOwever, Trade Winds, Climatology, volcanic eruptions, geysers, and other environmental factors could explain the discrepencies seen in the Air Quality ratings. 

It is highly likely that human-Kind is the cause for the degredation of Air Quality ratings. Likely fixes run the spectrum but states are clearly adhering to reducing the total emission of pollutants as each site in this study shows a decrease from the original year 2000 data points. 

Sources: 
https://www.epa.gov/cas
https://www.epa.gov/castnet/castnet-ozone-monitoring
https://www.epa.gov/ground-level-ozone-pollution/ground-level-ozone-basics#:~:text=Ozone%20can%20be%20good%20or,on%20where%20it%20is%20found.&text=Learn%20more%20about%20stratospheric%2C%20or,more%20about%20air%20emission%20sources.
tnet/castnet-ozone-monitoring
https://stackoverflow.com/
https://catalog.data.gov/dataset
https://www.epa.gov/aqs
