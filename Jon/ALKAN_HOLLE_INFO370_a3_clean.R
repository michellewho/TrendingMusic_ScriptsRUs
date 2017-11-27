# Assignment 3 Mini Data Science Project
# Data clean and organization file

library(dplyr)
setwd("~/Desktop/INFO370")
stravaData <- read.csv("strava_activity.csv")


# Noticed the only workouts with significant numbers were Rides and Runs
typeCount <- group_by(cleanStravaData, type) %>%
  summarise(averageSpeed = mean(average_speed), averageDistance = mean(distance), score = (averageSpeed * averageDistance), n = n())
#View(typeCount)

# General filters that apply to both data sets 
stravaData <- filter(stravaData, total_elevation_gain < 8000, distance < 600000, resource_state == 2, moving_time > 0, distance > 0, max_speed > 0, average_speed > 0, max_speed < 33, average_speed < max_speed, 
                     type == "Ride" && max_speed < 33 && distance < 600000 || 
                     type == "Run" && max_speed < 9.8 && distance < 300000)

# Filter and select data that is relevant to questions 1
stravaData1 <- filter(stravaData, is.null(athlete.sex) == FALSE, athlete.sex != "")
stravaData1 <- subset(stravaData1, select = c(athlete.sex, type, average_speed, distance, total_elevation_gain))

# Filter and select data that is relevant to questions 2
stravaData2 <- filter(stravaData, is.null(athlete.country) == FALSE, athlete.country != "")
stravaData2 <- subset(stravaData, select = c(type, athlete.country, total_elevation_gain, distance))


write.csv(stravaData1, file = "ALKAN_HOLLE_INFO370_a3_cleanData_q1.csv")
write.csv(stravaData2, file = "ALKAN_HOLLE_INFO370_a3_cleanData_q2.csv")


