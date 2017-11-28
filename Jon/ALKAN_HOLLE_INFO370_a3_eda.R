# Assignment 3 Mini Data Science Project
# Exploratory data analysis file (For question 1 and question 2)

library(dplyr)
setwd("~/Desktop/INFO370")
cleanStravaData <- read.csv("ALKAN_HOLLE_INFO370_a3_cleanData_q1.csv")
View(cleanStravaData)
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
plot(menRide$average_speed + (10 * menRide$incline), menRide$distance)
plot(menRun$average_speed +  (10 * menRun$incline), menRun$distance)
plot(womenRide$average_speed + (10 * womenRide$incline), womenRide$distance)
plot(womenRun$average_speed + (10 * womenRun$incline), womenRun$distance)

#Getting densities
#mens
m_ride_dis_d <- density(menRide$distance)
m_ride_spe_d <- density(menRide$average_speed)
m_ride_sco_d <- density(menRide$average_speed * menRide$distance)
m_run_dis_d <- density(menRun$distance)
m_run_spe_d <- density(menRun$average_speed)
m_run_sco_d <- density(menRun$average_speed * menRun$distance)
#womens
f_ride_dis_d <- density(womenRide$distance)
f_ride_spe_d <- density(womenRide$average_speed)
f_ride_sco_d <- density(womenRide$average_speed * womenRide$distance)
f_run_dis_d <- density(womenRun$distance)
f_run_spe_d <- density(womenRun$average_speed)
f_run_sco_d <- density(womenRun$average_speed * womenRun$distance)


#Plotting densities
plot(m_ride_dis_d)
plot(m_ride_spe_d)
plot(m_run_dis_d)
plot(m_run_spe_d)
plot(f_ride_dis_d)
plot(f_ride_spe_d)
plot(f_run_dis_d)
plot(f_run_spe_d)

plot(m_ride_sco_d, xlab = "Distance * average speed", col= 'blue', main = "Density of Distance * Speed", xlim= range(c(0, 1600000)), ylim = range(c(0, .0000045)))
par(new=TRUE)
plot(f_ride_sco_d, xlab = '', ylab = '', main = '', col='purple', axes = FALSE, xlim= range(c(0, 1600000)), ylim = range(c(0, .0000045)))


#Summary with just running and riding
summaryStravaRandR <- group_by(cleanStravaData, athlete.sex, type) %>%
  summarise(averageSpeed = mean(average_speed), averageDistance = mean(distance), averageElevationGain = mean(total_elevation_gain), averageIncline = mean(incline), averageScore = mean(score), n = n())
View(summaryStravaRandR)

write.csv(summaryStravaRandR, 'Alkan_Holle_a3_q1_summaryData.csv')

# Problem 2: An interesting question of your choosing that must use at least one of the following: kudos count, athlete country, 
# location country, and/or name.

# Question: 
# What is the correlation between atheltes from different countries and how elevation gain effect the distance they travel when 
# walking or biking? 

cleanStravaData2 <- read.csv("ALKAN_HOLLE_INFO370_a3_cleanData_q2.csv")

# Isolate different workouts by workout for exploratory data analysis 
rides <- cleanStravaData2 %>%
  filter(type == 'Ride')%>%
  select(athlete.country, type, total_elevation_gain, distance, incline)

runs <- cleanStravaData2 %>%
  filter(type == 'Run')%>%
  select(athlete.country, type, total_elevation_gain, distance, incline)

# Highlevel view of the data
plot(cleanStravaData2$total_elevation_gain, cleanStravaData2$distance)

plot(rides$athlete.country, rides$distance)
plot(runs$athlete.country, runs$distance)

plot(runs$athlete.country, runs$total_elevation_gain)
plot(rides$athlete.country, rides$total_elevation_gain)

hist(runs$total_elevation_gain)
hist(rides$total_elevation_gain)
plot(density(runs$total_elevation_gain))
plot(density(rides$total_elevation_gain))

hist(runs$distance)
hist(rides$distance)
plot(density(runs$distance))
plot(density(rides$distance))

# Per-country exploratory plots and subsets for statistical analysis

# Austraila
australiaRide <- rides %>%
  filter(athlete.country == "Australia") %>%
  select(athlete.country, type, total_elevation_gain, distance, incline)
plot(australiaRide$total_elevation_gain, australiaRide$distance)
plot(density(australiaRide$total_elevation_gain))
plot(density(australiaRide$distance))
write.csv(australiaRide, file = "australiaRide.csv")

