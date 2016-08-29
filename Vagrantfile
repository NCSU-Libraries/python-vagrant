# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|

  config.vm.box = "box-cutter/ubuntu1404-desktop"

  config.vm.provider "virtualbox" do |v|
    v.gui = true
  end

  config.vm.hostname = "python-dev"

  config.vm.network "private_network", ip: "192.168.50.30"

  config.vm.network "forwarded_port", guest: 80, host: 14401, auto_correct: true
  config.vm.network "forwarded_port", guest: 3306, host: 14402, auto_correct: true
  config.vm.network "forwarded_port", guest: 5000, host: 14403, auto_correct: true

  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = 'ansible/playbook.yml'
    ansible.inventory_path = 'ansible/inventories/development.ini'
    ansible.limit = 'all'
  end
end
