Vagrant::Config.run do |config|
  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "lucid64"

  # The url from where the 'config.vm.box' box will be fetched if it
  # doesn't already exist on the user's system.
  config.vm.box_url = "http://files.vagrantup.com/lucid64.box"

  # Assign this VM to a host only network IP, allowing you to access it
  # via the IP.
  # config.vm.network "33.33.33.60"

  # Forward a port from the guest to the host, which allows for outside
  # computers to access the VM, whereas host only networking does not.
  config.vm.forward_port 80, 8080
  config.vm.forward_port 81, 7000

  # Share an additional folder to the guest VM.
  config.vm.share_folder "repo-data", "/server", "."

  # Run some basic provisioning

  tasks = [ "sudo aptitude update",
            "sudo aptitude install -y python-pip git-core",
            "sudo pip install --upgrade pip",
            "sudo aptitude install -y build-essential gcc g++ ack-grep rpl unzip screen locate tree subversion python-dev libjpeg62-dev libfreetype6-dev",
            "sudo aptitude install -y colorgcc colormake colortail libxslt-dev libxml2-dev",
            "cd /server && sudo python ./bootstrap.py && ./bin/buildout"]

  for task in tasks
    config.vm.provision :shell, :inline => task
  end
end
