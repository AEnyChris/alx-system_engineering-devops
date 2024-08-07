# Installing and configuring NGINX on Ubuntu server

# update system repo
exec { 'init_commands':
  command  => 'sudo apt-get -y update',
  provider => shell,
  path     => ['/bin', '/usr/bin', '/usr/sbin'],
}

# install nginx
package {'nginx':
  ensure => 'installed'
}

# 'Hello World!' default response configuration
file {'default_reponse':
    ensure  => 'present',
    path    => '/var/www/html/index.html',
    content => 'Hello World!',
}

# 301 redirection configuration

exec {'conf_redirect':
    command  => 'sudo sed -i "/server_name _/a\        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
    provider => shell,
    path     => ['/bin', '/usr/bin', '/usr/sbin'],
}
# Adding custom header to nginx
exec {'add header':
    command  => 'sudo sed -i "55i\        add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
    provider => shell,
    path     => ['/bin', '/usr/bin', '/usr/sbin'],
}

# restart nginx to impliment configuration
exec {'start_nginx':
    command  => 'sudo service nginx start',
    provider => shell,
    path     => ['/bin', '/usr/bin', '/usr/sbin'],
}
