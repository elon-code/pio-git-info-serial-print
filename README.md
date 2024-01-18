# README #
Version 1.3

### Security Note ###
This script will have access to your file system using python. It will not modify any files, but it will read them. If you are concerned about security, you may want to look at the script and make sure it is not doing anything malicious. It is a very simple script, so it should be easy to understand.

You may also unintentionally reveal information about your project that you do not want to share. Once again, if you are worried please review the script and printouts.

### What is this repository for? ###

The purpose of this respository is to have an Arduino script that you can add to platform IO. The script will create a header file that will give you these as cpp variables. It uses Platform IO's python environment to run the script, so no need to install python. It will also automatically add the generated header file to your .gitignore file, so you don't have to worry about it being tracked by git.

### Summary of set up ###

1. Copy py script to your project folder
2. In your platform.ini file, include this line (replace embed_git_info.py with the name of your script, if different):
```extra_scripts = pre:embed_git_info.py```
3. Include generated header in your main.cpp file: ```#include "git_info.h"```
4. Add a serial printout for your git info:
```
  // This is the recommended setup, you may choose other setups
  Serial.print("Git Information:\n");
  Serial.print("Build Date/Time (local time): "); Serial.print(BUILD_DATE); Serial.print("\n");
  Serial.print("Builder's Name: "); Serial.print(GIT_USER_NAME); Serial.print(" Email: "); Serial.print(GIT_USER_EMAIL); Serial.print("\n");
  Serial.print("Repository URL: "); Serial.print(GIT_REPO_URL); Serial.print("\n");
  Serial.print("Branch: "); Serial.print(GIT_BRANCH); Serial.print(" | Tag: "); Serial.print(GIT_TAG); Serial.print("\n\n"); // Optional, only use if using tags.
  Serial.print("Commit Hash: "); Serial.print(GIT_COMMIT_HASH); Serial.print("\n");
  Serial.print("CRC: "); Serial.println(static_cast<long>(MAIN_FILE_CRC));
  Serial.print("\n=================================\n");

  // These are optional. Not really necessary as it's easy to see who worked on repo by going to link.
  // To enable, go into python script and uncomment.
  //Serial.print("Branch: "); Serial.println(GIT_BRANCH); // Optional, depending on your workflow
  //Serial.print("Git Update Date"); Serial.println(GIT_UPDATE_DATE); // Optional, depending on your workflow

```
or if using streaming library:
```
// Using Streaming Library
  Serial << "Git Information:\n"
    << "Build Date/Time (local time): " << BUILD_DATE << "\n"
    << "Builder's Name:  " << GIT_USER_NAME << " Email: " << GIT_USER_EMAIL  << "\n"
    << "Repository URL: " << GIT_REPO_URL << "\n"
    << "Branch: " << GIT_BRANCH << " | Tag: " << GIT_TAG  << "\n\n"
    << "Commit Hash: " << GIT_COMMIT_HASH << "\n" 
    << "CRC: " << static_cast<long>(MAIN_FILE_CRC) 
    << "\n=================================\n";
```

### Additional Configuration ###

* It is recommended to make a function that does all of this printing, as it helps simplify code. You may organize how you desire, but this is how I prefer it.

* If you are using a non-standard main file (file that is not main.cpp in src folder), you will need to change the following line in the python script:
```main_file = "src/main.cpp"``` to the path of your main file.

* Code will auto-add the main_file path to your gitignore. If you have already tracked it with git, you will need to remove it from git tracking. You can do this with the following command:
```git rm --cached include/git_info.h```

* Another thing to note is that you may want to add some #ifdef statements into your code to make sure it won't printout these headers when running in Arduino IDE. Here is an example of how to do this:
```
#ifdef PLATFORMIO
  // Code to execute only when compiled with PlatformIO
#endif
```
### Dependencies ###

PlatformIO is necessary, this will not work with Arduino IDE. Python is also a dependency, but this script uses platformIO's python environment, so no download or install is necessary. In fact, it is likely this code will not run successfully on your local environment, it is designed to be ran in PlatformIO python environment.

Streaming library is optional, but recommended. It makes printing out the git info much easier. You can find it here: https://github.com/janelia-arduino/Streaming

### Who do I talk to? ###

Repo owner: Elon Goliger egoliger@exploratorium.edu or elon2000@gmail.com