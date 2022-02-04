# Task 7.1

See `a.sh`, `b.sh` and `c.sh` in this directory.

There are also `apache_logs.txt` and `example_log.log` files to test scripts.

Examples of `a.sh`:

```
$ m7/task7.1/a.sh 
Available parameters:
        --all           Display the IP addresses and symbolic names of all hosts in the current subnet
        --target        Displays a list of open system TCP ports
```

```
$ m7/task7.1/a.sh --all 192.168.1.0/24
# Nmap 7.92 scan initiated Mon Jan 24 13:58:15 2022 as: nmap -sn -oG - 192.168.1.0/24
Host: 192.168.1.1 (OpenWrt.lan) Status: Up
Host: 192.168.1.178 (pc.lan)    Status: Up
Host: 192.168.1.224 ()  Status: Up
# Nmap done at Mon Jan 24 13:58:18 2022 -- 256 IP addresses (3 hosts up) scanned in 2.74 seconds
```

```
$ m7/task7.1/a.sh --target 192.168.1.1
Starting Nmap 7.92 ( https://nmap.org ) at 2022-01-21 18:27 EET
Nmap scan report for OpenWrt.lan (192.168.1.1)
Host is up (0.00049s latency).
Not shown: 65532 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
53/tcp   open  domain
9100/tcp open  jetdirect

Nmap done: 1 IP address (1 host up) scanned in 2637.33 seconds
```

Examples of `b.sh`:

```
$ m7/task7.1/b.sh 
Available parameters:
        --the-most-requested-ip         Displays from which ip were the most requests.
        --the-most-requested-page       Displays the most requested page.
        --requests-amount-from-ips      Displays how many requests were there from each ip.
        --reffered-non-existed-pages    Displays non-existent pages which clients were referred to.
        --time-with-most-requests       Displays what time did site get the most requests.
        --search-bots                   Displays what search bots have accessed the site.
```

Examples of `b.sh`:

```
$ m7/task7.1/b.sh --the-most-requested-ip m7/task7.1/apache_logs.txt 
157.55.39.250, it was repeated 62 times
```

```
$ m7/task7.1/b.sh --the-most-requested-ip m7/task7.1/example_log.log 
94.78.95.154, it was repeated 29 times
```

```
$ m7/task7.1/b.sh --the-most-requested-page m7/task7.1/apache_logs.txt 
/sitemap1.xml.gz, it was requested 8 times
```

```
$ m7/task7.1/b.sh --reffered-non-existed-pages m7/task7.1/apache_logs.txt 
/error404
/kovboyskie
```

```
$ m7/task7.1/b.sh --time-with-most-requests m7/task7.1/apache_logs.txt 
30/Sep/2015:02:26:55 there were 5 requests
```

```
$ m7/task7.1/b.sh --time-with-most-requests m7/task7.1/example_log.log 
25/Apr/2017:11:40:56 there were 4 requests
```
