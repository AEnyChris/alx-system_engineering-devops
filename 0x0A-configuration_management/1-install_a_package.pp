# Installs specified version of flask with pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

