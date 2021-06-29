#
# sweep.sh - run cointoss.py with varying numbers of values
#
start=$1
stop=$2
step=$3

for trials in `seq $start $step $stop`
do
	echo "Coin toss with " $trials " trials"
	python cointoss.py $trials
done
