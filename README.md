# SWEEP Documentation

[![](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](./LICENSE)
[![](https://img.shields.io/badge/framework-Slate-orange.svg)](http://lord.github.io/slate)

This project houses source code/examples for the SWEEP Platform documentation. More detailed documentation at https://docs.sweep.run/.


## Installation
--------------------------

Following commands assume MacOS (please feel free to submit a pull-request for Windows)

```console
$ git clone ...SWEEP-DOCS
$ cd SWEEP-DOCS
$ bundle install
$ bundle exec middleman server
```

Brings up the static website at http://localhost:4567. 

If 'bundle' does not exist, use 'Homebrew' to install
## Building the documentation (if needed)
-----------------------------------------

Create Rakefile, and add the below text to it

```javascript
require 'middleman-gh-pages'
task :default => [:build]
```

To build the site i.e. index.html, CSS etc. do

```console
$ rake build
```

The above command puts the contents of the site in the 'build' directory, next step is to make the static files under the 'gh-pages' branch. Goal is that we want the site to be hosted using GitHub.

```console
$ cd build
$ git checkout -b gh-pages
$ rake publish
```

The content is pushed to gh-pages branch, which is then linked to the custom domain [More here](https://help.github.com/en/articles/using-a-custom-domain-with-github-pages).  

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
