TitanicDatasetViaCsv <- read.csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

head(TitanicDatasetViaCsv)

fair_by_class <- tapply(TitanicDatasetViaCsv$Fare, TitanicDatasetViaCsv$Pclass, sum, na.rm = TRUE)

fair_percentage <- round(fair_by_class / sum(fair_by_class) * 100, 2)

print(fair_percentage)

pie(fair_percentage, labels = paste(names(fair_percentage), "Class\n", fair_percentage, "%"), col = c("gold","skyblue","green"), main = "Rev Dist by class (fair %)")

barplot(fair_percentage, names.arg = c("1st class","2nd class","3ed class"), col = c("gold","skyblue","green"), main = "Rev Dist by class (fair %)", ylab = "percentage", xlab = "class")
text(x = c(1,2,3), y = fair_percentage + 2, labels = paste(fair_percentage, "%"))