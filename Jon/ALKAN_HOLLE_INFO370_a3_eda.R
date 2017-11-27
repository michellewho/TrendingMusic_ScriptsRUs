# Assignment 3 Mini Data Science Project
# Exploratory data analysis file (For question 1 and question 2)

library(dplyr)
setwd("~/Desktop/INFO370")
cleanStravaData <- read.csv("ALKAN_HOLLE_INFO370_a3_cleanData_q1.csv")

# Problem 1: Do men tend to exercise more intensely (taking into account both distance and speed) than women?

# Isolate different subsets for exploratory plotting

#Create mens riding dataframe
menRide <- cleanStravaData %>%
  filter(type == 'Ride', athlete.sex == 'M') %>%
  select(average_speed, distance, total_elevation_gain)
#View(menRide)

#Create mens running dataframe
menRun <- cleanStravaData %>%
  filter(type == 'Run', athlete.sex == 'M')%>%
  select(average_speed, distance, total_elevation_gain)
#View(menRun)

#Create womens riding dataframe
womenRide <- cleanStravaData %>%
  filter(type == 'Ride', athlete.sex == 'F')%>%
  select(average_speed, distance, total_elevation_gain)
#View(womenRide)

#Create womens rnning dataframe
womenRun <- cleanStravaData %>%
  filter(type == 'Run', athlete.sex == 'F')%>%
  select(average_speed, distance, total_elevation_gain)
#View(womenRun)

#Exploratory plots

# Plots with speed vs. distance
plot(menRide$average_speed, menRide$distance)
plot(menRun$average_speed, menRun$distance)
plot(womenRide$average_speed, womenRide$distance)
plot(womenRun$average_speed, womenRun$distance)

#Plots with speed vs. distance + elevation gain
plot(menRide$average_speed, menRide$distance + menRide$total_elevation_gain)
plot(menRun$average_speed, menRun$distance + menRun$total_elevation_gain)
plot(womenRide$average_speed, womenRide$distance + womenRide$total_elevation_gain)
plot(womenRun$average_speed, womenRun$distance + womenRun$total_elevation_gain)

#Plots with speed + elevation gain/distance vs distance
plot(menRide$average_speed + 10 * (menRide$total_elevation_gain/menRide$distance), menRide$distance)
plot(menRun$average_speed + 10 * (menRun$total_elevation_gain/menRun$distance), menRun$distance)
plot(womenRide$average_speed + 10 * (womenRide$total_elevation_gain/womenRide$distance), womenRide$distance)
plot(womenRun$average_speed + 10 * (womenRun$total_elevation_gain/womenRun$distance), womenRun$distance)


#Summarize and prepare for modelling based on findings

#Create incline variable
cleanStravaData$incline <- cleanStravaData$total_elevation_gain / cleanStravaData$distance

#Summary with just running and riding
summaryStravaRandR <- group_by(cleanStravaData, athlete.sex, type) %>%
  summarise(averageSpeed = mean(average_speed), averageDistance = mean(distance), averageElevationGain = mean(total_elevation_gain), averageIncline = mean(incline), score = (averageSpeed * (averageDistance + (averageElevationGain * 3))), n = n())
View(summaryStravaRandR)

write.csv(summaryStravaRandR, 'Alkan_Holle_a3_q1_summaryData.csv')
write.csv(cleanStravaData, 'Alkan_Holle_a3_q1_rideAndRunDataToBeModeled.csv')

# Problem 2: An interesting question of your choosing that must use at least one of the following: kudos count, athlete country, 
# location country, and/or name.

summaryStrava <- group_by(cleanStravaData, athlete.sex, type) %>%
  summarise(averageSpeed = mean(average_speed), averageDistance = mean(distance), score = (averageSpeed * averageDistance), n = n())
View(summaryStrava)

# Question: 
# What is the correlation between atheltes from different countries and how elevation gain effect the distance they travel when 
# walking, biking, or running? 

cleanStravaData2 <- read.csv("ALKAN_HOLLE_INFO370_a3_cleanData_q2.csv")

# For the eda for this data --> vizualize country vs elevation gain, country vs distance, 
# find distributions for each and get the standard deveation for each
# summary where we aggregate by country and type and plot each with different colors 



