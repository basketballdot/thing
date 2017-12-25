function reverseIp6 {
    echo "$1" | awk -F: 'BEGIN {OFS=""; }{addCount = 9 - NF; for(i=1; i<=NF;i++){if(length($i) == 0){ for(j=1;j<=addCount;j++){$i = ($i "0000");} } else { $i = substr(("0000" $i), length($i)+5-4);}}; print}' | rev | sed -e "s/./&./g"
}


echo "update add $(reverseIp6 "$1")ip6.arpa. 600 IN PTR  $2"
# 2001:dc7::1
#Result:1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.7.c.d.0.1.0.0.2.ip6.arpa.
