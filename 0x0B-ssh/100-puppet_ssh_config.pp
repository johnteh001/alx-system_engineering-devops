#!/usr/bin/puppet
# making changes to configuration file

include stdlib

file_line { 'keylogin':
  ensure => 'present',
  line   => 'IdentityFile ~/.ssh/school',
  path   => '/etc/ssh/ssh_config',
}
file_line { 'pwd':
  ensure => 'present',
  line   => 'PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config',
}