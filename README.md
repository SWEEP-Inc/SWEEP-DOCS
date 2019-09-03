# SWEEP Documentation

[![](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](./LICENSE)
[![](https://img.shields.io/badge/framework-Slate-orange.svg)](http://lord.github.io/slate)

This project houses source code/examples for the SWEEP Platform documentation. More information documentation at https://docs.sweep.run/.


## Installation
--------------------------

git clone .../SWEEP-DOCS
cd SWEEP-DOCS

## Building the documentation (if needed)
-----------------------------------------

Create Rakefile, and add the below text to it

```javascript


require 'middleman-gh-pages'

task :default => [:build]
```

```console
rake build
```


cd build
$ git checkout -b gh-pages

## Frequently Asked Questions
--------------------------

**Examples and more documentation?**

Go to https://docs.sweep.run/ for API, and detailed documentation


**API documentation template**

Check out [Slate](lord.github.io/slate).

**Apply to SWEEP Beta Platform**

[Apply here](https://beta.sweep.run) for access SWEEP beta platform.

## Would like to Contribute ?
------------------------------

Feel free to submit pull requests with examples, and additional clarifications.



## Need Help? Found a bug?
-----------------------

[Submit an issue](https://github.com/sweep-inc/SWEEP-DOCS/issues) to the SWEEP documentation repo if you need any help. 


##### Credit
https://www.sitepoint.com/writing-api-documentation-slate/
http://altrepo.eu/Myridia/slate/blob/965156d54b10dced25716e36f304203aff8a22dc/Rakefile
