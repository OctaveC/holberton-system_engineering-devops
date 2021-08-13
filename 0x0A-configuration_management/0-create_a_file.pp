# Using Puppet
# Create a File /tmp/holberton

file { '/tmp/holberton':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
