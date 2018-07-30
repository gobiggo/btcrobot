#!/bin/bash
#set -e

apt-get -y --force-yes install expect

L=0
for i in `cat email_pool.txt`
do
        email[$L]=`echo $i |awk -F: '{print $1}'`
        iphone[$L]=`echo $i |awk -F: '{print $2}'`
        let "L=$L+1"

done

function scan(){
    expect -c "
            set timeout -1;
            spawn ./hpbscan
            expect {
                    \"*Cellphone number:*\" {send \"$1\r\"; exp_continue}
                    \"*Email address:*\" {send \"$2\r\"; exp_continue}
            }"

    echo "successs complate $2 scan"
}


for((i=0;i<${#email[@]};i++))
do
    echo ${email[$i]}
    echo ${iphone[$i]}
    scan ${iphone[$i]} ${email[$i]}
done

#set +e