#!/bin/bash

function f1 {
    echo Hello from $FUNCNAME!
    VAR="123"
}

f2() {
    p1=$1
    p2=$2
    sum=$((${p1} + ${p2}))
    echo "${sum}"
}

f1
echo ${VAR}

mySum="$(f2 1 2)"
echo mySum = $mySum

mySum="$(f2 10 -2)"
echo mySum = $mySum
