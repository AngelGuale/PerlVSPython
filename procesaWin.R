dtperl<-read.csv("angeltt.csv")
tperl<-dtperl["tiempo"]
tperl1<-sapply(tperl, as.numeric)
dpy1<-read.csv("angelvv.csv")
tiempospy<-dpy1["tiempo"]
tiempospy1<-sapply(tiempospy, as.numeric)
t.test(tperl1, tiempospy1)
boxplot(tperl1[1:16], tiempospy1[1:16],xlab="Tiempo de ejecución [s]", horizontal=TRUE)
