awk '/^>/ {printf("\n%s\n",$0);next; } { printf("%s",$0);}  END {printf("\n");}' <  GCF_000015005.1_ASM1500v1_genomic.fna > ASM1500v1_genomic.fa
