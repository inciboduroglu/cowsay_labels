#!/usr/bin/env bash

# -v requires bash 4.2>

RND=$(shuf -i 0-${#FLAMG[@]} -n 1)
# The  -b  option initiates  Borg  mode;  -d  causes  the  cow to appear dead; -g invokes greedy mode; -p causes a state of paranoia to come  over  the  cow;  -s makes  the  cow  appear thoroughly stoned; -t yields a tired cow; -w is somewhat the opposite of -t, and initiates wired mode; -y brings on the cow's youthful appearance.
FLAMG=("d" "g" "p" "s" "t" "w" "y")
TFILE=$(mktemp)
FINALFILE=$(mktemp)
# fortune -s | cowsay -W 25 -${FLAMG[$RND]} | tee /dev/stderr

ENOUGH="n"
while [ "$ENOUGH" != "y" ]
do
    OKPRINT="n"
    while [ "$OKPRINT" != "y" ]
    do
        # print short fortunes only
        fortune -s \
            | sed ':a;N;$!ba;s/\n/ /g' \
            | tee $TFILE
        read -p '* Add to quotes? [y/n] ' OKPRINT
    done

    # write each wanted quote
    echo "** You added the following quote to the list:"
    tee -a $FINALFILE < $TFILE
    read -p '* Enough quotes? [y/n] ' ENOUGH
done

echo "got the quotes... Passing them to the python script."
rm -f $TFILE

python main.py < $FINALFILE
rm -f $FINALFILE
