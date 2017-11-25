# Assignment 3 Mini Data Science Project
# Data clean and organization file

library(dplyr)
setwd("~/Desktop/INFO370")
stravaData <- read.csv("strava_activity.csv")

# Making sure we are only looking at workout metadata, entries with an assigned gender, and when the distance, speed, and moving time
# are all greater than 0
stravaData <- filter(stravaData, resource_state == 2, max_speed > 0, max_speed < 45, average_speed > 0, average_speed < 40,
                     is.null(athlete.sex) == FALSE, athlete.sex != "", distance > 0, moving_time > 0)

#running over 100 miles?? Think of other ways to clean the data 
 
stravaData = subset(stravaData, select = c(athlete.sex, type, average_speed, distance, elapsed_time, max_speed, moving_time, 
                                           total_elevation_gain, kudos_count, athlete.country))


write.csv(stravaData, file = "ALKAN_HOLLE_INFO370_a3_cleanData")

write.csv()#second file with different clean where you don't need an assigned gender 

# Questions for Lavi and Li
  # Can I create two output files from Clean for each problem? Or just one, making edits in the EDA script?
  # I don't have a very "statistical" approach to the first problem, is that okay?
  # Is it okay to only analyze Ride, Run, Walk for q 1 and 2 B/C those are the only workouts that have meaningful amounts of data?


