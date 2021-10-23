# Fixing Failling Requests

exec {'using sed':
  command => "sed -i 's/15/4096/' /etc/default/nginx",
  path    => '/usr/local/bin/:/bin/',
}

exec {'restart':
  command => 'sudo service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
