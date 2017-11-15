library(MASS)
library(dplyr)     # provides data manipulating functions.
library(ggplot2)   # for graphics
# A) Clean Data

# Getting data frame
df <- read.csv("spotify_data_final.csv")

# R-Square Adjusted
df.lm = lm(PeakPos ~ acousticness + danceability + duration_ms + energy + instrumentalness + liveness + loudness + speechiness + tempo + time_signature + valence, data=df)
summary(df.lm)$adj.r.squared

# AIC stepping
fit <- df.lm
step <- stepAIC(fit, direction="both")
step$anova # display results


# final linear regression
df.lm2 = lm(PeakPos ~ acousticness + duration_ms + energy + speechiness + valence, data=df)
print(df.lm2)

d <- df %>% select(PeakPos, acousticness, duration_ms, energy, speechiness, valence)
fit <- lm(PeakPos ~ acousticness + duration_ms + energy + speechiness + valence, data=d)

d <- d[-c(598), ]

d$predicted <- predict(fit)
d$residuals <- residuals(fit)

ggplot(d, aes(x = PeakPos, y = acousticness)) +
  geom_segment(aes(xend = PeakPos, yend = predicted), alpha = .2) +
  geom_point(aes(color = residuals)) +
  scale_color_gradient2(low = "blue", mid = "white", high = "red") +
  guides(color = FALSE) +
  geom_point(aes(y = predicted), shape = 1) +
  theme_bw()

ggplot(d, aes(x = PeakPos, y = duration_ms)) +
  geom_segment(aes(xend = PeakPos, yend = predicted), alpha = .2) +
  geom_point(aes(color = residuals)) +
  scale_color_gradient2(low = "blue", mid = "white", high = "red") +
  guides(color = FALSE) +
  geom_point(aes(y = predicted), shape = 1) +
  theme_bw()

ggplot(d, aes(x = PeakPos, y = energy)) +
  geom_segment(aes(xend = PeakPos, yend = predicted), alpha = .2) +
  geom_point(aes(color = residuals)) +
  scale_color_gradient2(low = "blue", mid = "white", high = "red") +
  guides(color = FALSE) +
  geom_point(aes(y = predicted), shape = 1) +
  theme_bw()

ggplot(d, aes(x = PeakPos, y = speechiness)) +
  geom_segment(aes(xend = PeakPos, yend = predicted), alpha = .2) +
  geom_point(aes(color = residuals)) +
  scale_color_gradient2(low = "blue", mid = "white", high = "red") +
  guides(color = FALSE) +
  geom_point(aes(y = predicted), shape = 1) +
  theme_bw()

ggplot(d, aes(x = PeakPos, y = valence)) +
  geom_segment(aes(xend = PeakPos, yend = predicted), alpha = .2) +
  geom_point(aes(color = residuals)) +
  scale_color_gradient2(low = "blue", mid = "white", high = "red") +
  guides(color = FALSE) +
  geom_point(aes(y = predicted), shape = 1) +
  theme_bw()


