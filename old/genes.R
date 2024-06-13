library(tidyverse)


setwd("/home/francescoc/Desktop/Project/myco/assembly.480.1")

degs <- read.table("DEGs.txt")
genome <- read.csv("proteins_1026_300490.csv", header = T)
gpromoters <- read.table("inter.genes.promoters.bed")

genes <- gpromoters %>%
  filter(V4 %in% degs$V1)

write.table(genes, "DEGs.genes.promoter.bed", sep = "\t", quote = F, row.names = F, col.names = F)


a <- read.table("all.genes.ATTCA.bed")

genes1000 <- a %>%
  filter(V12 %in% degs$V1) %>%
  mutate(diff_plus=V3-V10,
         diff_minus=V2-V11) %>%
  filter(abs(diff_plus) < 1000 | abs(diff_minus) < 1000)


genes100 <- a %>%
  filter(V12 %in% degs$V1) %>%
  mutate(diff_plus=V3-V10,
         diff_minus=V2-V11) %>%
  filter(abs(diff_plus) < 100 | abs(diff_minus) < 100)

write.table(genes1000, "DEGs.genes.1000.txt", sep = "\t", quote = F, row.names = F, col.names = F)
write.table(genes100, "DEGs.genes.100.txt", sep = "\t", quote = F, row.names = F, col.names = F)



a <- read.table("palindr.bed")
genes100 <- a %>%
  filter(V9 %in% degs$V1) 
