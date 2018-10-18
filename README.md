# Transmat

Upload and download file via WeTransfer from terminal

## Install
    
    pip install transmat 

## Usage

First of all you'll need a valid API Key from [WeTransfer Developers portal](https://developers.wetransfer.com)

    export WETRANSFER_API_KEY=<your-api-key>



#### Uploading file(s)

    transmat -u file1 file2 ..

You can also pass a message to be shown in the WeTransfer page
    
    transmat -u file1 file2 .. -m "Here's the files you needed!"
    
#### Downloading file

    transmat -d https://we.tl/abcdef... 
Multiple files download are automatically zipped by WeTransfer