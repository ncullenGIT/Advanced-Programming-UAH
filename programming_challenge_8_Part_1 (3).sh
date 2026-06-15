systemctl stop telnet 2>/dev/null #stops telnet
systemctl disable telnet 2>/dev/null #disables telnet
systemctl stop ftp 2>/dev/null #stops ftp
systemctl disable ftp 2>/dev/null #disables ftp
systemctl stop rsh 2>/dev/null #stops rsh
systemctl disable rsh 2>/dev/null #disables rsh

ufw default deny incoming #denies all incoming traffic
ufw allow 22 #allows ssh traffic
ufw allow 80 #allows http traffic
ufw enable #enables firewall

passwd -l root #expires password
passwd -l guest 2>/dev/null #locks guest account
awk -F: '$2=="" {print "User with no password: "$1}' /etc/shadow #checks file for users with empty passwords and prints them

apt update #updates package lists
apt upgrade -y #upgrades all installed packages
apt autoremove -y #removes unnecessary packages
