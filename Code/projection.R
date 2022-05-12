---
title: "Netflix Projection"
author: "Rashad Dixon"
date: "5/9/2022"
output: pdf_document
---

```{r, echo=FALSE, message=FALSE, warning=FALSE, results='hide', include=FALSE}
knitr::opts_chunk$set(echo = TRUE)

all_wdate <- read.csv(here('Data','netflix_titles.csv.')) %>%
  subset(select = -c(12))

shows_wrate <- read.csv(here('data','tv_shows.csv'))
shows_wrate$IMDb <- str_sub(shows_wrate$IMDb,end = -4)
shows_wrate$Rotten.Tomatoes <- str_sub(shows_wrate$Rotten.Tomatoes,end = -5)



stock <- read.csv(here('Data','netflix.csv')) %>%
  separate(Date,into = c('Year','Month','Day'))

movies_wrate <- read.csv(here('Data','MoviesOnStreamingPlatforms.csv'))
movies_wrate$Rotten.Tomatoes <- str_sub(movies_wrate$Rotten.Tomatoes, end = -5)
movies_wrate$IMDb <- 0

```
Interaction variable of The ratings of the shows and where they were available

```{r, echo=FALSE, message=FALSE, warning=FALSE, results='hide', include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
shows_wrate$DIM <- as.numeric(shows_wrate$IMDb) * shows_wrate$Disney.
shows_wrate$AIM <- as.numeric(shows_wrate$IMDb)  * shows_wrate$Prime.Video
shows_wrate$HIM <- as.numeric(shows_wrate$IMDb)  * shows_wrate$Hulu

movies_wrate$DIM <- as.numeric(movies_wrate$Rotten.Tomatoes) * shows_wrate$Disney.
movies_wrate$AIM <- as.numeric(movies_wrate$Rotten.Tomatoes) * shows_wrate$Prime.Video
movies_wrate$HIM <- as.numeric(movies_wrate$Rotten.Tomatoes) * shows_wrate$Hulu



```
Convert daily stock data to monthly to get MoM change in stock price


```{r, echo=FALSE, message=FALSE, warning=FALSE, results='hide', include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
stock$thirtyday_Open <- 0
stock$thirtyday_Close <- 0
stock$n <- 0
for (i in 1:nrow(stock)){
  stock[i,'thirtyday_Open'] <- stock[i,'Open']
  stock[i,'thirtyday_Close'] <- stock[i+29,7]
  stock[i,'n'] <- i
}

stock_thirty <- stock[stock$n == 1 | stock$n %% 30 == 1,]
stock_thirty$perc <- (stock_thirty$thirtyday_Close - stock_thirty$thirtyday_Open)/stock_thirty$thirtyday_Open

```


Merge Shows/Movies/Dates
```{r, echo=FALSE, message=FALSE, warning=FALSE, results='hide', include=FALSE}
all_wrate <- rbind(shows_wrate,movies_wrate)

df <- merge(all_wdate, all_wrate)
```

Note that the `echo = FALSE` parameter was added to the code chunk to prevent printing of the R code that generated the plot.
