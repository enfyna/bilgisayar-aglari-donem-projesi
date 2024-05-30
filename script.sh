#!/bin/bash

script="scratch/network-simulation"

run_experiment() {
  nDevices=$1
  MaxSpeed=$2
  folder="scratch/experiments/Test_${MaxSpeed}_${nDevices}/run"
  echo -n "Running experiments: "
  for r in $(seq 1 30); do
    echo -n " $r"
    mkdir -p "${folder}${r}"
    ./ns3 run "$script --randomStream=$r --ueNumPergNb=$nDevices --ueVelocity=$MaxSpeed --outputDir=${folder}${r}" > "${folder}${r}/log.txt" 2>&1
  done
  echo " END"
}


run_experiment 2 20


run_experiment 5 20


run_experiment 5 60


run_experiment 10 20
