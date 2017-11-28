library(dplyr)

fullDataQ1 <- read.csv("ALKAN_HOLLE_INFO370_a3_cleanData_q1.csv")
fullDataQ2 <- read.csv("ALKAN_HOLLE_INFO370_a3_cleanData_q2.csv")

summaryDataQ1 <- read.csv('Alkan_Holle_a3_q1_summaryData.csv')
summaryDataQ2 <- read.csv('Alkan_Holle_a3_q2_summaryData.csv')


# Question 1 modeling 
#Separate into 4 categories again to start doing independent t tests
menRide <- fullData %>% 
  filter(type == 'Ride', athlete.sex == 'M')
View(menRide)

menRun <- fullData %>% 
  filter(type == 'Run', athlete.sex == 'M')
View(menRun)

womenRide <- fullData %>% 
  filter(type == 'Ride', athlete.sex == 'F')
View(womenRide)

womenRun <- fullData %>% 
  filter(type == 'Run', athlete.sex == 'F')
View(womenRun)


#Because we have already established that the distributions are similar for the two populations but unequal sample sizes and variaces we used a two sample t-tests

#Start by doing each variable independently for cycling
t.test(menRide$distance, womenRide$distance)
t.test(menRide$average_speed, womenRide$average_speed)
t.test(menRide$incline, womenRide$incline)

#Next each variable for running independently
t.test(menRun$distance, womenRun$distance)
t.test(menRun$average_speed, womenRun$average_speed)
t.test(menRun$incline, womenRun$incline)

#finally testing the intensity score we created for both running and cycling. These scores are independent within their fields and not to be directly compared
t.test(menRun$score, womenRun$score)
t.test(menRide$score, womenRide$score)
t.test(menRide$average_speed*menRide$distance, womenRide$average_speed*womenRide$distance)


#Question 2 



