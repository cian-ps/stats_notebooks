input_dir="notebooks"
output_dir="_posts"
script="custom_nbconvert.py"

if [ ! -d $input_dir ]; then
echo "no such directory: $input_dir"
exit 1
fi

if [ ! -d $output_dir ]; then
echo "no such directory: $output_dir"
exit 1
fi

if [ ! -f $script ]; then
echo "no such file: $script"
exit 1
fi

for file in notebooks/*.ipynb
do
python $script $file
done