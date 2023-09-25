# pythonero

Python

pip3 install package_name -t ./

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow


## Miniconda

### https://docs.conda.io/projects/miniconda/en/latest/

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

```bash
~/miniconda3/bin/conda init bash
```


### Create conda enviroment

```bash
conda create --name py311
```

### Activate conda enviroment

```bash
conda activate py311
```

### Install python version

```bash
conda install python=3.11
```


