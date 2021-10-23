# Fixing Failling Requests

exec {'increase Ulimit':
  path    => '/usr/local/bin/:/bin/',
}

exec {'nginx':
  path    => ['/bin', '/usr/bin'],
  command => 'sudo service nginx restart',
}
