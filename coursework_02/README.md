# Router Data Processing

## Increase DHCP lease time

 Set the DHCP lease time very long (from 12h to 365d) to allow devices to retain their IP addresses for monitoring.

 Edit the following file: `/etc/config/dhcp`

## Data Extraction

### Get visited websites

Router Url:

https://192.168.1.1/webmon.sh


CLI Command:

```bash
cat /proc/webmon_recent_domains
```

Get to local file:

```bash
ssh root@gargoyle "cat /proc/webmon_recent_domains" > webmon_recent_domains.txt
```

### Bandwith Data

Router Url:
https://192.168.1.1/bandwidth.sh

File Url:
https://192.168.1.1/bandwidth.csv

Script Location:
/www/bandwidth.csv

Header format:

```
[Direction],[Interval Length],[Intervals Saved],[IP],[Interval Start],[Interval End],[Bytes Used]
```