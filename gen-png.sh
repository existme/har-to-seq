#!/usr/bin/env bash

file=$1
./har-uml.py $file | java -jar bin/plantuml.jar -pipe > $file.png
echo "Created $file.png"
open $file.png
