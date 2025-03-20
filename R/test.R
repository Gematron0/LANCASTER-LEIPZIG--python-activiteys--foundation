temp_data <- c(25,28,30,29,
               27,26,31,28,
               15,18,20,17,
               16,19,21,18,
               10,12,14,13,
               11,13,15,12)

arr <- array(temp_data,
            dim=c(4,3,2),
              dimnames = list(
                Days = c("Day1","Day2","Day3", "Day4"),
                citys = c("City1","City2","City3"),
                Months = c("Month1","Month2")
              ))

print(arr)