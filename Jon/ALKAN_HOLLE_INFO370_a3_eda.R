# Assignment 3 Mini Data Science Project
# Exploratory data analysis file (For question one and question 2)

library(dplyr)
setwd("~/Desktop/INFO370")
cleanStravaData <- read.csv("ALKAN_HOLLE_INFO370_a3_cleanData")

# Problem 1: Do men tend to exercise more intensely (taking into account both distance and speed) than women?

# Select only the types of exercise that is done by both males and femaels -------> Check and make sure each category has more than X entires? 
cleanStravaData <- filter(cleanStravaData, type %in% c('AlpineSki', 'BackcountrySki', 'Crossfit', 'Hike', 'Kayaking', 'NordicSki', 
                                                       'Ride', 'Run', 'Snowboarding', 'Swim', 'VirtualRide', 'Walk', 'Workout'))
   
summaryStrava <- group_by(cleanStravaData, athlete.sex, type) %>%
  summarise(averageSpeed = mean(average_speed), averageDistance = mean(distance), score = (averageSpeed * averageDistance), n = n())
View(summaryStrava)

# Problem 2: An interesting question of your choosing that must use at least one of the following: kudos count, athlete country, 
# location country, and/or name.

# Question: 
  # What is the correlation between atheltes from different countries and how elevation gain effect the distance they travel when 
  # walking, biking, or running? 

