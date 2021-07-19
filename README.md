This is a GNU Radio module to receive and reencode signals of (some) wireless car key fobs from Hella.


### Development

Like GNU Radio, this module uses *maint* branches for development.
These branches are supposed to be used with the corresponding GNU Radio
branches. This means: the *maint-3.7* branch is compatible with GNU Radio 3.7,
*maint-3.8* is compatible with GNU Radio 3.8, etc.


## Dependencies

GNU Radio


## Installation

```
mkdir build
cd build
cmake ..
make
sudo make install
sudo ldconfig
```

## Usage

See the flow graphs in the apps folder.


## Frame Format and Crypto

I recommend checking out the paper *Lock It and Still Lose It &ndash; On the
(In)Security of Automotive Remote Keyless Entry Systems* by Flavio D. Garcia,
David Oswald, Timo Kasper and Pierre Pavlidès, presented at the 25th USENIX
Security Symposium.

The paper covers the frame format, crypto, and security issues of wireless key
systems. This transceiver supports what the authors call VW-3 and VW-4.
According to my understanding, the WAV files (i.e., signal samples) in this
repository and a firmware dump of the ECU should be a good starting point to
clone key fobs and to extract the master key.

There is also a [Wired
article](https://www.wired.com/2016/08/oh-good-new-hack-can-unlock-100-million-volkswagens/)
on it.


## Further Information

I [blogged](https://www.bastibl.net/gr-keyfob/) about the module and gave a talk
at [SDR Academy](http://www.sdra-2015.de/)
([slides](https://fleark.de/keyfob.pdf) and
[video](https://www.youtube.com/watch?v=EkRZiFSoSZk)).

