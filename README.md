# promo
Projeto que popula promoções - gnome - debian - linux

Dicas:

no arquivo /etc/crontab, adicionar a seguinte linha:

# promo
# */1 *   * * *   <seu_user>  ( cd /home/<seu_user>/promo && /usr/bin/python ./url.py >> /home/<seu_user>/promo/hardmob.log 2>&1 )

Em 1 em 1 minuto se acaso você não viu a promoção, vai aparecer :)