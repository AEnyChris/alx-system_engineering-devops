# change OS config to allow holberton user without error

exec {'modify_hard':
  provider => shell,
  command  => 'sudo sed -i "/holberton hard nofile/s/5/65536/" /etc/security/limits.conf',
}

exec {'modify_soft':
  provider => shell,
  command  => 'sudo sed -i "/holberton soft nofile/s/4/65536/" /etc/security/limits.conf',
}
