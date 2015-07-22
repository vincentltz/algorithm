data <- read.csv(file="timing6.csv",head=TRUE,sep=",")

y1 = data$timing[data$algorithm=="changegreedy"]
y2 = data$timing[data$algorithm=="changedp"]

df <- data.frame(y1, y2, x = data$size[data$algorithm=="changedp"])

plot(y1 ~ x, data=df, type="p", pch=1, cex=0.5, col="blue", xlim=c(2000, 2200), ylim=c(0, 55), main="Problem 6 Coin Change Timing Plot", xlab="Amount of Change", ylab="Running Time (ms)")

lines(y2 ~ x, data=df, type="p", pch=2, cex=0.8, col="red")

legend(1995, 55.8, c("Change Greedy", "Change DP"), pch=c(1,2), col=c("blue","red"))

dev.copy(png, 'time3.png')
dev.off()