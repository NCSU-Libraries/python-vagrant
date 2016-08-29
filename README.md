# Python-Vagrant

## Web Scraping with Python

1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html). **Vagrant 1.8.4 or higher is required.** **Windows users must also install a shell environment** like [Git for Windows](https://git-for-windows.github.io/).
1. Clone or download this repository as a zip file.
1. From a terminal application, navigate to the Python-Vagrant directory, type `vagrant up`, and hit the `Return` key.
1. Once Vagrant is finished, type `vagrant ssh` to access the virtual environment. This environment has been configured to automatically change the directory to `/vagrant/code` on the guest machine.
1. To run the example code, type `python3 example_1.py` in the code directory.

## Vagrant Notes

* The username and password on the guest are both `vagrant`. If the GUI switches to the lock screen, use `vagrant` as the password to login.
* To exit the guest environment, type `exit` from the command line anywhere in the guest.
* To shut down the virtual machine, type `vagrant halt` from within the Python-Vagrant directory on the host.
* To turn on the virtual machine, type `vagrant up` from within the Python-Vagrant directory on the host.
* For more detailed information, visit the [Vagrant Documentation](https://www.vagrantup.com/docs/)

### What this environment includes

* git
* vim
* build-essential
* python3
* python3-dev
* python3-setuptools
* python3-matplotlib
* python3-numpy
* python3-scipy
* python3-pandas
* python3-pil
* pip3
* beautifulsoup4
* requests
* wordcloud
* jupyter
* sympy
* nose
