# Assignment 3 Mini Data Science Project
# Data clean and organization file

library(dplyr)
setwd("~/Desktop/INFO370")
stravaData <- read.csv("strava_activity.csv")

# A look into the most popular workouts
typeCount <- group_by(cleanStravaData, type) %>%
  summarise(n = n())
View(typeCount)

# A look into the countries with the most workouts recorded 
countryCount <- group_by(cleanStravaData, athlete.country) %>%
  summarise(n = n())
View(countryCount)

# General filters that apply to both data sets 
stravaData <- filter(stravaData, resource_state == 2, moving_time > 0, distance > 0, max_speed > 0, 
                     average_speed > 0, average_speed < max_speed, total_elevation_gain < 5000, 
                     type == "Ride" && max_speed < 33 && distance < 600000 | 
                     type == "Run" && max_speed < 9.8 && distance < 300000,
                     type == "Ride" | type == "Run")

stravaData$incline <- stravaData$total_elevation_gain / stravaData$distance

# Filter and select data that is relevant to questions 1
stravaData1 <- filter(stravaData, is.null(athlete.sex) == FALSE, athlete.sex != "")
stravaData1$score <- (stravaData$average_speed + stravaData$incline * 10) * stravaData$distance
stravaData1 <- subset(stravaData1, select = c(athlete.sex, type, average_speed, distance, total_elevation_gain, incline, score))

# Filter and select data that is relevant to questions 2
stravaData2 <- filter(stravaData,  
                      athlete.country == 'Australia' |
                      athlete.country == 'Brazil' |
                      athlete.country == 'Canada' |
                      athlete.country == 'France' |
                      athlete.country == 'United Kingdom' |
                      athlete.country == 'United States')
stravaData2 <- subset(stravaData2, select = c(type, athlete.country, total_elevation_gain, distance, incline))

write.csv(stravaData1, file = "ALKAN_HOLLE_INFO370_a3_cleanData_q1.csv")
write.csv(stravaData2, file = "ALKAN_HOLLE_INFO370_a3_cleanData_q2.csv")
