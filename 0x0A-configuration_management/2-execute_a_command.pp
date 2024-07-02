# Executes a command to kill a process using pkill

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => shell,
  path     => ['/bin', '/usr/bin', '/usr/sbin'],
  onlyif   => 'pgrep killmenow',
}
