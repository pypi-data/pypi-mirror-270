# Pymatris 📂


[![Pyversions](https://img.shields.io/pypi/pyversions/pymatris.svg?style=flat-square)](https://pypi.python.org/pypi/pymatris)

Parallel file downloader for HTTP/HTTPS, FTP and SFTP protocols. 




##  How to Use


Make sure you have python>=3.9 installed
Install pymatris from pip
```bash
pip install pymatris
```

In your terminal, run the following command to download files in parallel.
```bash
# Insert single url as argument
pymatris https://storage.data.gov.my/pricecatcher/pricecatcher_2022-01.parquet 

# Or multiple urls 
pymatris https://storage.data.gov.my/pricecatcher/pricecatcher_2022-01.parquet https://storage.data.gov.my/pricecatcher/pricecatcher_2022-02.parquet https://storage.data.gov.my/pricecatcher/pricecatcher_2022-03.parquet
```

```bash
  $ pymatris --help
  usage: pymatris [-h] [--max-parallel MAX_PARALLEL] [--max-splits MAX_SPLITS]
                [--overwrite] [--quiet]
                [--dir DIR] [--print-filenames] [--show-errors SHOW_ERRORS]
                URLS [URLS ...]



```



#### Arguments and Options

##### To provide path to save files, use --dir option. By default files will be saved in current directory.

```bash
pymatris --dir "./" <urls>
```

##### To overwrite existing files, use --overwrite option. By default, files will not be overwritten.

```bash
pymatris --overwrite <urls>
```
_Assuming your have "pricecatcher_2022-01.parquet" file in your current directory, running above command will overwrite the existing file.
During download, Pymatris creates tempfile to download files, if download is interrupted, rest assured that your existing files are safe, and tempfiles will be deleted._

##### To configure number of parallel downloads, use --max-parallel option. By default, 5 parallel downloads are allowed.

```bash
pymatris --max-splits 10 <urls>
```
_Pymatris uses asyncio to download files in parallel. By default, 5 files are downloaded in parallel. You can increase or decrease the number of parallel downloads using --max-parallel option._



##### To configure number of parallel download parts per file, use --max-splits option. By default, 5 parts are downloaded in parallel for each file.

```bash
pymatris --max-splits 10 <urls>
```
_This is only available for HTTP/HTTPS and SFTP protocols. Currently, FTP protocol does not support multipart downloads._


##### To hide progress bar, use --quiet option. By default, progress bar is shown.

```bash
pymatris --quiet <urls>
```




