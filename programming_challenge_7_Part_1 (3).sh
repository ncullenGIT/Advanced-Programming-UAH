read -p "Enter the file name: " file #ask user for file

if [[ ! -f "$file" ]]; then #checks if the file exists
    echo "Error: File does not exist." #notifies user that file does not exist
    exit 1 #exits
else
    echo "File Load Operation Successful" #notifies user that file was found
fi

if grep -q "administrator" "$file"; then #checks if administrator is in the file
    echo "Match found: Please check all security logs" #notifies user that administrator was found
else
    echo "Match not found: Please proceed with system update" #notifies user that a match was not found
fi

grep "Logon ID" "$file" #prints lines with Logon ID
grep -i -e "Account" -e "administrator" "$file" | sed 's/Account/Local/g; s/administrator/local_user/g' #modifies file contents and shows lines

echo "All occurrences of Security ID:"
grep -o "Security ID" "$file" | wc -l #counts and displays total occurrences of security id
echo

echo "Sorted timestamps (YYYY-MM-DD HH:MM:SS):" 
grep -Eo '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}' "$file" | sort #finds and sorts lines chronologically
