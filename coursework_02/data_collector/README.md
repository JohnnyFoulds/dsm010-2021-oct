# Bandwidth Data Collector

This is a simple container used to collect bandwidth data from a Gargoyle (OpenWRT based) router.

## Router File System

In the home directory `/root` a shell script named `bandwidth` is created with the content below. The purpose of this file is to extract data and print it to stdout for local collection:

```bash
cat /tmp/bw_backup/do_bw_backup.sh | grep bw_get | sed 's/.*bw_get/bw_get/' | sed 's/\-f .*/-t/g' > /tmp/tmp.bw.sh
sh  /tmp/tmp.bw.sh | sed 's/^[^\-]*\-//g' |  sed 's/\-/,/g'
rm  /tmp/tmp.bw.sh
```

The `ssh/id_rsa.pub` file has been uploaded to the [router](https://192.168.1.1/access.sh) to allow for key based authentication.

## Retieve Bandwidth data

To manually retrieve tha bandwidth data the following command can be used:

```bash
ssh root@gargoyle "/root/bandwidth"
```

## Docker Image

### Build

```bash
docker build -t foulds/bandwidth
```

### Run

```bash
docker run --rm -t -i -v ${PWD}/data:/data foulds/bandwidth
```

## Web References

- [How to run a cron job inside a docker container?](https://stackoverflow.com/questions/37458287/how-to-run-a-cron-job-inside-a-docker-container)