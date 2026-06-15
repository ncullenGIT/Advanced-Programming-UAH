inputFormat="png" #input file format
outputFormat="jpg" #output file format
inputDir="$HOME/Documents/Bash_Project_Examples" #default input directory
outputDir="$HOME/Documents/convertedfinal3" #default output directory

useInfo() { #displays instructions
    echo "Usage: $0 [-i input_format] [-o output_format] [-d input_directory] [-D output_directory]"
    echo "Example: $0 -i png -o jpg -d ./images -D ./converted_images"
    exit 1
}

while getopts ":i:o:d:D:" opt; do #loop to set options the user specified
    case $opt in
        i) inputFormat="$OPTARG" ;; #set input format to value passed 
        o) outputFormat="$OPTARG" ;; #set output format to value pased
        d) inputDir="$OPTARG" ;; #set input directory to value passed
        D) outputDir="$OPTARG" ;; #set output directory to value passed
        *) useInfo ;; #calls use function to let the user know the correct formating
    esac #ends case
done

mkdir -p "$outputDir" #create output directory

find "$inputDir" -type f -name "*.$inputFormat" | while read -r file; do #finds all files matching the input in the directory
    mimeType=$(file --mime-type -b "$file") #gets file type and removes the file name
    if [[ "$mimeType" == image/* ]]; then #checks if file starts with image
        filename=$(basename "$file" ."$inputFormat") #gets file name without extension
        magick "$file" "$outputDir/${filename}.${outputFormat}" #converts file 
        echo "Converted: $file -> $outputDir/${filename}.${outputFormat}" #notifies user that file was converted
    fi
done
