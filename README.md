# responses

`responses` is a simple tool for creating and serving canned JSON responses.
This can be useful for testing services whose interface is defined, but whose
implementation is not yet complete.


### Requirements

1. Python 2.7+
2. pip


### Installation

To install `responses`, start by cloning the repository onto your local machine:

    git clone https://github.com/epochblue/responses

`cd` into the directory that `git` creates and install the necessary requirements
(I recommending doing this inside of a [virtualenv](http://www.virtualenv.org/),
but that is optional):

    pip install -r requirements.txt

And that's it, `responses` is installed and ready to be configured and run.


### Running `responses`

To run the application, run the following command from the project root:

    python responses.py

This should parse your configuration file and start a local server. You can make
sure everything is working by pointing your browser to the URL printed out when
starting the server.


### Configuring `responses`

Configuration for `responses` is done in a [YAML](http://www.yaml.org/) file.
An example file can be seen in the `example/` directory that came with the
project when it was downloaded. It may be easiest to copy this file from the
example directory to the project root directory, which is where `responses`
will look for its configuration:

    cp example/responses.yaml responses.yaml

Open that file in you favorite editor, create your canned responses and restart
`responses`. Happy testing!


## Author

Bill Israel - [@epochblue](https://twitter.com/epochblue) - [http://billisrael.info/](http://billisrael.info/)


## LICENSE

<a rel="license"
     href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="http://i.creativecommons.org/p/zero/1.0/80x15.png" style="border-style: none;" alt="CC0" />
</a>

To the extent possible under law, [Bill Israel](http://billisrael.info/), has
waived all copyright and related or neighboring rights to `responses`. This
work is published from: United States.


