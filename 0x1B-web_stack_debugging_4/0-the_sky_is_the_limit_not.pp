# Fix failling requests

exec {'using sed to increase limit':
  command => "sed -i 's/15/4000/' /etc/default/nginx",
  path    => '/usr/local/bin/:/bin/',
}

exec {'nginx restart':
  command => 'sudo service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
