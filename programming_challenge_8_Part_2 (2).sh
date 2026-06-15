awk -F: '$2=="" {print $1}' /etc/shadow > user_audit.txt

awk -F: '$3==0 && $1!="root" {print $1}' /etc/passwd >> user_audit.txt

find / -type f -perm -0002 2>/dev/null > file_audit.txt

find / -type f \( -perm -4000 -o -perm -2000 \) 2>/dev/null >> file_audit.txt

netstat -tuln 2>/dev/null > network_audit.txt

cat /proc/sys/net/ipv4/ip_forward >> network_audit.txt

grep "failed password" /var/log/auth.log | wc -l > failed_logins.txt
