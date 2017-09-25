# Syunik-settings
Set up Syunik mining rigs on Linux 16.04.3

INSTALLATION

1. You need to install NVIDIA drivers on Ubuntu 16.04.3:
    ```
    sudo add-apt-repository ppa:graphics-drivers/ppa 
    sudo apt-get update
    sudo apt-get install nvidia-384
    ```  
    restart Ubuntu
    
2. Enable Overclocking:

    sudo gedit /etc/X11/xorg.conf
    Add following options:
    
        Option	   "Coolbits" "31"
        Option     "RegistryDwords" "PerfLevelSrc=0x2222"
        
    You will end up with something like this:
    
        Section "Screen"
            Identifier     "Screen0"
            Device         "Device0"
            Monitor        "Monitor0"
            DefaultDepth    24
            Option	   "Coolbits" "31"
            Option         "RegistryDwords" "PerfLevelSrc=0x2222"
            SubSection     "Display"
                Depth       24
            EndSubSection
        EndSection

        Section "Screen"
            Identifier     "Screen1"
            Device         "Device1"
            Monitor        "Monitor1"
            DefaultDepth    24
            Option	   "Coolbits" "31"
            Option         "RegistryDwords" "PerfLevelSrc=0x2222"
            SubSection     "Display"
                Depth       24
            EndSubSection
        EndSection
        
    Restart Ubuntu
    
3. Change all necessary settings in sh files and make them boot with the system

Good Luck!
