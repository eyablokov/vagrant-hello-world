# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/centos-7.2"
  config.vm.box_check_update = true
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "1024"
    vb.name = "hello_world"
  end
  config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
end
