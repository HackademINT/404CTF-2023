#!/usr/bin/zsh

echo "Generating program..."
python create_pony.py "`python asm.py $1`"
echo "Compiling..."
ponyc