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