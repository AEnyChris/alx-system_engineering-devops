# Fix error in web-settings.php

exec {'fix-server':
  command =>'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
