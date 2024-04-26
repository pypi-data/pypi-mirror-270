## cmdline_utils
<br>
A CLI tool, which can be invoked by using clu prompt

```bash
clu publish python package

Publishing a Python package to PyPI
$ python setup.py sdist
$ twine upload dist/*
```

Navigate to https://console.groq.com/keys to setup API KEY

Navigate to https://console.groq.com/docs/models to setup ModelId

### For macOS/Linux:
----------------
To set the GROQ_API_KEY environment variable for your current terminal session, execute the following command:<br>
```bash
export GROQ_API_KEY='your_api_key_here'
```

Replace 'your_api_key_here' with your actual API key.

If you wish to set this variable permanently, add the above line to your shell's startup file, such as ~/.bashrc or ~/.zshrc.

### For Windows Command Prompt:
---------------------------
To set the GROQ_API_KEY environment variable for your current session, execute the following command:

``` bash
set GROQ_API_KEY='your_api_key_here'
```

Replace 'your_api_key_here' with your actual API key.