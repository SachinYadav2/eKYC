# How To Use It This Project
## Step Wise Go to >
### 1 - First Step You Created the Virtual ENV (Because Do'nt need to the external Library Load in my server during the Deployedment).
           -  How to Created the venv 
                    1 - when you are working on the ### Window > python -m venv my_venv_name
                    2 - how to active the venv - .\myenv\Scripts\activate ( this time use a backbard slash)
            Mac Os
                   1 - created using this command python3 -m venv my_venv_name
                   2 - activate the venv using the terminal - source venv/bin/activate (forward and source throw)
### 2 You make sure parrely you main the how much library you are install and Rember the first collect the library how many library you are and check the vestion depndey show that in future you install the all library with any problem
     1 - first how to install the library terminal(your venv shuld be activate) - pip install numpy (when you install the library in inside the jupyter that time !pip install numpy)
     2 - check the how much library are install till now - pip list or pip freeze
     3 - check created the requirements.txt file using this command - pip freeze > requirement.txt (this > sign is tell us you write the text inside the the this txt file this command will on the last stage of the code).
     4 - some time when you copy any project that time you need to directly install the some library - pip install -r requirement.txt this commnad you run 

### 3 Git Related Always kepp in mind you main the flow of git
        1 - git init ( git intialize inside the you project or say folder inside )
        2 - git add . ( all file add in the git virtually)
        3 - git commit -m "Commit to push the login page" ( you commit alwys make some sence)
        4 - git branch -M main  ( if you bracn is not exite that time this is created the brach)
                if exites then you can switch the branc using the git checkout xyz
        4 - only this command will use first time - git remote add origin https://github.com/SachinYadav2/eKYC.git

        4 - git push -u origin main ( push you code with your origin )
            if already push some time - git push (this command may be use some time)

        6 .gitignore ( this file throw you can ignore the file or folder during the git add . time )

        6 - how to revert he last commit 
                1 - check the last commit id (git log --oneline)
                2 - git reset head id
                3 - git push origin main --force

                


### 4 Now Created the Your Project Flow Chart so that you have already id ( that you MR and Team will be help you )
![This Flow Char](https://github.com/SachinYadav2/eKYC/blob/main/images/Flow_Chart.png)


### 5 






