Titanic <- read.csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# cleaning data
Titanic$Pclass <- as.numeric(Titanic$Pclass)
Titanic$Age <- ifelse(is.na(Titanic$Age), 70, Titanic$Age) # condition, True statment, false statment

# calculating porbobillity
Titanic$estimated_probabilitiy <- (1/Titanic$Pclass) * (1 - Titanic$Age/100)

# lceaning data, ust in case there is a person above the age of 100; so maximum % is at 100
Titanic$estimated_probabilitiy <- ifelse(estimated_probabilitiy > 1, 1, estimated_probabilitiy)

Titanic_sim <- Titanic %>%
  mutate(
    Pclass = as.numeric(Titanic$Pclass),
    Age = ifelse(is.na(Age), 70, Age),
    estimated_probabilitiy = (1/Pclass) * (1 - Age/100),
    estimated_probabilitiy = ifelse(estimated_probabilitiy > 1, 1, estimated_probabilitiy)
  )

estimated_probabilitiy <- Titanic_sim %>%
  group_by(Pclass) %>%
  summarise(estimated_probabilitiy = mean(estimated_probabilitiy), na.rm = TRUE)