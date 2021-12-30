## Conda Environment

```bash
conda create -n dsm010 python=3.8
conda init bash
conda activate dsm010
```

### Git LFS

```bash
# download and extract
cd ~/temp
wget https://github.com/git-lfs/git-lfs/releases/download/v3.0.2/git-lfs-linux-amd64-v3.0.2.tar.gz
tar -xvf git-lfs-linux-amd64-v3.0.2.tar.gz

# update the install file and install
nano install.sh
# prefix="/home/jfoul001/"
./install.sh
export PATH=/home/jfoul001/bin:$PATH
nano ~/.bashrc
# add export PATH=/home/jfoul001/bin:$PATH

# add to git repository
cd ~/code/dsm010-2021-oct/
git lfs install
git lfs track "*.txt"
```

## Hadoop

### Local Test

```bash
chmod +x mapper.py reducer.py
cat data/raw/sample.txt  | ./mapper.py | sort | ./reducer.py
```

Upload a sample file to the Hadoop File System.

```bash
hadoop fs -mkdir dsm010
hadoop fs -put ~/code/dsm010-2021-oct/coursework_01/data/raw/sample.txt dsm010
hadoop fs -ls dsm010
```

### Execute Sample Job
```bash
# delete existing output
hadoop fs -rm -r cw1_sample

# execute the job
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar \
    -input dsm010/sample.txt \
    -output cw1_sample \
    -file mapper.py \
    -mapper mapper.py \
    -file reducer.py \
    -reducer reducer.py

# show the output
hadoop fs -cat cw1_sample/part-00000
```

## Web References

- [Hadoop Streaming](https://hadoop.apache.org/docs/r1.2.1/streaming.html)
- [Calculating variance and mean with MapReduce (Python)](https://thedeadbeef.wordpress.com/2010/06/16/calculating-variance-and-mean-with-mapreduce-python/)
- [mapreduce example for calculating standard deviation and median on a sample data](https://timepasstechies.com/map-reduce-example-sd-median/)