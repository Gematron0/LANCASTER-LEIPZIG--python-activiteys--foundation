TitanicDatasetViaCsv <- read.csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

head(TitanicDatasetViaCsv)

fair_by_class <- tapply(TitanicDatasetViaCsv$Fare, TitanicDatasetViaCsv$Pclass, sum, na.rm = TRUE)

fair_percentage <- round(fair_by_class / sum(fair_by_class) * 100, 2)

passenger_by_class <- table(TitanicDatasetViaCsv$Pclass)

passanger_percentage <- round(passenger_by_class / sum(passenger_by_class) *100, 2)

comparison_matrix <- rbind(fair_percentage, passanger_percentage)

print(comparison_matrix)

barplot(comparison_matrix, beside = TRUE, names.arg = c("1st class", "2nd class", "3ed class"), col = c("gold","skyblue"), legend = c("Fair revenue","passenger distribution by class"))

par(mfrow = c(1,2))

pie(fair_percentage)
pie(passanger_percentage)