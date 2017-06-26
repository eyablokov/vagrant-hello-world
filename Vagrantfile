# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

    # virtual machine image
    config.vm.box = "ubuntu/xenial64"

    # virtual machine provider & resources
    config.vm.provider "virtualbox" do |vb|
        vb.gui = false
        vb.memory = "2048"
        vb.cpus = "2"
        vb.name = "controller"
    end

    # provision with Ansible
    config.vm.provision "ansible_local" do |ansible|
        ansible.install = true
        ansible.install_mode = "pip"
        ansible.playbook = "playbook.yml"
        ansible.inventory_path = "/vagrant/inventory"
        ansible.limit = "all"
    end

    # virtual machine networking
    config.vm.network "forwarded_port", guest: 8080, host: 8080, host_ip: "127.0.0.1"

end
