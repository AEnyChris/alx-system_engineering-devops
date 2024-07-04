# Modify ssh configuration file for no password and priv key addition

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
