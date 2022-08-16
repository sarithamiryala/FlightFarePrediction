# FlightFarePrediction
This is a project to predict flight fare 

# Software and Account requiremenrs

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)



Creating conda enviornment

....

conda create -p newenv python==3.7 -y

...

...

conda activate newenv/

...

OR

...

conda activate newenv

...

pip install -r requirments.txt

To Add files to git

...

git add .

or

...

git add <filename>

...

> Note: To ignore file or folder from git we can write name/folder in .gitignore file

To check the git status

...

git status

....

To check all versions maintained by git

...

git log

....

To create version/commit all changes to git

...

git commit -m "message"

...

To send version/message to git
...

git push origin main

...

To Check remote url
...

git remote -v

...

To set up CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = saritha.jce@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME=  flight-fare-prediction-5



Build Docker Image
...

docker build -t <image_name>: <tagname> .

> Note:  Image name for docker must be lowercase

To list docker image

...

docker images

...

Run docker image

...

docker run -p 5000:5000 -e PORT=5000 85fa9b402bb1
```

To check running container in docker
```
docker ps
```

To stop docker conatiner
```
docker stop <container_id>
```



```
python setup.py install