read -p "Enter the full path of the log file: " logFile #asks user for log file

grep -Ei "error|critical" "$logFile" > critical_errors.log #gets lines with error or critical and saves to critical errors

sed -e 's/ERROR/error/g' -e 's/CRITICAL ALERT/critical/g' critical_errors.log > formatted_critical_errors.log #replaces instances of all caps error and critical alert with lowercase

grep -Eo '^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}.*' formatted_critical_errors.log #displays only the timestamp and error message

grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' formatted_critical_errors.log | sort -u | wc -l #counts unique IP addresses

grep -i "failed" formatted_critical_errors.log | head -n 10 #shows first 10 occurances of failed
