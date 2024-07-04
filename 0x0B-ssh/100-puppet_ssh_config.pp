file_line {'add identity file':
    ensure => 'present'
    path   => '/etc/ssh/ssh_config',
    line   => '    Identity ~/.ssh/school',
}


file_line {'no password':
    ensure => 'present'
    path   => '/etc/ssh/ssh_config',
    line   => '    PasswordAuthentication no',
}
