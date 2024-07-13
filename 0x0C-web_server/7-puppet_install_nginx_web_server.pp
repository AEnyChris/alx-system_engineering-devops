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
file_line {'redirect_conf':
    ensure => 'present',
    path   => '/etc/nginx/sites-available/default',
    after  => 'server_name _',
    line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

# restart nginx to impliment configuration
exec {'start_nginx':
    command  => 'sudo service nginx start',
    provider => shell,
    path     => ['/bin'/, '/usr/bin', '/usr/sbin'],
}
