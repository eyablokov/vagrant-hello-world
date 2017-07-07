vagrant-hello-world
===================

Deploy simple Flask app, which uses MySQL database to show a content, in a Docker container, inside of VirtualBox.

Tools used
==========

- Ansible (as a software provisioning tool)
- Docker (as a software delivery tool)
- Vagrant (to describe a virtual machine host)
- VirtualBox (as a Vagrant provider)

Description
===========

Stuff in this repository gives just an example how we can use tools, specified above, to describe a software deployment and provisioning.

1. We use Vagrant to create a virtual machine. We use VirtualBox as the provider. Vagrant creates a machine and installs Ansible on it.

2. Using Ansible (`ansible_local`) provisioner, we're going to do all stuff:

- we're installing Docker into this virtual machine, just locally.
- we're going to have 4 Docker containers:
  - "docker-consul" and "docker-registrator", so we can watch and add/remove services we'll have by discovering.
  - "docker-mysql", where we do have a database, used by Flask app, located neighbourly in a container.
  - "docker-flask", where the simple http app located. This app queries the MySQL database to show the result.

Docker containers uses default internal network.
Appropriate subdirectories from the `/vagrant/custom-files` directory are mounted inside containers.

How to run
==========

At the moment, there's a not fixed problem. Running `vagrant up` being in project's directory for the first time. you'll get "Permission denied" error on the "create consul container" Ansible task. Here you should just run `vagrant provision`, and everything will be good.

So, to watch the result:

- clone this repository.
- switch into its directory.
- run `vagrant up`
- {{ you'll face the error above }}
- run `vagrant provision`
- when everything will be done, just open http://127.0.0.1:8080/ in web browser. You'll see 'Hello, World' in a table, which means it works.
