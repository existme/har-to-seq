#!/usr/bin/env bash

file=$1

if [ -z "$file" ]; then
  echo "Usage: $0 <har filename>"
  exit 1
fi

python har-uml.py $file | java -jar bin/plantuml.jar -pipe > $file.png
echo "Created $file.png"
open $file.png
