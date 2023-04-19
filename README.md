# CE4171-IoT-Communications-and-Networking
Application Folder is the Folder containing my Android Studio Files
Local Server is the Folder containing Files that run on server


## Application
My Android Studio Version:

Android Studio 4.1.2 <br>
Build #AI-201.8743.12.41.7042882, built on December 20, 2020 <br>
Runtime version: 1.8.0_242-release-1644-b01 amd64 <br>
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o

You may need to change the dependencies in build.gradle (:app) file as it can be different due to the different of Windows and Android Studion Version.


## Local Server
You need to use the Administrator Privileges to download the TensorFlow, Pillow and Flask using Python command. <br>
To run the Local Server, you need to disable the Windows Firewall so that the packet can communicate with the IoT devices.

For the testing of the Application apk on the Android Devices. <br>
Remember to disable the Windows Firewall, connect the IoT devices on the same network as the Cloud Server (Own PC). <br>
If you are using the Cloud, you can just open the port for the communication purpose.

## To Test using Local Server
1. Run the Local Server then check the IP address.
2. Change the IP address at the Application folder, NetworkClient.java, before you build the apk file.
3. Install the apk file on the Android Devices.
4. Ensure the IoT Devices - Android Devices, and Server are on the same network.
5. Disable the Windows Firewall.
6. Run the Application.
