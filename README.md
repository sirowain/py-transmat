# Transmat

Upload and download file via WeTransfer from terminal

File upload command uses the [py3wetransfer](https://github.com/fliot/py3wetransfer) module, which supports the WeTransfer Public API V2.

## Install
    
    pip install transmat 
or 

    pip install --user transmat

## Usage

First of all you'll need a valid API Key from [WeTransfer Developers portal](https://developers.wetransfer.com)

    export WETRANSFER_API_KEY=<your-api-key>



#### Upload file(s)

    transmat -u file1 file2 ..

You can also pass a message to be shown in the WeTransfer page
    
    transmat -u file1 file2 .. -m "Here's the files you needed!"
    
#### Download files

    transmat -d https://we.tl/abcdef... 
Multiple files download are automatically zipped by WeTransfer
