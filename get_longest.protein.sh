for file in *.fa; do cat $file | cut -d" " -f1,4 | sed 's/gene://' | sed '/^>/ s/$/ /' | tr -s "\s" |  tr -d "\n" | sed 's/>/\n>/g' | sed '1d' | awk -v OFS="\t" '{print $1, $2, $3, length($3)}' | sort -k2,2 -k4nr | awk 'L!=$2 {print $1, $2, $4,"\n" $3} {L=$2}' > $file.out; done        #批量筛选出由可变剪切产生的长度最大的蛋白．其中*.fa代表蛋白质序列文件，提取以空格分割的第1,4列，删除"gene:", 在以">"开头的每行的末尾添加一个空格，删除换行符，用"\n>" 替换">",　删除第一行(因为是空行)，以tab分割的形式打印$1(蛋白ID), $2(基因ID ), $3(蛋白序列)及蛋白序列长度．

sort -k2,2 -k4nr　　　　　#表示先对第２列即基因ID进行排序，基因ID相同的，再按第４列即蛋白质长度进行降序排列．
awk 'L!=$2 {print $1, $2, $4,"\n" $3} {L=$2}'    #将第一行的第二列(基因ID)赋给变量L，并按蛋白ID，基因ID,　蛋白长度，换行，蛋白质序列的格式打印．再将以后每行的第二列与L比较，若L不等于$2，则按上述格式打印，若L等于$2,则不打印

## ediplus 替换
ENST\d{1,} 
 
cat Vigna_angularis.Vigan1.1.cds.all.fa| cut -d" " -f1,4 | sed 's/gene://' | sed '/^>/ s/$/ /' | tr -s "\s" |  tr -d "\n" | sed 's/>/\n>/g' | sed '1d' | awk -v OFS="\t" '{print $1, $2, $3, length($3)}' | sort -k2,2 -k4nr | awk 'L!=$2 {print  ">"$2,"\n" $3} {L=$2}' 

