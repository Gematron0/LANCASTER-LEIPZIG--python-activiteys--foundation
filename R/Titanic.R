data("Titanic") # grabs a publicly avalable dataset
print(Titanic)

Titanic_df <- as.data.frame(Titanic) # converts the data into a table so its easeyer to read
print(Titanic_df)

print(head(Titanic_df))

plot(Titanic_df$Freq, main = "Titanc Passanger Freq", col = "Green", pch = "16")
plot(Titanic_df$Freq, main = "Titanc Passanger Freq", type = "o")

hist(Titanic_df$Freq, col = "Green")

barplot(Titanic_df$Freq, names.arg = Titanic_df$Class, col = c("green", "Red","Blue","Black"))

boxplot(Titanic_df$Freq, main = "boxplot")

stripchart(Titanic_df$Freq)

pie(table(Titanic_df$Class))

mosaicplot(Titanic)

print("========================================================================================")
TitanicDatasetViaCsv <- read.csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(TitanicDatasetViaCsv)

plot(TitanicDatasetViaCsv$Age, TitanicDatasetViaCsv$Fare, col = "Blue", pch = 16, xlab = "Age", ylab = "Fare", main = "Age V.S., Fare paid (in $)")

sortedAge <- sort(TitanicDatasetViaCsv$Age, na.last = TRUE)
plot(sortedAge, typy = "o", col = "green", main = "Plot of frequency V.S., Age")

barplot(table(TitanicDatasetViaCsv$Pclass, TitanicDatasetViaCsv$Survived), beside = TRUE, legend = c("Dead","Survived"), Main = "Survived count by passangers class")

boxplot(TitanicDatasetViaCsv$Fare)

stripchart(TitanicDatasetViaCsv$Fare, method = "jitter")

pie(table(TitanicDatasetViaCsv$Sex))

qqnorm(TitanicDatasetViaCsv$Age)
qqline(TitanicDatasetViaCsv$Age, col = "Red")

plot(density(na.omit(TitanicDatasetViaCsv$Fare)), main = "Fair dencity plot", col = "Blue")