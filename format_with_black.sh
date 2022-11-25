all_python_files=`find . -type f -name "*.py"`

for file in $all_python_files
do
    black $file
done