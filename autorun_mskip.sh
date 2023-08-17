
input="list.txt"
while IFS= read -r line
do
echo "Starting ${line}"

python3 metskipper14.py -i ${line}

echo "Ending ${line}"
done < "$input"
echo "################## ALL FILES ARE DONE ########################"


