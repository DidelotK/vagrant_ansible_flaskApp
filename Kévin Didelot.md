TP DevOps
=========

Note : 16 / 20

[1,5] Définir une VM avec un Vagrantfile
--------------------------------------
OK, la VM est bien définie. Ceci étant dit, vous auriez certainement du utiliser un dossier partagé (config.vm.synced_folder) plutôt que d'utiliser le provisionner "file". En effet, ce dernier va copier le dossier que vous désignez (votre application) dans votre VM, mais uniquement lors du provisioning. Donc si vous changez votre application, mais que vous ne reprovisionez pas votre VM, vous ne verrez pas les changements. Pas très pratique.

Déployer avec Ansible
---------------------

    [1,5] nginx
    -----------
    Ok, vous déployez et configurez nginx. Ceci dit, vos modifications du rôle de palkan le rendent bien moins générique : il y a beaucoup trop de valeurs hard-codées (comme par exemple le port d'écoute du site).
    Enfin, il semble que vous vous marchiez un peu sur les pieds entre les ports d'écoute : votre application flask va écouter sur 0.0.0.0:5000, et vous demandez à nginx d'écouter sur le 127.0.0.1:5000 (pour faire proxy de 127.0.0.1:5000).


    [2] sqlite
    ----------
    Je ne vous reproche pas de ne pas avoir configuré la DB, car nous ne l'utilisons pas vraiment.

    [1,5] supervisord
    ---------------
    Même remarque que pour nginx : le rôle est bon et fonctionne, en revanche, il n'est pas très générique. N'oubliez pas qu'il est probable que vous utilisiez vos rôles pour plein d'applications, autant qu'ils resservent !

    [2,5] gunicorn
    ------------
    Ok, vous déployez gunicorn sur l'ensemble du système, ce qui est probablement un peu overkill. Vous pouviez vous contenter de le déployer au sein de votre virtualenv d'application (et ainsi ne pas polluer le système), et via pip.

[3] Créer une appli Flask "hello world"
---------------------------------------
Wow, ça c'est une application "Hello world" ! Probablement légèrement overkill, mais elle est prète à tout :)
Pour aller plus loin, vous pourriez prendre l'habitude d'avoir aussi un fichier `requirements.txt` et y lister toutes vos dépendances (les librairies, genre `flask` ou `gunicorn`), ce qui vous simplifierait la vie lors du déploiement (`pip install -r requirements.txt`).

[4] Créer un rôle qui déploie l'app Flask
-----------------------------------------
À quelques détails près, votre rôle ansible est vraiment pas mal.
L'activation du virtualenv devrait se faire dans le sccript qui lance l'application. Dans votre cas, vous avez configuré `supervisord` pour lancer une commande `gunicorn` qui elle même lance votre applciation. C'est dans ce script que devrait se trouver l'activation du virtualenv, afin qu'il utilise le gunicorn que vous avez installé au sein du virtualenv (ainsi que toutes les autres dépendances).
Enfin, comme dit plus haut, vous devriez restreindre vos installations via pip (de la lib `flask` par exemple) au virtualenv, pour ne pas polluer le système.
Pour finir, il ne manque qu'une chose à votre rôle : un reload de supervisor, pour qu'il lance l'application que vous aviez configuré plus tôt, et que vous venez de déployer ici !