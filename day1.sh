part1=$(cat $1 | sed 's/[^0-9]//g' | awk '{print substr($1, 1, 1),substr($1, length, 1)}' | tr -d " " | awk '{total = total + $1}END{print total}')
echo "Part 1 solution is: ${part1}"