#!/bin/sh
data_path="/opt/sync_notion/data/tmp/data.py"
maining_src="/opt/sync_notion/add_to_notion.py"
data_var="task_list"
log_path="/opt/sync_notion/data/tmp/log.log"
python="/usr/local/bin/python3"

if [ $# -le 0 ]; then
    $python $maining_src > $log_path
    if [ $? ]; then
        rm $data_path
    fi
    exit
fi

title=''
executor=''
num=''
ztime=''

if [ ! -f $data_path ]; then
    echo "# -*- coding: utf-8 -*-" > $data_path
    echo "from ..task import Task" >> $data_path
    echo "$data_var = []" >> $data_path
fi

if [ $# -eq 4 ]; then
    title="$1"
    executor="$2"
    num="$3"
    ztime="$4"
else
    while [ -n "$1" ]; do
        case "$1" in
            -t) shift;title="$1";;
            -e) shift;executor="$1";;
            -n) shift;num="$1";;
            -z) shift;ztime="$1";;
            *) ;;
        esac
        shift
    done
fi

echo "$data_var.append(Task(\"$title\", \"$executor\", \"$num\", \"$ztime\"))" >> $data_path