australiaRuns <- runs %>%
  filter(athlete.country == "Australia") %>%
  select(athlete.country, type, total_elevation_gain, distance, incline)
plot(australiaRuns$total_elevation_gain, australiaRuns$distance)
plot(density(australiaRuns$total_elevation_gain))
plot(density(australiaRuns$distance))
write.csv(australiaRuns, file = "australiaRuns.csv")


# Brazil
brazilRides <- rides %>%
  filter(athlete.country == "Brazil") %>%
  select(athlete.country, type, total_elevation_gain, distance, incline)
plot(brazilRides$total_elevation_gain, brazilRides$distance)
plot(density(brazilRide$total_elevation_gain))
plot(density(brazilRide$distance))
write.csv(brazilRides, file = "brazilRides.csv")

brazilRuns <- runs %>%
  filter(athlete.country == "Brazil") %>%
  select(athlete.country, type, total_elevation_gain, distance, incline)
plot(brazilRuns$total_elevation_gain, brazilRuns$distance)
plot(density(brazilRuns$total_elevation_gain))
plot(density(brazilRuns$distance))
write.csv(brazilRuns, file = "brazilRuns.csv")


# Canada
canadaRides <- rides %>%
  filter(athlete.country == "Canada") %>%
  select(athlete.country, type, total_elevation_gain, distance, incline)
plot(canadaRides$total_elevation_gain, canadaRides$distance)
plot(density(canadaRide$total_elevation_gain))
plot(density(canadaRide$distance))
write.csv(canadaRides, file = "canadaRides.csv")

canadaRuns <- runs %>%
  filter(athlete.country == "Canada") %>%
  select(athlete.country, type, total_elevation_gain, distance, incline)
plot(canadaRuns$total_elevation_gain, canadaRuns$distance)
plot(density(canadaRuns$total_elevation_gain))
plot(density(canadaRuns$distance))
write.csv(canadaRuns, file = "canadaRuns.csv")


# France
franceRides <- rides %>%
  filter(athlete.country == "France") %>%
  select(athlete.country, type, total_elevation_gain, distance, incline)
plot(franceRides$total_elevation_gain, franceRides$distance)
plot(density(franceRides$total_elevation_gain))
plot(density(franceRides$distance))
write.csv(franceRides, file = "franceRides.csv")

franceRuns <- runs %>%
  filter(athlete.country == "France") %>%
  select(athlete.country, type, total_elevation_gain, distance, incline)
plot(franceRuns$total_elevation_gain, franceRuns$distance)
plot(density(franceRuns$total_elevation_gain))
plot(density(franceRuns$distance))
write.csv(franceRuns, file = "franceRuns.csv")


# UK
UKRides <- rides %>%
  filter(athlete.country == "United Kindgom") %>%
  select(athlete.country, type, total_elevation_gain, distance, incline)
plot(UKRides$total_elevation_gain, UKRides$distance)
plot(density(UKRides$total_elevation_gain))
plot(density(UKRides$distance))
write.csv(UKRides, file = "UKRides.csv")

UKRuns <- runs %>%
  filter(athlete.country == "United Kingdom") %>%
  select(athlete.country, type, total_elevation_gain, distance, incline)
plot(UKRuns$total_elevation_gain, UKRuns$distance)
plot(density(UKRuns$total_elevation_gain))
plot(density(UKRuns$distance))
write.csv(UKRuns, file = "UKRuns.csv")


# US
USRides <- rides %>%
  filter(athlete.country == "United States") %>%
  select(athlete.country, type, total_elevation_gain, distance, incline)
plot(USRides$total_elevation_gain, USRides$distance)
plot(density(USRides$total_elevation_gain))
plot(density(USRides$distance))
write.csv(USRides, file = "USRides.csv")

USRuns <- runs %>%
  filter(athlete.country == "United States") %>%
  select(athlete.country, type, total_elevation_gain, distance, incline)
plot(USRuns$total_elevation_gain, USRuns$distance)
plot(density(USRuns$total_elevation_gain))
plot(density(USRuns$distance))
write.csv(USRuns, file = "USRuns.csv")


# Summary  
summaryStravaQ2 <- group_by(cleanStravaData2, athlete.country, type) %>%
  summarise(averageDistance = mean(distance), averageElevationGain = mean(total_elevation_gain), averageIncline = mean(incline), n = n())
View(summaryStravaQ2)

write.csv(summaryStravaQ2, file = "Alkan_Holle_a3_q2_summaryData.csv")


