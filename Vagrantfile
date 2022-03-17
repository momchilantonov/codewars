# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.ssh.insert_key = false
  config.vm.box = "shekeriev/ubuntu-20-04-server"
  config.vm.provider "virtualbox" do |vb|
    vb.name = "codewars"
    vb.cpus = 2 
    vb.memory = 2048
  end 

  config.vm.synced_folder ".", "/project"
  config.vm.network "forwarded_port", guest: 2200, host: 2200
  config.vm.provision "shell", inline: <<EOS

sudo apt-get update
sudo apt-get install -y python3-venv
python3 -m venv /project/venv

EOS

end