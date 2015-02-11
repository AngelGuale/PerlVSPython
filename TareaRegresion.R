coef=lm(peso$V1 ~ peso$V2)
plot(peso$V2, peso$V1)
abline(coef)
