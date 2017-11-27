# Assignment 3 Mini Data Science Project
# Exploratory data analysis file (For question one and question 2)

library(dplyr)
setwd("~/Desktop/INFO370")
cleanStravaData <- read.csv("ALKAN_HOLLE_INFO370_a3_cleanData.csv")

# Problem 1: Do men tend to exercise more intensely (taking into account both distance and speed) than women?

# Select only the types of exercise that is done by both males and femaels -------> Check and make sure each category has more than X entires? 
cleanStravaData <- filter(cleanStravaData, type %in% c('AlpineSki', 'BackcountrySki', 'Crossfit', 'Hike', 'Kayaking', 'NordicSki', 
                                                       'Ride', 'Run', 'Snowboarding', 'Swim', 'VirtualRide', 'Walk', 'Workout'))


#Create a dataset of only ride & run because of the lack of volume of data for other activities
rideAndRunStravaData <- cleanStravaData %>%
  filter(type %in% c('Run', 'Ride'))
View(rideAndRunStravaData)


#rideAndRunStravaData$intensity <- rideAndRunStravaData$distance


# Isolate different subsets for exploratory plotting
menRide <- rideAndRunStravaData %>%
  filter(type == 'Ride', athlete.sex == 'M') %>%
  select(average_speed, distance, total_elevation_gain)
View(menRide)

menRun <- rideAndRunStravaData %>%
  filter(type == 'Run', athlete.sex == 'M')%>%
  select(average_speed, distance, total_elevation_gain)
View(menRun)

womenRide <- rideAndRunStravaData %>%
  filter(type == 'Ride', athlete.sex == 'F')%>%
  select(average_speed, distance, total_elevation_gain)
View(womenRide)

womenRun <- rideAndRunStravaData %>%
  filter(type == 'Run', athlete.sex == 'F')%>%
  select(average_speed, distance, total_elevation_gain)
View(womenRun)

plot(menRide)
plot(menRun)
plot(womenRide)
plot(womenRun)



summaryStrava <- group_by(cleanStravaData, athlete.sex, type) %>%
  summarise(averageSpeed = mean(average_speed), averageDistance = mean(distance), score = (averageSpeed * averageDistance), n = n())
View(summaryStrava)

#Summary with just running and riding
summaryStravaRandR <- group_by(rideAndRunStravaData, athlete.sex, type) %>%
  summarise(averageSpeed = mean(average_speed), averageDistance = mean(distance), averageElevationGain = mean(total_elevation_gain), score = (averageSpeed * (averageDistance + (averageElevationGain * 3))), n = n())
View(summaryStravaRandR)

write.csv(summaryStravaRandR, 'Alkan_Holle_a3_q1_summaryData.csv')

# Problem 2: An interesting question of your choosing that must use at least one of the following: kudos count, athlete country, 
# location country, and/or name.

# Question: 
  # What is the correlation between atheltes from different countries and how elevation gain effect the distance they travel when 
  # walking, biking, or running? 

