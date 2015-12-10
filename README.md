# promo
Projeto que popula promoções - testado em (gnome - debian) ou (lxde - lubuntu) - linux

Dicas:

Para o serviço iniciar automaticamente quando o sistema operacional é iniciado é necessário que o X esteja "em pé" para o Notify do kernel tenha suporte nos popups. É aconselhável adicionar o autostart no .config do usuário, assim:

# vim /home/seu_usuario/.config/autostart/promo.desktop

No novo arquivo promo.desktop adicione a seguintes linhas:

<pre>
[Desktop Entry]
Name=Promocao
GenericName=Promo
Exec=/opt/promo/url.py
Terminal=false
Categories=Network
Type=Application
StartupNotify=true
X-GNOME-Autostart-enabled=true
</pre>

Pronto! Em 1 em 1 minuto a consulta vai ser gerada, armazenando em banco de dados sqlite para não repetir.
