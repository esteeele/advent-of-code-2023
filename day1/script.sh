cat input.txt | python3 word-replacer.py | sed 's/[^0-9]//g' | awk '{print substr($0, 1, 1) substr($0, length, 1)}' | awk '{ sum += $1 } END { print sum }'
